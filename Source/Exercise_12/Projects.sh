@echo off
cls
echo "**********************************************"
echo This batch file will create a project directory
echo This is for demonstration purposes only.
echo "**********************************************"
echo *** press [ctrl][c] to exit or any key to continue ***
pause
set /p NAME=Enter the name of the project, then press [return]
echo Creating Projects
mkdir Projects
cd Projects
mkdir Documentation
mkdir Tests
mkdir Examples
mkdir Source
cls
dir
echo "**********************************************"
echo Finished creating project Projects
echo "**********************************************"
cd ..
