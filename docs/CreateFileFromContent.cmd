@echo off
setlocal enabledelayedexpansion

REM Loop through each line in content.txt
for /F "tokens=1* delims=:" %%a in (content.txt) do (
    REM Trim whitespace for title and path
    set "title=%%a"
    set "path=%%b"
    set "title=!title:~1!"
    set "path=!path:~1!"

    REM Create the directory if it doesn't exist
    if not exist "!path!\.." mkdir "!path!\.."

    REM Write the title to the file
    echo # !title! > "!path!"
)

endlocal
