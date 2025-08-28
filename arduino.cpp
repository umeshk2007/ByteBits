// Define the pin for the sensor
const int sensorPin = A0; // Example: Analog pin for a temperature sensor
void setup() {
  // Start the Serial communication
  Serial.begin(9600);
}
void loop() {
  // Read the sensor value
  int sensorValue = analogRead(sensorPin);
  
  // Convert the sensor value to a meaningful unit (e.g., temperature)
  float voltage = sensorValue * (5.0 / 1023.0); // Convert to voltage
  float temperature = (voltage - 0.5) * 100; // Example conversion for LM35
  // Send the data as CSV
  Serial.print(millis()); // Timestamp
  Serial.print(","); // CSV separator
  Serial.print(temperature); // Sensor value
  Serial.println(); // New line for the next entry
  // Wait for a second before the next reading
  delay(1000);
}