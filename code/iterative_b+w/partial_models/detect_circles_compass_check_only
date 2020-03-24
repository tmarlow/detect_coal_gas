# RUN AFTER PRIMARY SCRIPT
# this is a spot check, using a lower blur value to increase accuracy for small circles
# it finds images with 2+ circles the size of the compass rose
# it then exports those images, with an argument so that it doesn't overwrite images already found from the primary algorithm

# this is only to find those images which were missed in the original pass, because the circles were too small (and the blur was too great)

# import the necessary packages
import numpy as np
import argparse
import glob
import os,sys
import cv2

def change_to_output(path):
    return os.path.join(os.path.split(os.path.dirname(path))[0], 'output', os.path.basename(path))

# parameters for hough_circles, GaussianBlur, and circle drawn by cv2 are defined here
p1c_check = 20
p2c_check = 24
blur1c_check = 3
blur2c_check = 3

# circle that is drawn for you to see
draw_stroke = 10

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

## Get all the png image in the PATH_TO_IMAGES. Input whatever folder you're actually using.
imgnames = sorted(glob.glob("/Users/jtollefs/Documents/SOCBROWNPHD/FMGP/detect_coal_gas/input/*.jpg"))

# load the image, clone it for output, and then convert it to grayscale
# load list of images, code from https://stackoverflow.com/questions/46505052/processing-multiple-images-in-sequence-in-opencv-python
for imgname in imgnames:
    imageC_check = cv2.imread(imgname)
    outputC_check = imageC_check.copy()
    blurC_check = cv2.GaussianBlur(imageC_check,(blur1c_check,blur2c_check),0)
    grayC_check = cv2.cvtColor(blurC_check, cv2.COLOR_BGR2GRAY)


#   imgname2 = "_gray".join(os.path.splitext(imgname))  [[removed]]
#   cv2.imwrite(imgname2, gray)  [[removed]]

# detect circles in the image
# 2nd number after HOUGH_GRADIENT = min distance between centers of HoughCircles
# too wide a radius returns false positives; that's why it's split into multiple segments
# compass is between 87 and 90px


# ITERATION C_check - this includes compass rose
    circlesC_check = cv2.HoughCircles(grayC_check,cv2.HOUGH_GRADIENT,1,17,
                                param1=p1c_check,param2=p2c_check,minRadius=28,maxRadius=35)
    if circlesC_check is not None:
        circlesC_check = np.round(circlesC_check[0, :]).astype("int")

        for (x, y, r) in circlesC_check:
            # draw the outer circle
            cv2.circle(outputC_check,(x, y), r, (0, 255, 0), draw_stroke)
            # draw the radius
            cv2.putText(outputC_check,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(outputC_check,(x, y), 2, (0, 0, 255), 3)

# count circles

    if circlesC_check is not None:
        no_of_circlesC_check = int(len(circlesC_check))
    else: no_of_circlesC_check = int(0)

# if there are more than one noncompass circles
    if (no_of_circlesC_check>1):
        imgnameC_check = "_out".join(os.path.splitext(imgname))
        imgnameC_check = change_to_output(imgnameC_check)

# so that it doesn't overwrite images from primary script
        if not os.path.exists(imgnameC_check):
            cv2.imwrite(imgnameC_check, outputC_check)
