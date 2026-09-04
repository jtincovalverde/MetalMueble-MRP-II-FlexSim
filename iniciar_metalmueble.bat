@echo off
setlocal EnableExtensions
TITLE MetalMueble - FlexSim 2027

set "SAFE_DIR=%PUBLIC%\FlexSimAuto"
if not exist "%SAFE_DIR%" mkdir "%SAFE_DIR%"
copy /B /Y "%~dp0MetalMueble_V23_COLAS_EN_CUADRICULA.txt" "%SAFE_DIR%\MetalMuebleV23.txt" >nul

set "FLEX="
for %%F in (
  "C:\Program Files\Autodesk\FlexSim 2027\program\flexsim.exe"
  "C:\Program Files\FlexSim 2027\program\flexsim.exe"
  "C:\Program Files\FlexSim\FlexSim 2027\program\flexsim.exe"
) do if exist "%%~F" set "FLEX=%%~F"
if not defined FLEX for /f "delims=" %%F in ('where /R "C:\Program Files" flexsim.exe 2^>nul') do if not defined FLEX set "FLEX=%%F"
if not defined FLEX (
  echo [ERROR] No se encontro flexsim.exe de FlexSim 2027.
  pause
  exit /b 1
)

set "SEED=%SAFE_DIR%\FlexSimSeed.fsm"
if not exist "%SEED%" (
  echo Preparando el modelo base de FlexSim...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/flexsim/ai-course-materials/main/HelloWorld/HelloWorld.fsm' -OutFile '%SEED%'"
)
if not exist "%SEED%" (
  echo [ERROR] No se pudo obtener FlexSimSeed.fsm.
  pause
  exit /b 2
)

echo ================================================================
echo   MetalMueble - simulacion MRP II
echo ================================================================
echo.
echo Preparando el modelo de 420 piezas en FlexSim 2027...
echo.
echo Cuando FlexSim abra, pulsa Ejecutar una sola vez.
echo.
start "" "%FLEX%" "%SEED%" /maintenance disablemsg_runscript /scriptpath "%SAFE_DIR%\MetalMuebleV23.txt"
exit /b 0
