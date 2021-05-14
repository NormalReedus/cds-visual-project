import os
import json
import argparse
from pathlib import Path
from shutil import copyfile # To show the output images

import numpy as np
from sklearn.neighbors import NearestNeighbors

from utils import get_filepaths

def main(num_neighbors, target_name, data_path):
    # Raise exception early if data_path does not exist
    if not os.path.isdir(data_path):
        raise Exception(f'cannot find data_path: {data_path}')

    # NearestNeighbors include the target itself, so we add 1 so it returns the correct number of neighbors (exluding the target)
    num_neighbors += 1

    # Load in the image embedding features
    feature_list = np.genfromtxt(os.path.join('..', 'features', 'feature_list.csv'), delimiter=",")
    # Load file_map between feature index and filename
    with open(os.path.join('..', 'features', 'file_map.json')) as file:
        file_map = json.load(file)

    # Brute force knn calculates distances between all image embeddings (up to n_neighbors), but is fairly quick in this case
    # When no classification is done n_neighbors can just be the number of neighbors we are interested in seeing
    neighbors = NearestNeighbors(n_neighbors=num_neighbors,
                                algorithm='brute',
                                metric='cosine').fit(feature_list)

    # Get the neighbors to our target (in the order of how close they are)
    feature_index = file_map.index(target_name)
    distances, indices = neighbors.kneighbors([feature_list[feature_index]])

    # idxs[0] is the target image
    # Contains indices of the images that are the most like the target
    idxs = []
    for i in range(len(indices[0])):
        print(distances[0][i], indices[0][i], file_map[indices[0][i]])
        idxs.append(indices[0][i])

    # Copy the similar images into /output
    for i, fileidx in enumerate(idxs):
        filename = file_map[fileidx]
        _, file_ext = os.path.splitext(filename)
        filepath = os.path.join(data_path, filename)

        # New neighboring file is identified by fileidx and named according to how close it is to the target (i)
        copyfile(filepath, os.path.join('..', 'output', f'{i}{file_ext}')) 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "extract image embedding features from the instagram dataset")
   
    parser.add_argument("-t", "--target_name", required = True, type = str, help = "name of the image file (in data_path) that you wish to find similar images to")
    parser.add_argument("-d", "--data_path", default = Path('../data/'), type = Path, help = "path to the directory containing the image files")
    parser.add_argument("-nn", "--num_neighbors", default = 10, type = int, help = "the number of similar images to the target image to display")

    args = parser.parse_args()
    
    main(data_path = args.data_path, num_neighbors = args.num_neighbors, target_name = args.target_name)