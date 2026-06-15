import csv
import random
import time
from datetime import datetime

CSV_FILE = "../data/sensor_log.csv"

while True:

    temperature = random.randint(25, 40)
    humidity = random.randint(40, 90)
    soil = random.randint(10, 90)
    water = random.randint(20, 100)
    light = random.randint(500, 4000)

    pump = "ON" if soil < 30 else "OFF"

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            temperature,
            humidity,
            soil,
            water,
            light,
            pump
        ])

    print(
        f"Temp={temperature}°C "
        f"Soil={soil}% "
        f"Water={water}% "
        f"Pump={pump}"
    )

    time.sleep(3)