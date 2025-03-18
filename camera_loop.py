from picamera2 import Picamera2
import time
import os

# Create a directory to store images if it doesn't exist
output_dir = "captured_images"
os.makedirs(output_dir, exist_ok=True)

# Initialize the camera
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# Capture images in a loop
image_interval = 5  # Seconds between captures
image_count = 0

try:
    print("Starting camera loop. Press Ctrl+C to stop.")
    while True:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        image_path = os.path.join(output_dir, f"image_{timestamp}.jpg")
        picam2.capture_file(image_path)
        print(f"Captured: {image_path}")
        image_count += 1
        time.sleep(image_interval)

except KeyboardInterrupt:
    print("\nCamera loop stopped by user.")

finally:
    picam2.close()
