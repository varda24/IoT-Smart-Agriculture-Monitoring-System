"""Entry point for the Smart Agriculture Monitoring System."""

from python_simulation.archive.serial_logger import simulate_sensor_data


def main():
    data = simulate_sensor_data()
    print("Simulated sensor data:", data)


if __name__ == "__main__":
    main()
