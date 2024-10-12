#!/bin/bash
cd ${{ secrets.WORK_DIR }} && source venv/bin/activate && python app.py \& && exit
