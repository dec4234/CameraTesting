from picamera2 import Picamera2
import cv2

# Initialize the camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())  # Use preview mode for video
picam2.start()

try:
    while True:
        frame = picam2.capture_array()
        cv2.imshow("Camera Feed", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nStopping camera.")

finally:
    cv2.destroyAllWindows()
    picam2.stop()
    picam2.close()
