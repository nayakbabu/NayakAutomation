[Unit]
Description=Custom health check service
After=network.target

[Service]
Type=oneshot
ExecStart=/home/satya/cloudelabday1/healthcheck.sh
User=satya