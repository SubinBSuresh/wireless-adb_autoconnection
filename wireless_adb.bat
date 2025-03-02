@echo off

ipconfig > conf.txt
python get_gateway_ip.py > gateway_ip.txt

set /p gateway_ip= < gateway_ip.txt

if "%gateway_ip%" == "Error" (
    echo Could not get gateway IP
    exit /b 1
)
echo Checking for other Wi-Fi ADB connections...
for /f "tokens=1" %%i in ('adb devices ^| findstr /C:":5555" ^| findstr /V /C:"%gateway_ip%:5555"') do (
    adb -s %%i disconnect
    echo Disconnected: %%i
)

echo Gateway IP: %gateway_ip%

rem Add your adb commands here, using %gateway_ip%
adb tcpip 5555
timeout /t 2 >nul
adb connect %gateway_ip%:5555
adb devices

del conf.txt
del gateway_ip.txt