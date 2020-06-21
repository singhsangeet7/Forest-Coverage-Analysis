import cv2 as cv
import json 

import numpy as np
def findAcc(img, nam):
	low_green = np.array([0, 80, 0])
	high_green = np.array([150, 255, 100])
	hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

	mask = cv.inRange(hsv_img, low_green, high_green)

	res = cv.bitwise_and(img, img, mask = mask)

	cv.imshow(str(nam+1) + " Mask", mask)
	cv.imwrite(str(nam+1) + ".png", mask)
	cv.waitKey(0)
   
	bw = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
	bw = cv.GaussianBlur(bw, (3, 3), 0)

	a, thresh = cv.threshold(bw, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
	kernel = np.ones((5,5), np.uint8)
	
	canny = cv.Canny(bw, a*0.5, a)

	cv.imshow(str(nam+2) + " Canny", canny)
	cv.imwrite(str(nam+2) + ".png", canny)
	cv.waitKey(0)
    

	canny = cv.dilate(canny, kernel, iterations=1)
	# cv.imshow("ss", canny)
	
	area, tot = cv.countNonZero(canny), img.shape[0] * img.shape[1]
	#cv.putText(img, 'Forest Cover ' + str(area/tot * 100) , (56, 80), cv.FONT_HERSHEY_COMPLEX, 0.7, (2,255,2),2)
	cv.imshow(str(nam+3), img)
	cv.imwrite(str(nam+3)+'.png', img)
	cv.waitKey(0)

	return area/tot
image = cv.imread(str(102)+".png")
findAcc(image, (69)) 
cv.waitKey(0)
cv.destroyAllWindows()
'''
l=[]
for i in range(1,3):
    #cv.imshow(str(i)+".png")
    
    image = cv.imread(str(i+100)+".png") 
  
# Window name in which image is displayed 
    window_name = 'image'
    l.append(findAcc(image, 8191099+i)*100)
    cv.waitKey(0)
    cv.destroyAllWindows()
# Using cv2.imshow() method  
# Displaying the image  
    #cv.imshow(str(nam+i), image)
sp=json.dumps(l)
#print(sp)

with open("dataset.txt","w") as j:
    j.write(sp)

for i in l:
    print(i)
'''
'''
with open('abc.txt','r') as f:
    for line in f:
        print(line)
        img = cv.imread('anand vihar.png')
        cv.imshow('image555', img)
        print(img)
        findAcc(img, 90)
        cv.waitKey(0)
        cv.destroyAllWindows()
        #print(line,end='')
        

'''

