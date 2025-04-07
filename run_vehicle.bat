@echo off
echo =============================================
echo  Iniciando o container vehicle_client...
echo =============================================

REM Navega até a pasta onde está o docker-compose.yml
cd /d ".\app\Vehicle"

REM Executa o container com terminal interativo
docker compose run --rm -it --service-ports vehicle

echo =============================================
echo  Execução finalizada.
echo =============================================
pause