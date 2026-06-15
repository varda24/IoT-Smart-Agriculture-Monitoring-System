# 🌱 IoT-Enabled Smart Agriculture Monitoring System

## 📌 Project Overview

The IoT-Enabled Smart Agriculture Monitoring System is a smart farming solution designed to monitor environmental and soil conditions in real time. The system collects data from multiple sensors, including temperature, humidity, soil moisture, water level, and light intensity sensors, and displays the information on an interactive dashboard.

The project demonstrates how IoT technologies can be used to automate irrigation decisions, reduce water wastage, improve crop productivity, and support data-driven agriculture practices.

This project was developed using ESP32, Wokwi simulation, Python, and Streamlit. Since physical hardware was unavailable, Wokwi was used for virtual embedded system simulation and Python was used to generate and analyze sensor data.

---

# 🎯 Problem Statement

Traditional farming often relies on manual observation of soil and environmental conditions. This approach can lead to:

* Excessive water consumption
* Delayed irrigation decisions
* Crop stress due to environmental changes
* Lack of real-time monitoring
* Reduced agricultural efficiency

The objective of this project is to provide a smart monitoring system that continuously tracks important agricultural parameters and assists in irrigation management.

---

# 🚀 Features

* Real-time agricultural parameter monitoring
* Soil moisture analysis
* Temperature and humidity monitoring
* Water level monitoring
* Light intensity monitoring
* Automatic irrigation decision logic
* Pump ON/OFF simulation
* Alert generation for critical conditions
* Data logging using CSV files
* Interactive Streamlit dashboard
* Auto-refreshing live dashboard
* Wokwi-based virtual IoT simulation
* GitHub-ready project structure

---

# 🛠 Technology Stack

## Embedded Systems

* ESP32
* Arduino Framework
* PlatformIO
* Wokwi Simulator

## Sensors

* DHT22 Temperature and Humidity Sensor
* Soil Moisture Sensor (Simulated)
* Water Level Sensor (Simulated)
* LDR Sensor (Simulated)

## Software

* Python
* Streamlit
* Pandas
* Plotly

## Development Tools

* VS Code
* Git
* GitHub

---

# 📐 System Architecture

```text
+-------------------------+
|      Sensor Layer       |
+-------------------------+
| DHT22                   |
| Soil Moisture Sensor    |
| Water Level Sensor      |
| LDR Sensor              |
+------------+------------+
             |
             v
+-------------------------+
|         ESP32           |
+-------------------------+
| Sensor Reading          |
| Threshold Logic         |
| Pump Control            |
| Alert Processing        |
+------------+------------+
             |
             v
+-------------------------+
| Data Logging Layer      |
+-------------------------+
| CSV Storage             |
+------------+------------+
             |
             v
+-------------------------+
| Streamlit Dashboard     |
+-------------------------+
| KPI Cards               |
| Charts                  |
| Alerts                  |
| Reports                 |
+-------------------------+
```

---

# ⚙️ Project Workflow

```text
Sensor Data Collection
          ↓
ESP32 Processing
          ↓
Threshold Evaluation
          ↓
Pump Decision Logic
          ↓
Data Logging
          ↓
Dashboard Visualization
          ↓
Alert Generation
```

---

# 📂 Project Structure

```text
IoT-Smart-Agriculture-Monitoring-System/
│
├── src/
│   └── main.cpp
│
├── dashboard/
│   └── app.py
│
├── python_simulation/
│   ├── sensor_generator.py
│   └── archive/
│       └── serial_logger.py
│
├── data/
│   └── sensor_log.csv
│
├── images/
│   ├── wokwi_circuit.png
│   ├── dashboard.png
│   ├── pump_on.png
│   ├── pump_off.png
│   ├── alerts.png
│   └── folder_structure.png
│
├── docs/
│
├── circuit_diagram/
│
├── README.md
├── requirements.txt
├── platformio.ini
├── diagram.json
└── wokwi.toml
```

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/IoT-Smart-Agriculture-Monitoring-System.git

cd IoT-Smart-Agriculture-Monitoring-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Dashboard

```bash
streamlit run dashboard/app.py
```

Open the browser at:

```text
http://localhost:8501
```

---

# 📊 Dashboard Features

The Streamlit dashboard provides:

* Live KPI cards
* Temperature monitoring
* Humidity monitoring
* Soil moisture monitoring
* Water level monitoring
* Interactive charts
* Alert notifications
* Downloadable CSV reports

---

# 🚨 Alert Conditions

| Condition           | Alert             |
| ------------------- | ----------------- |
| Soil Moisture < 30% | Low Soil Moisture |
| Temperature > 35°C  | High Temperature  |
| Water Level < 20%   | Low Water Level   |
| Soil Moisture < 30% | Pump ON           |

---

# 📸 Screenshots

## Wokwi Circuit Simulation

Add screenshot:

```text
images/wokwi_circuit.png
```

## Dashboard

Add screenshot:

```text
images/dashboard.png
```

## Pump ON State

Add screenshot:

```text
images/pump_on.png
```

## Pump OFF State

Add screenshot:

```text
images/pump_off.png
```

## Alert Monitoring

Add screenshot:

```text
images/alerts.png
```

---

# 📈 Sample Sensor Data

| Temperature | Humidity | Soil Moisture | Water Level | Pump |
| ----------- | -------- | ------------- | ----------- | ---- |
| 33°C        | 76%      | 68%           | 44%         | OFF  |
| 39°C        | 80%      | 15%           | 62%         | ON   |
| 28°C        | 65%      | 75%           | 70%         | OFF  |

---

# 🎓 Learning Outcomes

Through this project, the following concepts were explored:

* Internet of Things (IoT)
* Embedded Systems Development
* ESP32 Programming
* Sensor Integration
* Data Acquisition
* Automation Logic
* Dashboard Development
* Data Visualization
* CSV Data Logging
* GitHub Project Management

---

# 🔮 Future Enhancements

* MQTT Integration
* Blynk Mobile Application
* ThingSpeak Cloud Integration
* Weather API Integration
* SMS Notifications
* Email Alerts
* AI-Based Irrigation Prediction
* Crop Recommendation System
* Mobile Dashboard Application
* Cloud Database Integration

---

# 💼 Interview Explanation

### Explain Your Project

I developed an IoT-Enabled Smart Agriculture Monitoring System using ESP32, Wokwi simulation, Python, and Streamlit. The system monitors temperature, humidity, soil moisture, water level, and light intensity. Based on predefined thresholds, it simulates irrigation decisions and pump control. Sensor readings are logged into CSV files and visualized through a real-time dashboard. The project demonstrates IoT architecture, sensor integration, automation logic, and data visualization techniques commonly used in smart farming applications.

---

# 📝 Note

A serial logger implementation is included in the archive folder for future physical ESP32 deployment. Since physical hardware was unavailable, Wokwi simulation and a Python-based sensor generator were used to emulate real-time agricultural sensor data.

---

# 👨‍💻 Author

**Varda Kunde**


