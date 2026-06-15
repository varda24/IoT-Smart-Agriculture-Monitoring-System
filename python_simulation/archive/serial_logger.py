import serial
import csv
from datetime import datetime
from pathlib import Path

ser = serial.Serial("COM5", 115200)

csv_path = Path(__file__).resolve().parent.parent / "data" / "sensor_log.csv"

with open(csv_path, "a", newline="") as file:
    writer = csv.writer(file)

    while True:

        try:

            line = ser.readline().decode(errors="ignore").strip()

            if not line.startswith("CSV:"):
                continue

            line = line.replace("CSV:", "")

            values = line.split(",")

            if len(values) != 6:
                print("Invalid CSV line:", values)
                continue

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                values[0],
                values[1],
                values[2],
                values[3],
                values[4],
                values[5]
            ])

            file.flush()

            print("Logged:", values)

            print(f"""
            Temperature    : {values[0]} °C
            Humidity       : {values[1]} %
            Soil Moisture  : {values[2]} %
            Water Level    : {values[3]} %
            Light          : {values[4]}
            Pump Status    : {"ON" if values[5]=='1' else "OFF"}
            ---------------------------------
            """)

        except Exception as e:
            print("Error:", e)
