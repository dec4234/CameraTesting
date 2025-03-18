from picamera import PiCamera
from time import sleep

# Initialize camera
camera = PiCamera()
camera.resolution = (3280, 2464)  # Max resolution for Pi Camera v2

# Capture images in a loop
try:
    while True:
        camera.capture('/home/pi/image.jpg')
        print("Image captured!")
        sleep(0.5)  # 2 FPS (1 frame per 0.5s)

except KeyboardInterrupt:
    print("\nStopping camera.")

finally:
    camera.close()
