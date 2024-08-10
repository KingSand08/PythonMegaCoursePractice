import cv2

PROJDIR = "./App_Project_Practice/computer_vision-image_processing/"
CASCASDE_FILEPATH = PROJDIR + "data/haarcascade_files/"
CASCASDE_IMGPATH = PROJDIR + "assets/haarcascade_images/"
PHOTO_TO_USE = "photo.jpg"
RESIZE_BOOL = True

# Read cacade file
faceCascade = cv2.CascadeClassifier(CASCASDE_FILEPATH + "haarcascade_frontalface_default.xml")

# CREATE USABLE IMAGE OBJECT
img = cv2.imread(CASCASDE_IMGPATH + PHOTO_TO_USE)

# Use grey image of img container to greatly increase face search quality
greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # RGB img -> Greyscale img


# START CASCADE FUNCTIONS
# This will attempt to find the upper left corner of a human face and then attempt to discover the rest of the face
# Returns an array that cotains 4 numbers:
#       [ x -> (row number of the top left of face), y -> (column number of the top left of face)
#           , w -> (width of registered face), h -> (hieght of registered face) ]
faces = faceCascade.detectMultiScale(greyImg,
    scaleFactor = 1.1, # What this does is determine how much to shrink the image  while the function is searching 
                        # for a face. The smaller, the more accurate, this is because larger scale factors will
                        # expand the image more and cover more area but with less detail (so less accurate).
                        # Recommended to be at 1.05, but if inaccurate, 1.1 is okay too (such as with news.jpg ex).
    minNeighbors = 5    # This determines how many members the function should search around a given searchable
                        # chunk. The default is recommended to be 5 typically.
    )

for x, y, w, h in faces:
    # Will use cv2 to draw a visable representation of the found face array as a rectangle in a new image
    # (x , y)               first point of the top left side of the face
    # (x + w, y + h)        second point of bottom right registered area
    # (blue, green, red)    color of the rectangle (in BGR format)
    # int width             stroke size of the line
    foundFaceImg = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3) 

# Resize image to display for easier reability
resized_img = cv2.resize(foundFaceImg, (int(img.shape[1]/1.5), int(img.shape[0]/1.5)))

# Resize logic
imgToUse = (resized_img if RESIZE_BOOL else foundFaceImg)

# Now displaying the image
cv2.imshow("Found Faces", imgToUse)
cv2.waitKey(0)
cv2.destroyAllWindows()