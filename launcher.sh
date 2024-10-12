#!/bin/bash
echo "Entrando"
echo "Voy a ejecutar la activación del venv"
source venv/bin/activate 
echo "venv activado"
echo "voy a hacer ls"
ls
echo "ls realizado"
echo "voy a hacer el deploy"
python app.py \& 
echo "deploy en background hecho"
echo "finalmente voy hacia la salida"
exit
echo "salida realizada"
