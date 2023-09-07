@ECHO OFF

set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || ( echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

powercfg.exe /hibernate off
winget 1> nul 2> nul || goto installWinget
pip3 show tk 1> nul 2> nul || goto installTkinter
goto exit

:installWinget
curl -L https://github.com/microsoft/winget-cli/releases/download/v1.1.12653/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle -o wingetInstaller.msixbundle
wingetInstaller.msixbundle
pip3 show tk 1> nul 2> nul || goto installTkinter
goto exit

:installTkinter
pip3 install tk
goto exit

:exit
pip3 install -r requirements.txt
cd ../Documentation/
Xcopy "CheatSheet SANS" %userprofile%\Desktop\"CheatSheet SANS" /E/H/C/I