import cv2 as cv
for i in range(1,3):
    #cv.imshow(str(i)+".png")
    nam=1000
    image = cv.imread(str(i)+".png") 
  
# Window name in which image is displayed 
    window_name = 'image'
  
# Using cv2.imshow() method  
# Displaying the image  
    cv.imshow(str(nam+i), image)