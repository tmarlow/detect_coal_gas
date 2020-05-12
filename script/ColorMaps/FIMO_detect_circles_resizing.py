# runs through color maps in 2 iterations (to avoid finding false pos circles of r=0, at (x,y) (0,0))
# used on images sized 1400*2008 (2.8 megapx), downloaded from Sanborn indices
# see resize function below - this script resizes images to fit the target resolution listed above
# this is .28 of the BW-sized maps. Multiply BW map radii bins by .28 to get the bins used here
# note that some maps include compass rose as a circle; some do not. Adjust iterations accordingly.

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
# need to test params

# params for circles_small
## Radii
rmin_s = 15
rmax_s = 55
# min distance between circles
min_dist_s = 15
# params
p1_s = 20
p2_s = 65
# blur
b1_s = 7
b2_s = 7

# params for circles_large
## Radii
rmin_l = 55
rmax_l = 100
# min distance between circles
min_dist_l = 55
# params
p1_l = 20
p2_l = 65
# blur
b1_l = 7
b2_l = 7

# thickness for circle that is drawn for you to see
draw_stroke = 8

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

## Get all the png image in the PATH_TO_IMAGES. Input whatever folder you're actually using.
imgnames = sorted(glob.glob("../input/*.jpg"))

# load the image, clone it for output, and then convert it to grayscale
# load list of images, code from https://stackoverflow.com/questions/46505052/processing-multiple-images-in-sequence-in-opencv-python
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


    blur_s = cv2.GaussianBlur(output,(b1_s,b2_s),0)
    blur_l = cv2.GaussianBlur(output,(b1_l,b2_l),0)
    gray_s = cv2.cvtColor(blur_s, cv2.COLOR_BGR2GRAY)
    gray_l = cv2.cvtColor(blur_l, cv2.COLOR_BGR2GRAY)


#   imgname2 = "_gray".join(os.path.splitext(imgname))  [[removed]]
#   cv2.imwrite(imgname2, gray)  [[removed]]

# detect circles in the image
# 2nd number after HOUGH_GRADIENT = min distance between centers of HoughCircles
# too wide a radius returns false positives; that's why it's split into multiple segments
# compass is between 87 and 90px


# Small iteration
    circles = cv2.HoughCircles(gray_s,cv2.HOUGH_GRADIENT,1,min_dist_s,
                                param1=p1_s,param2=p2_s,minRadius=rmin_s,maxRadius=rmax_s)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), draw_stroke)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)


# Large iteration
    circles1 = cv2.HoughCircles(gray_l,cv2.HOUGH_GRADIENT,1,min_dist_l,
                                param1=p1_l,param2=p2_l,minRadius=rmin_l,maxRadius=rmax_l)
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
    if circles is not None:
        no_of_circles = int(len(circles))
    else: no_of_circles = int(0)

    if circles1 is not None:
        no_of_circles1 = int(len(circles1))
    else: no_of_circles1 = int(0)

# if there is a circle, print output
    if (no_of_circles>0) or (no_of_circles1>0):
        imgname1 = "_out".join(os.path.splitext(imgname))
        imgname1 = change_to_output(imgname1)
        cv2.imwrite(imgname1, output)
