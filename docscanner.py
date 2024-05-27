# import the necessary packages

from fourpointscan import *
from skimage.filters import threshold_local     # Help us obtain the “black and white” feel to our scanned image.
import numpy as np      # Use for numerical processing
import argparse     # Useful for parsing command line arguments
import cv2      # Contains OpenCV functions
import imutils      # Contains functions for resizing, rotating, and cropping images

# construct the argument parser and parse the arguments for command line/terminal
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned") # "--image" is the path to the image that contains the document we want to scan
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) # load the image
# reseize scanned image to have a height of 500 pixels for better accuracy
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
gray = cv2.GaussianBlur(gray, (5, 5), 0) # Blur to remove high frequency noise
edged = cv2.Canny(gray, 75, 200) # Perform edge detection

# Show the original image and the edge detected image
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break
        # The scanner app will assume that (1) the document to be scanned is the main focus of the image and 
        # (2) the document is rectangular, and thus will have four distinct edges

# show the contour (outline) of the piece of paper
print("STEP 2: Find contours of paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply the four point transform to obtain a top-down view of the original image
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
# Note: We multiply by the resized ratio because we performed edge detection and found contours on the resized image of height=500 pixels.
# However, we want to perform the scan on the original image, not the resized image, thus we multiply the contour points by the resized ratio.

# convert the warped image to grayscale, then threshold it to give it that 'black and white' paper effect
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255

# show the original and scanned images
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)