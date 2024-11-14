#!/bin/bash
pid=$(lsof -i :7860 | awk 'NR==2 {print $2}')
kill $pid

sleep 5

timestamp=$(date +"%d-%m-%Y %H:%M:%S")
echo "Proceso eliminado: $pid @ $timestamp"

cd
cd code/gradio-standalone-do/
source venv/bin/activate
python app.py
echo "Proceso reiniciado."
