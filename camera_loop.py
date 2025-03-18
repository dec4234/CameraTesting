from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()

try:
    while True:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"/home/pi/image_{timestamp}.jpg"
        picam2.capture_file(filename)
        print(f"Captured: {filename}")
        time.sleep(0.5)  # 2 FPS

except KeyboardInterrupt:
    print("\nStopping camera.")

finally:
    picam2.stop()
    picam2.close()
