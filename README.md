# Detecting Coal Gasification using OpenCV #

This is a project at Brown University aimed at detecting the historic locations of coal gasification plants using digitized Sanborn maps and OpenCV.

Coal Gasification plants have a distinct shape on Sanborn maps making their detection using computer vision packages like [OpenCV](https://opencv.org/).



**compass_selector**
Reads in files, analyzes for compass-sized circles.
Outputs CSV list of positive and negative results.
A large proportion of positive results means you should run the "compasses" version of scripts on that folder.
To do so, change the "compass" variable from 0 to 1.

**FIMO**: For use with maps downloaded from FIMO database

**LOC**: For use with maps downloaded from Library of Congress API

**BW**: For use with black and white maps downloaded from ProQuest Sanborn Digital database.

**files_to_dataframe**: Take a list of images in folders and converts to dataframe. Analyze for compasses as you would using compass_selector
