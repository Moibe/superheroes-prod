#!/bin/bash

COMPOSE="/usr/bin/docker-compose --ansi never"
DOCKER="/usr/bin/docker"

cd code/gradio-standalone-do/
$COMPOSE run certbot renew --dry-run && $COMPOSE kill -s SIGHUP webserver
$DOCKER system prune -af
