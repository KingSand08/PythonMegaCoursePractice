import cv2, time, pandas
from datetime import datetime

video = cv2.VideoCapture(0)

# There must be a delay to properly capture the first frame, if immediate the first frame will be blank
time.sleep(2)

# Instantiate needed vars
first_frame = None
key = None
statusList = [None, None]
timesActive = []
data =[]

# If q or escape key are pressed
while True:
    check, frame = video.read()
    if not check:
        print("Failed to capture image")
        continue
    
    # Motion status
    status = 0
    
    # Generates a copy of the frame in greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Blur greysale image to remove noise and increase accuracy in calculation 
    gray = cv2.GaussianBlur(gray, (21, 21), 0) # GaussianBlur(frame to be blurred, (width, hieght) -> both width and 
                                                      # height of gaussian blur, so parameters of blurriess ), then last param
                                                      # is standard deviation (0 is commonly used).
    # Capture first frame if on the first itteration
    if first_frame is None:
        first_frame = gray
        continue
    
    # Create delta and thresh frames for proper motion detection
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # This is a tuple, but we only want to access the 
                                                                             # second index as that is where the actual frame is returned from the threshold method
    
    # This smoothes over the threshhold frame
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) # If itterations is higher it will be smoother 
    
    # Get contours of distinct objects in the video frame (outlines) of the threshold frame
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Trim number of contour to be only bigger than 1000 pixels
    for contour in cnts:
        if (cv2.contourArea(contour) < 10000): # If countour is bigger than 1000 px
            continue
        status = 1 # Motion status triggered
        (x, y, w, h) = cv2.boundingRect(contour)  # Then create countor rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    # Update status list with current status
    statusList.append(status)
    
    # Ensure status list only hols current and previous values (to secure memory for long program runtimes), 
    # will ONLY effect the itteration after the code below is triggered
    statusList = statusList[-2:]
    
    # Updates the server list
    if statusList[-1] == 1 and statusList[-2] == 0:
        timesActive.append(datetime.now())
    if statusList[-1] == 0 and statusList[-2] == 1:
        timesActive.append(datetime.now())
    
    # cv2.imshow("First Frame", first_frame)
    # cv2.imshow("Gray Frame", gray)
    # cv2.imshow("Delta Frame", delta_frame)
    # cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Colored Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q') or key == ord('\x1b'):
        if(status == 1):
            timesActive.append(datetime.now())
        break
print(statusList)
print()
print(timesActive)
video.release() # This will stop using the camera
cv2.destroyAllWindows()

for i in range(0, len(timesActive), 2):
    # df = df.append({"Start":timesActive[i], "End":timesActive[i+1]}, ignore_index=True)
    data.append({"Start": timesActive[i], "End": timesActive[i+1]})

df = pandas.DataFrame(data)
df.to_csv("./App2_WebcamMotionDetectorProgram/motion_capture_times.csv", index=False)