@echo off

set script_dir=%~dp0

for %%i in ("%script_dir%.") do set "parent_dir=%%~fi"
for %%* in ("%parent_dir%") do set parent_name=%%~nx*

rem echo script_dir: %script_dir%
rem echo parent_dir: %parent_dir%
rem echo parent_name: %parent_name%

pyinstaller --onefile --noconfirm --log-level=INFO %parent_name%.py
