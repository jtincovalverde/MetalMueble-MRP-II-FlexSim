# MetalMueble MRP II — FlexSim 2027

A portfolio case study that documents the **FlexSim implementation of an MRP II manufacturing-capacity scenario** for a fictitious metal-furniture company.

> **Academic context:** the underlying MRP II case was developed as group coursework. This repository focuses on the FlexSim implementation, automation package, modeling logic, and technical validation used for the simulation component.

## What the model represents

The simulated production flow is:

```mermaid
flowchart LR
    A[Materia Prima] --> B[Cola Corte]
    B --> C[Corte]
    C --> D[Cola Soldadura]
    D --> E[Soldadura]
    E --> F[Cola Ensamble]
    F --> G[Ensamble]
    G --> H[Cola Acabado]
    H --> I[Acabado]
    I --> J[Producto Terminado]
```

The portfolio version models an initial lot of **420 units** over a **40-hour simulation horizon**. The configured processing times are:

| Work center | Process time |
| --- | ---: |
| Corte | 5.6976 min/unit |
| Soldadura | 13.4723 min/unit |
| Ensamble | 8.5046 min/unit |
| Acabado | 10.4762 min/unit |

The expected operational behavior of the case is an accumulation before **Soldadura**, which is the slowest configured process and the intended bottleneck in the scenario.

## What this repository demonstrates

- Manufacturing-process modeling with **FlexSim 2027 Education**
- Automated creation/configuration through **FlexScript**
- Queue visualization and physical flow of work items
- Controlled release of an initial lot of 420 items
- Process-time and capacity configuration
- KPI visualization for work-in-process, waiting time, throughput, and finished units
- A Windows launcher that locates FlexSim and starts the model-building script
- Static package validation through Python and GitHub Actions

## Repository structure

```text
MetalMueble-MRP-II-FlexSim/
├── 01_ABRIR_METALMUEBLE_V23.bat
├── MetalMueble_V23_COLAS_EN_CUADRICULA.txt
├── README.md
├── NOTICE.md
├── .gitignore
├── data/
│   └── capacity_plan.csv
├── scripts/
│   ├── capacity_check.py
│   └── validate_package.py
├── docs/
│   ├── CASE_STUDY.md
│   ├── DIAGNOSTICO_original.txt
│   └── LEEME_original.txt
└── .github/
    └── workflows/
        └── validate.yml
```

## How to run it

### Requirements

- Windows 11 or another compatible Windows environment
- Autodesk FlexSim 2027 / FlexSim 2027 Education
- Internet access the first time the launcher needs to obtain the FlexSim seed model

### Steps

1. Close FlexSim if it is already open.
2. Run `01_ABRIR_METALMUEBLE_V23.bat`.
3. Wait for FlexSim to open and for the script to configure the model.
4. Press **Run** once.
5. Use FlexSim's fast-forward controls to observe the queues, processing stations, and finished-product accumulation.

The launcher copies the FlexScript file into a safe public folder, searches for the local FlexSim executable, obtains a seed model when needed, and launches FlexSim with the script path.

## MRP II capacity context

The FlexSim model belongs to a broader capacity-planning case. The deterministic analysis compares required workload with available capacity across Corte, Soldadura, Ensamble, and Acabado. In the base scenario, Soldadura requires **77.85 h** against **64.77 h** of available capacity, making it the overloaded work center.

A compact dataset is included in `data/capacity_plan.csv`, and the calculation can be reproduced with:

```bash
python scripts/capacity_check.py
```

See [`docs/CASE_STUDY.md`](docs/CASE_STUDY.md) for the portfolio summary of the academic scenario.

## Initial lot logic

The Source is configured with a time-zero arrival and a short inter-arrival interval. The first item is created at `t = 0`; subsequent items are released every `0.06 s`. The OnExit logic stops creation after the 420th item, so the initial lot is released during approximately the first **25.14 simulated seconds**.

The reset trigger restores the original inter-arrival interval so the model can be reset and run again.

## Queue visualization

This V23 version focuses on improving the visual behavior of queues. Instead of stacking items in one vertical tower, queues use **Stack Inside Queue** placement so visible items occupy rows, columns, and additional layers inside the queue area.

The same visual placement is used for the finished-product storage queue.

## KPIs included in the model

The script creates visual indicators for:

- Finished units
- Content of the welding queue
- Average waiting time before welding
- Throughput
- Identified bottleneck

These indicators are intended to make the simulation easier to explain during an operations / MRP II presentation.

## Static validation

Because FlexSim itself is not available in GitHub Actions, CI does **not** claim to execute or prove the simulation runtime. Instead, `scripts/validate_package.py` performs static checks for the portfolio package, including:

- expected 420-unit release logic
- 40-hour stop time
- required process-time values
- required process objects and queue names
- expected KPI definitions
- absence of known problematic legacy references such as `Arrival1` and `creationtrigger`

Run locally with:

```bash
python scripts/validate_package.py
```

## Important limitation

This repository documents the exact automation package and modeling configuration used in the portfolio version. FlexSim runtime behavior must still be verified inside a compatible FlexSim 2027 installation; the GitHub CI check is intentionally limited to static validation.

## Version

**V23 — Colas en cuadrícula**

The principal change from the previous working version is visual queue placement; the package keeps the established process sequence, configured process times, initial lot logic, 40-hour horizon, and KPI layer.
