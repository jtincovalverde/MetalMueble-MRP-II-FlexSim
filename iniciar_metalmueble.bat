@echo off
setlocal EnableExtensions
TITLE MetalMueble - FlexSim 2027

set "WORK_DIR=%PUBLIC%\MetalMueble"
if not exist "%WORK_DIR%" mkdir "%WORK_DIR%"
copy /B /Y "%~dp0modelo_metalmueble.txt" "%WORK_DIR%\modelo_metalmueble.txt" >nul

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

set "BASE_MODEL=%WORK_DIR%\modelo_base.fsm"
if not exist "%BASE_MODEL%" (
  echo Preparando el modelo base de FlexSim...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/flexsim/ai-course-materials/main/HelloWorld/HelloWorld.fsm' -OutFile '%BASE_MODEL%'"
)
if not exist "%BASE_MODEL%" (
  echo [ERROR] No se pudo preparar el modelo base de FlexSim.
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
start "" "%FLEX%" "%BASE_MODEL%" /maintenance disablemsg_runscript /scriptpath "%WORK_DIR%\modelo_metalmueble.txt"
exit /b 0
