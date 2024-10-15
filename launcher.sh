#!/bin/bash
source venv/bin/activate
tmux new -s sesionRoyal
sleep 3
python app.py
sleep 5
curl http://localhost:7860
echo "Now detach"
detach
