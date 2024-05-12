source env/bin/activate
while true; do
  python3 ./AI/extract_db.py
  python3 ./AI/bin.py
done