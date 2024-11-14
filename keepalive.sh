#!/bin/bash
timestamp=$(date +"%d-%m-%Y %H:%M:%S")
pid=$(lsof -i :7861 | awk 'NR==2 {print $2}')
if [ -z "$pid" ]; then
  echo "La variable pid está vacía. No se encontró ningún proceso escuchando en el puerto 7861. Entonces si reiniciaré para que exista."
  cd
  cd code/gradio-standalone-do/
  source venv/bin/activate
  python app.py &
  PID=$(pgrep -f "python app.py")
  timestamp2=$(date +"%d-%m-%Y %H:%M:%S")
  echo "Proceso reiniciado: $PID @ $timestamp2"
else
  echo "El PID del proceso es: $pid o sea que hay un proceso corriendo, no hay necesidad de matarlo ni hacer nada más que avisar: ALIVE. $timestamp"
fi

# Pasar esto a un nuevo deply que matará y arrancará pero solo ante cambios.
# kill $pid
#echo "Proceso eliminado: $pid @ $timestamp"
