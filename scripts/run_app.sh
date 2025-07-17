#!/bin/bash

set -e

if command -v docker compose &>/dev/null; then
    DC="docker compose"
elif command -v docker-compose &>/dev/null; then
    DC="docker-compose"
else
    echo "❌ Docker Compose is not installed!"
    exit 1
fi
echo -e "\n"
echo "▶️ Starting Noxer App..."
docker compose up -d --build
echo "✅ Noxer App is running."
docker compose up -d --build
clear
echo -e "\n\n"
echo -n "Starting"
for i in {1..5}; do
    sleep 0.5
    echo -n "."
done
echo
echo "▶You can access the API server at:"
echo "http://$(hostname -I | awk '{print $1}'):5555/info"
echo -e "\n\n"