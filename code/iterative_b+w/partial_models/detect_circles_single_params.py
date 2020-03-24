# this version runs through a folder in multiple passes, using multiple ranges of circle radii
# it's an attempt to avoid all the false positives that seem to come out of a wide range of circle radii (low min and high max) in the hough.circles radius parameters
# this version also includes one iteration that only returns images with a circle count greater than 1 (that range of radii should include compass rose radius)
# it only saves an output images after it's run through each iteration

# import the necessary packages
import numpy as np
import argparse
import glob
import os,sys
import cv2

def change_to_output(path):
    return os.path.join(os.path.split(os.path.dirname(path))[0], 'output', os.path.basename(path))

# parameters for hough_circles, GaussianBlur, and circle drawn by cv2 are defined here
p1 = 20
p2 = 48
blur1 = 31
blur2 = 31
# for circles including compass rose
p1c = 20
p2c = 38
# circle that is drawn for you to see
draw_stroke = 20

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
    blur = cv2.GaussianBlur(image,(blur1,blur2),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

#   imgname2 = "_gray".join(os.path.splitext(imgname))  [[removed]]
#   cv2.imwrite(imgname2, gray)  [[removed]]

# detect circles in the image
# 2nd number after HOUGH_GRADIENT = min distance between centers of HoughCircles
# too wide a radius returns false positives; that's why it's split into multiple segments
# compass is between 87 and 90px



# ITERATION 2
    circles2 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,26,
                                param1=p1,param2=p2,minRadius=36,maxRadius=60)
    if circles2 is not None:
        circles2 = np.round(circles2[0, :]).astype("int")

        for (x, y, r) in circles2:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 3
    circles3 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,51,
                                param1=p1,param2=p2,minRadius=61,maxRadius=90)
    if circles3 is not None:
        circles3 = np.round(circles3[0, :]).astype("int")

        for (x, y, r) in circles3:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 3a
    circles3a = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,81,
                                param1=p1,param2=p2,minRadius=91,maxRadius=120)
    if circles3a is not None:
        circles3a = np.round(circles3a[0, :]).astype("int")

        for (x, y, r) in circles3a:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 4
    circles4 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,111,
                                param1=p1,param2=p2,minRadius=121,maxRadius=150)
    if circles4 is not None:
        circles4 = np.round(circles4[0, :]).astype("int")

        for (x, y, r) in circles4:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 5
    circles5 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,141,
                                param1=p1,param2=p2,minRadius=151,maxRadius=180)
    if circles5 is not None:
        circles5 = np.round(circles5[0, :]).astype("int")

        for (x, y, r) in circles5:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 6
    circles6 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,170,
                                param1=p1,param2=p2,minRadius=181,maxRadius=210)
    if circles6 is not None:
        circles6 = np.round(circles6[0, :]).astype("int")

        for (x, y, r) in circles6:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 1
    circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,201,
                                param1=p1,param2=p2,minRadius=211,maxRadius=241)
    if circles1 is not None:
        circles1 = np.round(circles1[0, :]).astype("int")

        for (x, y, r) in circles1:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# define bottom threshold for how many circles to find
    if circles1 is not None:
        no_of_circles1 = int(len(circles1))
    else: no_of_circles1 = int(0)
    if circles2 is not None:
        no_of_circles2 = int(len(circles2))
    else: no_of_circles2 = int(0)
    if circles3 is not None:
        no_of_circles3 = int(len(circles3))
    else: no_of_circles3 = int(0)
    if circles3a is not None:
        no_of_circles3a = int(len(circles3a))
    else: no_of_circles3a = int(0)
    if circles4 is not None:
        no_of_circles4 = int(len(circles4))
    else: no_of_circles4 = int(0)
    if circles5 is not None:
        no_of_circles5 = int(len(circles5))
    else: no_of_circles5 = int(0)
    if circles6 is not None:
        no_of_circles6 = int(len(circles6))
    else: no_of_circles6 = int(0)

    if circlesC is not None:
        no_of_circlesC = int(len(circlesC))
    else: no_of_circlesC = int(0)

# add all circles not counting compass
    total_noncompass_circles = no_of_circles1 + no_of_circles2 + no_of_circles3 + no_of_circles3a + no_of_circles4 + no_of_circles5 + no_of_circles6

# if there is a noncompass circle, or if there are two circles of compass size
    if (total_noncompass_circles>0) or (no_of_circlesC>1):
        imgname1 = "_out".join(os.path.splitext(imgname))
        imgname1 = change_to_output(imgname1)
        cv2.imwrite(imgname1, output)
