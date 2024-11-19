#!/bin/bash
timestamp=$(date +"%d-%m-%Y %H:%M:%S")
pid=$(lsof -i :7880 | awk 'NR==2 {print $2}')
kill $pid
echo "Proceso eliminado: $pid @ $timestamp"
#Mejorar éste proceso porque ésa busqueda a veces encuentra varios procesos y no mata al correcto y causa desperfectos. 
#En cambio los logs de crontabs te dicen exactamente cual está corriendo y ese es el que debes de quitar. 
#FUTURE: Por ahora bastará con hacer kill y dejar que el cron corra, en el futuro el cron podría guardar el valor y que ese sea usado por deployer en su kill.
sleep 5

cd
cd code/ocean-devo-superheroes/
source venv/bin/activate
python app.py &
PID=$(pgrep -f "python app.py")
timestamp2=$(date +"%d-%m-%Y %H:%M:%S")
echo "Proceso reiniciado: $PID @ $timestamp2"
