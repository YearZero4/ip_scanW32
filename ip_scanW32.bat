@echo off
set /p ip= ^<^<^< Direccion IP A Escanear ^>^>^>  
echo Escaneando Direccion IP ^> %ip% & echo.
setlocal enabledelayedexpansion
set "resultados="
for /f "tokens=1,2,3 delims=." %%a in ("%ip%") do set ipx=%%a.%%b.%%c.

for /L %%a in (0,1,99) do (
echo ^<^>^<^> Progreso -^> %%a%%
ping -w 1 -n 1 %ipx%%%a | find /i "ttl" >nul && (
set "resultados=!resultados! %ipx%%%a"
)
)
echo.
set /a n=1
if defined resultados (
echo ^<^>^<^>^<^> Direcciones IP encontradas ^<^>^<^>^<^> & echo.
echo ---^> [%n%] !resultados!
set /a n+=1
) else (
echo No se encontraron direcciones IP.
)
echo.
echo El escaneo a finalizado
pause >nul
