@echo off
echo Playing Assyncronic (⁠◕⁠‿⁠◕⁠)...

:: Verifying if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)
python -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies (pygame)...
    pip install pygame
)

:: Playing the program
python main.py
pause