#!/bin/bash
echo "Entrando"
which python
echo "Voy a ejecutar la activación del venv"
source venv/bin/activate 
echo "venv activado"
echo "Haré which python otra vez"
which python
echo "voy a hacer ls"
ls
echo "ls realizado"
echo "voy a hacer el deploy"
python app.py 
echo "deploy en background hecho"
echo "finalmente voy hacia la salida"
exit
echo "salida realizada"
