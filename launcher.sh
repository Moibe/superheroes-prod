#!/bin/bash
source venv/bin/activate && python app.py \& && exit || echo "Command Failed"
