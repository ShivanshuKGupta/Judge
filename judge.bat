@echo off

python -u %~dp0/main.py %*

if %errorlevel% neq 0 (
    echo Judge Failed to Succesfully Complete its Execution.
    pause
)