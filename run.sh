#!/bin/bash

# activate the virtual environment if not already activated
source env/bin/activate
# start the Ai script in the background before starting the main script and save output to a file called anomaly.log, save the pid of the process to a file called anomaly.pid and destroy the process when the main script is stopped
python3 ./AI/anomaly.py > anomaly.log 2>&1 &
echo $! > anomaly.pid
docker compose up -d
echo "Your Deep Learning powered IDS is running..."
while true; do
  python3 main.py
  python3 ./AI/extract_db.py
  python3 ./AI/bin.py
done
# stop the Ai script when the main script is stopped
kill $(cat anomaly.pid)
rm anomaly.pid