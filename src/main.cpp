#include <Arduino.h>
#include <DHTesp.h>

#define DHT_PIN 15

#define SOIL_PIN 34
#define WATER_PIN 32
#define LDR_PIN 35

#define PUMP_LED 2

DHTesp dht;

void setup() {

  Serial.begin(115200);

  dht.setup(DHT_PIN, DHTesp::DHT22);

  pinMode(PUMP_LED, OUTPUT);

  delay(1000);
}

void loop() {

  TempAndHumidity data = dht.getTempAndHumidity();

  // Skip invalid DHT readings
  if (isnan(data.temperature) || isnan(data.humidity)) {
    delay(3000);
    return;
  }

  int soilRaw = analogRead(SOIL_PIN);
  int waterRaw = analogRead(WATER_PIN);
  int lightRaw = analogRead(LDR_PIN);

  int soilPercent = map(soilRaw, 0, 4095, 100, 0);
  int waterPercent = map(waterRaw, 0, 4095, 0, 100);

  soilPercent = constrain(soilPercent, 0, 100);
  waterPercent = constrain(waterPercent, 0, 100);

  bool pumpStatus = false;

  if (soilPercent < 30) {
    digitalWrite(PUMP_LED, HIGH);
    pumpStatus = true;
  }
  else {
    digitalWrite(PUMP_LED, LOW);
    pumpStatus = false;
  }

  // CSV FORMAT
  // temperature,humidity,soil,water,light,pump
// ---------- HUMAN READABLE OUTPUT ----------

Serial.println("--------------------------------");

Serial.print("Temperature: ");
Serial.print(data.temperature);
Serial.println(" C");

Serial.print("Humidity: ");
Serial.print(data.humidity);
Serial.println(" %");

Serial.print("Soil Moisture: ");
Serial.print(soilPercent);
Serial.println(" %");

Serial.print("Water Level: ");
Serial.print(waterPercent);
Serial.println(" %");

Serial.print("Light Intensity: ");
Serial.println(lightRaw);

Serial.print("Pump Status: ");

if (pumpStatus)
  Serial.println("ON");
else
  Serial.println("OFF");

if (soilPercent < 30)
  Serial.println("ALERT: LOW SOIL MOISTURE");

if (data.temperature > 35)
  Serial.println("ALERT: HIGH TEMPERATURE");

if (waterPercent < 20)
  Serial.println("ALERT: LOW WATER LEVEL");


delay(3000);
}