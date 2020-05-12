# import the necessary packages
import numpy as np
import argparse
import cv2


# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())


# load the image, clone it for output, and then convert it to grayscale
image = cv2.imread("../Gasification/1920-sanborn_screenshot.tiff")
output = image.copy()
blur = cv2.GaussianBlur(image,(3,3),0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray_img.png', gray)

# detect circles in the image
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 150)#, #maxRadius = 200)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                            param1=20,param2=50,minRadius=20,maxRadius=60)



circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)


cv2.imwrite("output.png", output)
