#!/bin/bash
echo "Activaré source"
source venv/bin/activate
echo "Source Activado"
echo "Crearé sesión royal" 
tmux new -s sesionRoyal
echo "Sesión creada"
echo "Dormiré 3"
sleep 3
echo "Desperté"
echo "Correré python app.py"
python app.py
echo "Corrí python app.py"
echo "Dormiré 5"
sleep 5
echo "Desperté"
echo "Haré curl"
curl http://localhost:7860
echo "Curl hecho"
echo "Detacharé"
echo "Now detach"
detach
echo "Detachado"
