import cv2, time
import numpy

videoCapture = cv2.VideoCapture(0) # If this were not a caputre, you would need to define the path/name of the file, as well the coloring
check, noLightCheck = videoCapture.read() # assuming capture can't start this fast (nearly always)
time.sleep(0.2)
key = None
framesGenerated = 0
framesWithNoLight = 0
# print(noLightCheck)
# If q or escape key are pressed
while key != ord('q') and key != ord('\x1b'):
    # Check for preforming operations on captured images (from the video feed)
    # Frame for capturing and displaying captured images (from the video feed)
    check, frame = videoCapture.read()
    
    framesGenerated += 1 # Take in how many frames created
    # Can take in how many frames there are when its practically black
    if numpy.mean(frame) < 6:
        framesWithNoLight += 1
        
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

videoCapture.release() # This will stop using the camera
cv2.destroyAllWindows()