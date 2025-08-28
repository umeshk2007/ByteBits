import serial
import time

ser = serial.Serial('COM3', 9600)
time.sleep(2)

with open('sensor_data.csv', 'w') as file:
    file.write('Timestamp,Pressure,Humidity,Temperature,Strength\n')

    # Set defaults for Pressure, Humidity, Strength (replace with actual readings if available)
    default_pressure = 1.0
    default_humidity = 1.0
    default_strength = 1.0

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip() # "Timestamp,Temperature"
            parts = line.split(',') 
            if len(parts) == 2:
                timestamp, temperature = parts
                # Compose full input line
                full_line = f"{timestamp},{default_pressure},{default_humidity},{temperature},{default_strength}"
                file.write(full_line + '\n')
                print(full_line)
