# this version runs through a folder in multiple passes, using multiple ranges of circle radii
# it's an attempt to avoid all the false positives that seem to come out of a wide range of circle radii (low min and high max) in the hough.circles radius parameters
# this version also includes one iteration that only returns images with a circle count greater than 1 (that range of radii should include compass rose radius)

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
imgnames = sorted(glob.glob("/Users/jtollefs/Documents/SOCBROWNPHD/FMGP/detect_coal_gas/input/*.jpg"))

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
# compass is between 87 and 90px

# ITERATION 1 (for range smalller than compass circle)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                                param1=20,param2=50,minRadius=30,maxRadius=60)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), 2)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# for successive iterations with different radii, change "_out" to "_out2", "_out3", etc
        imgname1 = "_out1".join(os.path.splitext(imgname))
        imgname1 = change_to_output(imgname1)
        cv2.imwrite(imgname1, output)


# ITERATION 2 (**for range that includes compass circle)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                                param1=20,param2=100,minRadius=61,maxRadius=120)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

# define number of circles
        no_of_circles = len(circles)
# define bottom threshold for how many circles to find
        if (no_of_circles>1):

            for (x, y, r) in circles:
                # draw the outer circle
                cv2.circle(output,(x, y), r, (0, 255, 0), 2)
                # draw the radius
                cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
                # draw the center of the circle
                cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

            imgname2 = "_out2".join(os.path.splitext(imgname))
            imgname2 = change_to_output(imgname2)
            cv2.imwrite(imgname2, output)

# ITERATION 3 (**for range larger than compass circle)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,
                                param1=20,param2=50,minRadius=121,maxRadius=220)
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
