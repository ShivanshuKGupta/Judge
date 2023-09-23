@echo off
setlocal enabledelayedexpansion

echo Checking for an installation of python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo fatal: Python is not installed or not in PATH.
    exit /b 1
)

echo Checking for an installation of node (npm)
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo fatal: node is not installed or not in PATH.
    echo Please install node from https://nodejs.org/ then run this script.
    exit /b 1
)

set "current_location=%~dp0"
setx PATH "%current_location%;%PATH%" /M

echo judge has been added to the PATH environment variable.
echo Please restart any open command prompts for the changes to take effect.

echo Installing @dodona/dolos
npm install -g @dodona/dolos

echo Installation Complete.
pause
exit
endlocal
