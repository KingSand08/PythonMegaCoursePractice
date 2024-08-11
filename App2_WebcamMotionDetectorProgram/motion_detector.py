import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(2)
# Instantiate needed vars
first_frame = None
key = None

# If q or escape key are pressed
while key != ord('q') and key != ord('\x1b'):
    check, frame = video.read()
    if not check:
        print("Failed to capture image")
        continue
    
    # Generates a copy of the frame in greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Blur greysale image to remove noise and increase accuracy in calculation 
    gray = cv2.GaussianBlur(gray, (21, 21), 0) # GaussianBlur(frame to be blurred, (width, hieght) -> both width and 
                                                      # height of gaussian blur, so parameters of blurriess ), then last param
                                                      # is standard deviation (0 is commonly used).
    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # This is a tuple, but we only want to access the 
                                                                             # second index as that is where the actual frame is returned from the threshold method
    
    # This smoothes over the threshhold frame
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) # If itterations is higher it will be smoother 
    
    # Get contours of distinct objects in the video frame (outlines) of the threshold frame
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Trim number of contour to be only bigger than 1000 pixels
    for contour in cnts:
        if (cv2.contourArea(contour) < 1000): # If countour is bigger than 1000 px
            continue
        (x, y, w, h) = cv2.boundingRect(contour)  # Then create countor rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    cv2.imshow("First Frame", first_frame)
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Colored Frame", frame)

    print("Delta frame min:", delta_frame.min())
    print("Delta frame max:", delta_frame.max())
    key = cv2.waitKey(1)

video.release() # This will stop using the camera
cv2.destroyAllWindows()