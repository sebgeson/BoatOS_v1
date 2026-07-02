#!/bin/bash
set -e

chmod +x /home/sgson/BoatOS/scripts/start_boatos.sh

sudo tee /etc/systemd/system/boatos.service > /dev/null <<'EOF'
[Unit]
Description=BoatOS Marine Dashboard
After=network.target

[Service]
User=sgson
WorkingDirectory=/home/sgson/BoatOS
ExecStart=/home/sgson/BoatOS/scripts/start_boatos.sh
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable boatos.service
sudo systemctl restart boatos.service

echo "BoatOS service installerad."
