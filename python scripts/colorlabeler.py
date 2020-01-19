# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
import argparse
from skimage.color import rgb2lab, deltaE_cie76
import os



class colorlabeler:
    COLORS = {
        'GREEN': [0, 128, 0],
        'BLUE': [0, 0, 128],
        'YELLOW': [255, 255, 0],
    	'RED': [128, 0, 0],
    	'PURPLE': [255, 0, 255],
    	'ORANGE': [255, 165, 0],
        'BROWN': [150, 75, 0]
    }
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
    	help="path to input image")
    args = vars(ap.parse_args())
    
    def __init__(self, args):
        self.args = args

    def RGB2HEX(self, color):
        return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

    def get_image(self, imagepath):
        image = cv2.imread(imagepath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image


    def get_colors(self, image, number_of_colors):
    	modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    	modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

    	clf = KMeans(n_clusters = number_of_colors)
    	labels = clf.fit_predict(modified_image)

    	counts = Counter(labels)

    	center_colors = clf.cluster_centers_
    	# We get ordered colors by iterating through the keys
    	ordered_colors = [center_colors[i] for i in counts.keys()]
    	hex_colors = [self.RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    	rgb_colors = [ordered_colors[i] for i in counts.keys()]
    	return rgb_colors


    def match_image_by_color(self, image, color, number_of_colors = 5):

        image_colors = self.get_colors(image, number_of_colors)
        selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

        select_image = False
        for i in range(number_of_colors):
            curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
            diff = deltaE_cie76(selected_color, curr_color)

        return diff


def main():
    images = []
    labeler = colorlabeler(args["input"])
    for file in os.listdir(args["input"]):
        if not file.startswith('.'):
            images.append(labeler.get_image(os.path.join(args["input"], file)))
    colors = []
    for i in range(len(images)):
    	selected = []
    	for color in COLORS.keys():
    		selected.append(labeler.match_image_by_color(images[i], COLORS[color]))
    	colors.append(list(COLORS.keys())[selected.index(min(selected))])
    print(colors)
    return colors

if __name__ == '__main__':
	main()
