import cv2
import matplotlib.pyplot as plt
import os
import argparse
# %matplotlib inline

#sources
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--input1", required=True,
	help="path to test image")
ap.add_argument("-i2", "--input2", required=True,
	help="path to retrieved images")
args = vars(ap.parse_args())

#reading both retrieved and actual image; converts image from rgb to grey
sift = cv2.AKAZE_create()
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

actual = cv2.imread(ap["input1"])
actual_gray = cv2.cvtColor(actual, cv2.COLOR_BGR2GRAY)
keypoints_1, descriptors_1 = sift.detectAndCompute(actual_gray, None)
images = []

for image in os.listdir(ap["input2"]):
    print(image)
    retrieved = cv2.imread(os.path.join(folder, image))
    retrieved_gray = cv2.cvtColor(retrieved, cv2.COLOR_BGR2GRAY)
    keypoints_2, descriptors_2 = sift.detectAndCompute(retrieved_gray,None)
    matches = bf.match(descriptors_1,descriptors_2)
    matches = sorted(matches, key = lambda x:x.distance)
    images.append(matches)

#returns the top image from the match
lengths = [len(image) for image in images]
print(lengths)
top_image = lengths.index(max(lengths))

if lengths[top_image] > 200:
    print("True")
