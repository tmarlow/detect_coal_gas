# This version runs through a images in multiple passes, using different radii bins in each pass.
# to be used on sanborn digital edition  maps, sized roughly 2970x3388px (10megapx), generated from pdf files using pdf2img with 300 as quality setting
# radius including compass tested to ensure it captures (nearly) every compass circle

# import the necessary packages
import numpy as np
import argparse
import glob
import os,sys
import cv2

def change_to_output(path):
    return os.path.join(os.path.split(os.path.dirname(path))[0], 'output', os.path.basename(path))

# parameters for circle bin radii, hough_circles, GaussianBlur, and circle drawn by cv2 are defined here



# Medium circles
## Radii
rmin_m1 = 61
rmax_m1 = 90
rmin_m2 = 91
rmax_m2 = 120
## params
p1_m = 20
p2_m = 42
## blur
b1_m = 15
b2_m = 15

# Large circles
## Radii
rmin_l1 = 121
rmax_l1 = 150
rmin_l2 = 151
rmax_l2 = 180
rmin_l3 = 181
rmax_l3 = 210
rmin_l4 = 211
rmax_l4 = 241
## Params
p1_l = 20
p2_l = 42
## blur
b1_l = 31
b2_l = 31


# thickness for circle that is drawn for you to see
draw_stroke = 15

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

    blurM = cv2.GaussianBlur(image,(b1_m,b2_m),0)
    blurL = cv2.GaussianBlur(image,(b1_l,b2_l),0)

    grayM = cv2.cvtColor(blurM, cv2.COLOR_BGR2GRAY)
    grayL = cv2.cvtColor(blurL, cv2.COLOR_BGR2GRAY)

#   imgname2 = "_gray".join(os.path.splitext(imgname))  [[removed]]
#   cv2.imwrite(imgname2, gray)  [[removed]]

# detect circles in the image
# 2nd number after HOUGH_GRADIENT = min distance between centers of HoughCircles
# too wide a radius returns false positives; that's why it's split into multiple segments
# compass is between 87 and 90px




# ITERATION 3
    circles3 = cv2.HoughCircles(grayM,cv2.HOUGH_GRADIENT,1,51,
                                param1=p1_m,param2=p2_m,minRadius=rmin_m1,maxRadius=rmin_m2)
    if circles3 is not None:
        circles3 = np.round(circles3[0, :]).astype("int")

        for (x, y, r) in circles3:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 3a
    circles3a = cv2.HoughCircles(grayM,cv2.HOUGH_GRADIENT,1,81,
                                param1=p1_m,param2=p2_m,minRadius=rmin_m1,maxRadius=rmax_m1)
    if circles3a is not None:
        circles3a = np.round(circles3a[0, :]).astype("int")

        for (x, y, r) in circles3a:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 4
    circles4 = cv2.HoughCircles(grayL,cv2.HOUGH_GRADIENT,1,111,
                                param1=p1_l,param2=p2_l,minRadius=rmin_l1,maxRadius=rmax_l1)
    if circles4 is not None:
        circles4 = np.round(circles4[0, :]).astype("int")

        for (x, y, r) in circles4:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 5
    circles5 = cv2.HoughCircles(grayL,cv2.HOUGH_GRADIENT,1,141,
                                param1=p1_l,param2=p2_l,minRadius=rmin_l2,maxRadius=rmax_l2)
    if circles5 is not None:
        circles5 = np.round(circles5[0, :]).astype("int")

        for (x, y, r) in circles5:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 6
    circles6 = cv2.HoughCircles(grayL,cv2.HOUGH_GRADIENT,1,170,
                                param1=p1_l,param2=p2_l,minRadius=rmin_l3,maxRadius=rmax_l3)
    if circles6 is not None:
        circles6 = np.round(circles6[0, :]).astype("int")

        for (x, y, r) in circles6:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION 1
    circles1 = cv2.HoughCircles(grayL,cv2.HOUGH_GRADIENT,1,201,
                                param1=p1_l,param2=p2_l,minRadius=rmin_l4,maxRadius=rmax_l4)
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


# add all circles not counting compass
    total_noncompass_circles = no_of_circles1 + no_of_circles3 + no_of_circles3a + no_of_circles4 + no_of_circles5 + no_of_circles6

# if there is a noncompass circle, or if there are two circles of compass size
    if (total_noncompass_circles>0):
        imgname1 = "_out".join(os.path.splitext(imgname))
        imgname1 = change_to_output(imgname1)
        cv2.imwrite(imgname1, output)
