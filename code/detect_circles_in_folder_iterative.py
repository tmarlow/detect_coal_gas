# import the necessary packages
import numpy as np
import argparse
import glob
import os,sys
import cv2

def change_to_output(path):
    return os.path.join(os.path.split(os.path.dirname(path))[0], 'output', os.path.basename(path))

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

## Get all the png image in the PATH_TO_IMAGES. Input whatever folder you're actually using.
imgnames = sorted(glob.glob("/Users/jtollefs/Documents/SOCBROWNPHD/FMGP/SANBORNMAPDOWNLOADS/detect_coal_gas-master-test/input/*.jpeg"))

# load the image, clone it for output, and then convert it to grayscale
# load list of images, code from https://stackoverflow.com/questions/46505052/processing-multiple-images-in-sequence-in-opencv-python
for imgname in imgnames:
    image = cv2.imread(imgname)
    output = image.copy()
    blur = cv2.GaussianBlur(image,(3,3),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

#   imgname2 = "_gray".join(os.path.splitext(imgname))  [[removed]]
#   cv2.imwrite(imgname2, gray)  [[removed]]

# detect circles in the image
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50)#, #maxRadius = 200)
# 50 = min distance between centers of HoughCircles
# too wide a radius returns false positives; try iterations of min50max100; min101max150; etc

# ITERATION 1
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                                param1=20,param2=50,minRadius=45,maxRadius=99)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), 2)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# for successive iterations with different radii, change "_out" to "_out2", "_out3", etc
        imgname1 = "_out1".join(os.path.splitext(imgname))
        imgname1 = change_to_output(imgname1)
        cv2.imwrite(imgname1, output)


# ITERATION 2
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                                param1=20,param2=100,minRadius=100,maxRadius=149)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), 2)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# for successive iterations with different radii, change "_out" to "_out2", "_out3", etc
        imgname2 = "_out2".join(os.path.splitext(imgname))
        imgname2 = change_to_output(imgname2)
        cv2.imwrite(imgname2, output)

# ITERATION 3
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                                param1=20,param2=50,minRadius=150,maxRadius=200)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), 2)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# for successive iterations with different radii, change "_out" to "_out2", "_out3", etc
        imgname3 = "_out3".join(os.path.splitext(imgname))
        imgname3 = change_to_output(imgname3)
        cv2.imwrite(imgname3, output)
