#### FOLDER STRUCTURE###
# level 1: input folder, this script
# input folder: a collection of folders with images (images must be in folders; no sub-folders)
# place output folder within input folder


# import the necessary packages
import numpy as np
import argparse
import glob
import os,sys
import cv2
import pandas as pd

def change_to_output(path):
    return os.path.join(os.path.split(os.path.dirname(path))[0], 'output', os.path.basename(path))

# parameters for circle bin radii, hough_circles, GaussianBlur, and circle drawn by cv2 are defined here
# need to test params


# params for circles_compass
## Radii
rmin_c = 25
rmax_c = 35
# min distance between circles
min_dist_c = 15
# params
p1_c = 20
p2_c = 50
# blur
b1_c = 3
b2_c = 3


# thickness for circle that is drawn for you to see
draw_stroke = 8
text_size = 0.5
text_stroke = 1

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

## Get all the png image in the PATH_TO_IMAGES. Input whatever folder you're actually using.
## including /saveTo**/ also searches one level of sub-directories below "input" that start with saveTo
imgnames = sorted(glob.glob("test/test/*.jpg"))


# load the image, clone it for output
for imgname in imgnames:
    image = cv2.imread(imgname)
    copy = image.copy()



######## resize to fit params ###################################################

    height, width = copy.shape[:2]
    target_height = 2008
    target_width = 1390

    # enlarge image by factor
    if (target_height * target_width) < (height * width):
        # get scaling factor
        scaling_factor = (target_height + target_width) / (float(height) + float(width))

        # resize image
        output = cv2.resize(copy, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # enlarge image by a calculated factor so it's the same resolution as the target
    if (target_height * target_width) > (height * width):
        # get scaling factor
        scaling_factor = (target_height + target_width) / (float(height) + float(width))

        # resize image
        output = cv2.resize(copy, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_LINEAR)

########## end of resize to fit params ########################################

    blur_c = cv2.GaussianBlur(output,(b1_c,b2_c),0)
    gray_c = cv2.cvtColor(blur_c, cv2.COLOR_BGR2GRAY)



# Compass? iteration
    circles_c = cv2.HoughCircles(gray_c,cv2.HOUGH_GRADIENT,1,min_dist_c,
                                param1=p1_c,param2=p2_c,minRadius=rmin_c,maxRadius=rmax_c)
    if circles_c is not None:
        circles_c = np.round(circles_c[0, :]).astype("int")

        for (x, y, r) in circles_c:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, text_size, (255,0,0), text_stroke, cv2.LINE_AA)
            # draw the center of the circle
        #    cv2.circle(output,(x, y), 2, (0, 0, 255), 3)


# define bottom threshold for how many circles to find
    if circles_c is not None:
        no_of_circles_c = int(len(circles_c))
    else: no_of_circles_c = int(0)


# if there is a circle, print output
    if (no_of_circles_c>0):
        imgname1 = "_out".join(os.path.splitext(imgname))
        imgname1 = change_to_output(imgname1)

# now, look at dataframe to see if there are any folders with a lot of positives.
# do so by getting the mean of "circ", grouped by "set"
# This incidates they have a compass visible, and you need to run the compass script instead.
