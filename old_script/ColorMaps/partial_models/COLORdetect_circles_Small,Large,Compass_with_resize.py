# set radius params for color maps
# this version runs through a folder in multiple passes, using multiple ranges of circle radii
# it's an attempt to avoid all the false positives that seem to come out of a wide range of circle radii (low min and high max) in the hough.circles radius parameters

# import the necessary packages
import numpy as np
import argparse
import glob
import os,sys
import cv2

def change_to_output(path):
    return os.path.join(os.path.split(os.path.dirname(path))[0], 'output', os.path.basename(path))



# for circles including compass rose
## Radii
rmin_c = 28
rmax_c = 37
# params
p1_c = 20
p2_c = 50
# blur
b1_c = 3
b2_c = 3

# Small circles
## Radii
rmin_s = 38
rmax_s = 60
# params
p1_s = 20
p2_s = 65
# blur
b1_s = 7
b2_s = 7

# Large circles
## Radii
rmin_l = 60
rmax_l = 100
# params
p1_l = 20
p2_l = 65
# blur
b1_l = 7
b2_l = 7

# thickness for circle that is drawn for you to see
draw_stroke = 15





# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

## Get all the png image in the PATH_TO_IMAGES. Input whatever folder you're actually using.
imgnames = sorted(glob.glob("..input/*.jpg"))

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






    blurC = cv2.GaussianBlur(output,(b1_c,b2_c),0)
    blurS = cv2.GaussianBlur(output,(b1_s,b2_s),0)
    blurL = cv2.GaussianBlur(output,(b1_l,b2_l),0)
    grayC = cv2.cvtColor(blurC, cv2.COLOR_BGR2GRAY)
    grayS = cv2.cvtColor(blurS, cv2.COLOR_BGR2GRAY)
    grayL = cv2.cvtColor(blurL, cv2.COLOR_BGR2GRAY)
#   imgname2 = "_gray".join(os.path.splitext(imgname))  [[removed]]
#   cv2.imwrite(imgname2, gray)  [[removed]]

# detect circles in the image
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50)#, #maxRadius = 200)
# 50 = min distance between centers of HoughCircles
# too wide a radius returns false positives; try iterations of min50max100; min101max150; etc
# compass is between 87 and 90px

# ITERATION for compass circles
    circlesC = cv2.HoughCircles(grayC,cv2.HOUGH_GRADIENT,1,50,
                                param1=p1_c,param2=p2_c,minRadius=rmin_c,maxRadius=rmax_c)
    if circlesC is not None:
        circlesC = np.round(circlesC[0, :]).astype("int")

        for (x, y, r) in circlesC:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), 2)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)

# ITERATION for smaller than compass circles
    circlesS = cv2.HoughCircles(grayS,cv2.HOUGH_GRADIENT,1,50,
                                param1=p1_s,param2=p2_s,minRadius=rmin_s,maxRadius=rmax_s)
    if circlesS is not None:
        circlesS = np.round(circlesS[0, :]).astype("int")

        for (x, y, r) in circlesS:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), 2)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)


# ITERATION2 for larger than compass circles
    circlesL = cv2.HoughCircles(grayL,cv2.HOUGH_GRADIENT,1,50,
                                param1=p1_l,param2=p2_l,minRadius=rmin_l,maxRadius=rmax_l)
    if circlesL is not None:
        circlesL = np.round(circlesL[0, :]).astype("int")

        for (x, y, r) in circlesL:
            # draw the outer circle
            cv2.circle(output,(x, y), r, (0, 255, 0), 2)
            # draw the radius
            cv2.putText(output,str(r),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            # draw the center of the circle
            cv2.circle(output,(x, y), 2, (0, 0, 255), 3)


# count circles in each iteration
    if circlesC is not None:
        no_of_circlesC = int(len(circlesC))
    else: no_of_circlesC = int(0)

    if circlesS is not None:
        no_of_circlesS = int(len(circlesS))
    else: no_of_circlesS = int(0)

    if circlesL is not None:
        no_of_circlesL = int(len(circlesL))
    else: no_of_circlesL = int(0)

# if there is a noncompass circle, or if there are two circles of compass size
    if (no_of_circlesS>0) or (no_of_circlesL>0) or (no_of_circlesC>1):
        imgname1 = "_out".join(os.path.splitext(imgname))
        imgname1 = change_to_output(imgname1)
        cv2.imwrite(imgname1, output)
