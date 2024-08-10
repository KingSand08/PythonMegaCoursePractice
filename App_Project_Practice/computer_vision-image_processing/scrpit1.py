import cv2, glob

PROJDIR_ASSETS = "./App_Project_Practice/computer_vision-image_processing/assets/"
RZ_IMGPATH = PROJDIR_ASSETS + "resized_imgs/"
IMPORT_IMGPATH = PROJDIR_ASSETS + "sample_images/"

def batchImgShow(PATH = './', coloring = 1, sequence = True):
     images = glob.glob(PATH + "*.jpg")
     if(sequence):
          for image in images:
               imageName = image.replace(PATH, '')
               img = cv2.imread(image, coloring)
               cv2.imshow(imageName, img)
          cv2.waitKey(0) # 0 = on user interaction, n > 0 = on timer
          cv2.destroyAllWindows()
     else:
          for image in images:
               imageName = image.replace(PATH, '')
               img = cv2.imread(image, coloring)
               cv2.imshow(imageName, img)
               cv2.waitKey(0) # 0 = on user interaction, n > 0 = on timer
               cv2.destroyAllWindows()
     
def batchImgResizeAndSave(DESTPATH, PATH = './', coloring = 1, show = True, amnt = (100, 100)):
     images = glob.glob(PATH + "*.jpg")
     for image in images:
          imageName = image.replace(PATH, '')
          img = cv2.imread(image, coloring)
          resized_img = cv2.resize(img, amnt)
          if(show):
               cv2.imshow(imageName, resized_img)
               cv2.waitKey(500)
               cv2.destroyAllWindows()
          cv2.imwrite(DESTPATH + imageName + "_resized_" + str(amnt) + ".jpg", resized_img)
          
def simpleTutorial():
     img = cv2.imread(PROJDIR_ASSETS + "simple_tutorial/galaxy.jpg", 0) # 1 = colored, 0 = greyscaled (img has 1 band), -1 color image but with alpha channel (trasparent cababilities)
     resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
     img = cv2.imread(PROJDIR_ASSETS + "simple_tutorial/galaxy.jpg", 0) # 1 = colored, 0 = greyscaled (img has 1 band), -1 color image but with alpha channel (trasparent cababilities)
     resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
     cv2.imshow("Galaxy", img)
     cv2.imshow("Galaxy Resized", resized_img)

     cv2.imwrite(PROJDIR_ASSETS + "simple_tutorial/galaxy_resized.jpg", resized_img)

     cv2.waitKey(0) # 0 = on user interaction, n > 0 = on timer
     cv2.destroyAllWindows()
     
simpleTutorial()
batchImgShow(IMPORT_IMGPATH)
batchImgResizeAndSave(RZ_IMGPATH, IMPORT_IMGPATH, show=False)