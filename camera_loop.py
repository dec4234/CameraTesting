import time
from picamera2 import Picamera2


def capture_images():
    # Initialize Picamera2
    picam2 = Picamera2()

    # Configure the camera for max resolution
    camera_config = picam2.create_still_configuration(main={"size": picam2.sensor_resolution})
    picam2.configure(camera_config)

    picam2.start()
    print("Camera started. Capturing images at 1-second intervals...")

    try:
        image_count = 0
        while True:
            filename = f"image_{image_count:04d}.jpg"  # Save images with sequential names
            picam2.capture_file(filename)
            print(f"Captured: {filename}")
            image_count += 1
            time.sleep(1)  # Wait for 1 second between captures
    except KeyboardInterrupt:
        print("\nStopping image capture...")
    finally:
        picam2.stop()
        print("Camera stopped.")


if __name__ == "__main__":
    capture_images()
