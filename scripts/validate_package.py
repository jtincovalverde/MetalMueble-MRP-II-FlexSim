from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "MetalMueble_V23_COLAS_EN_CUADRICULA.txt"
LAUNCHER = ROOT / "iniciar_metalmueble.bat"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    require(SCRIPT.exists(), f"Missing {SCRIPT.name}")
    require(LAUNCHER.exists(), f"Missing {LAUNCHER.name}")

    text = SCRIPT.read_text(encoding="utf-8-sig")
    bat = LAUNCHER.read_text(encoding="utf-8-sig")

    required_tokens = [
        'materiaPrima.name = "Materia_Prima"',
        'colaCorte.name = "Cola_Corte"',
        'corte.name = "Corte"',
        'colaSoldadura.name = "Cola_Soldadura"',
        'soldadura.name = "Soldadura"',
        'colaEnsamble.name = "Cola_Ensamble"',
        'ensamble.name = "Ensamble"',
        'colaAcabado.name = "Cola_Acabado"',
        'acabado.name = "Acabado"',
        'productoTerminado.name = "Producto_Terminado"',
        'corte.setProperty("ProcessTime", [5.6975772765, "min"])',
        'soldadura.setProperty("ProcessTime", [13.4722614342, "min"])',
        'ensamble.setProperty("ProcessTime", [8.5045948204, "min"])',
        'acabado.setProperty("ProcessTime", [10.4761904762, "min"])',
        'materiaPrima.setProperty("TimeZeroArrival", 1)',
        'materiaPrima.setProperty("InterArrivalTime", 0.06)',
        'current.stats.output.value >= 419',
        'stoptime(hours(40))',
        'CUELLO DE BOTELLA: SOLDADURA',
        'setProperty("ItemPlacement", "Stack Inside Queue")',
    ]

    for token in required_tokens:
        require(token in text, f"Expected token not found: {token}")

    forbidden_tokens = [
        "Arrival1",
        "creationtrigger",
        "FlowItemBin",
    ]

    # Ignore explanatory comments when checking known legacy implementation paths.
    import re
    code = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    code = re.sub(r"//.*", "", code)

    for token in forbidden_tokens:
        require(token not in code, f"Forbidden legacy implementation token found in executable code: {token}")

    require("flexsim.exe" in bat.lower(), "Launcher does not search for flexsim.exe")
    require("/scriptpath" in bat.lower(), "Launcher does not invoke FlexSim with /scriptpath")

    # 419 intervals after the t=0 item => 420 items in ~25.14 s.
    release_window = 419 * 0.06
    require(abs(release_window - 25.14) < 1e-9, "Initial lot timing check failed")

    print("Static package validation passed.")
    print("Expected lot: 420 units")
    print(f"Initial release window: {release_window:.2f} simulated seconds")
    print("Simulation horizon: 40 hours")
    print("Expected bottleneck: Soldadura")
    print("Note: FlexSim runtime execution is not tested by this script.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
