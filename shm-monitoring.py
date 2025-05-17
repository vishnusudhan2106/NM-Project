import random
import time

# Define threshold values
VIBRATION_THRESHOLD = 5.0   # in mm/s
STRAIN_THRESHOLD = 300      # in microstrain

# Simulate sensor data
def read_vibration_sensor():
    return round(random.uniform(0.0, 10.0), 2)

def read_strain_sensor():
    return random.randint(100, 500)

# Check for faults
def detect_faults(vibration, strain):
    vibration_status = "OK"
    strain_status = "OK"

    if vibration > VIBRATION_THRESHOLD:
        vibration_status = "FAULT"

    if strain > STRAIN_THRESHOLD:
        strain_status = "FAULT"

    return vibration_status, strain_status

# Main monitoring loop
def monitor_structure():
    print("🏗️ Structural Health Monitoring System Started\n")
    print("{:<20} {:<15} {:<15} {:<10} {:<10}".format("Time", "Vibration (mm/s)", "Strain (µε)", "Vib-Stat", "Str-Stat"))
    print("-" * 70)

    try:
        while True:
            vibration = read_vibration_sensor()
            strain = read_strain_sensor()
            vib_status, strain_status = detect_faults(vibration, strain)
            print("{:<20} {:<15} {:<15} {:<10} {:<10}".format(
                time.strftime("%H:%M:%S"),
                vibration,
                strain,
                vib_status,
                strain_status
            ))
            time.sleep(2)  # 2 second delay for next reading
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

# Run the program
if __name__ == "__main__":
    monitor_structure()
