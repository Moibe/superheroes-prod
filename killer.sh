#!/bin/bash
echo "Entrando a killer"
pid=$(lsof -i :7860 | awk 'NR==2 {print $2}')
echo "Proceso to kill:"
echo "PID: $pid"
kill $pid
echo "Killed"
