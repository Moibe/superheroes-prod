#!/bin/bash
source venv/bin/activate
python app.py & 
sleep 5
curl http://localhost:7860
