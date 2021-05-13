# %% IMPORTS
import os
import json
import numpy as np
from sklearn.neighbors import NearestNeighbors

from utils import get_filepaths
from shutil import copyfile # To show the output images


# %% LOAD FEATURE_LIST
# Load in the image embedding features
feature_list = np.genfromtxt(os.path.join('..', 'features', 'feature_list.csv'), delimiter=",")
# Load file_map between feature index and filename
with open(os.path.join('..', 'features', 'file_map.json')) as file:
    file_map = json.load(file)

# %% NEAREST NEIGHBORS
# Brute force knn calculates distances between all image embeddings (up to n_neighbors), but is fairly quick in this case
# When no classification is done n_neighbors can just be the number of neighbors we are interested in seeing
neighbors = NearestNeighbors(n_neighbors=10, 
                             algorithm='brute',
                             metric='cosine').fit(feature_list)

# Get the neighbors to our target (in the order of how close they are)
feature_index = file_map.index('insta14121.jpg')
distances, indices = neighbors.kneighbors([feature_list[feature_index]])

# idxs[0] is the target image
# Contains indices of the images that are the most like the target
idxs = []
for i in range(len(indices[0])):
    print(distances[0][i], indices[0][i])
    idxs.append(indices[0][i])

# %% # SAVE OUTPUT
# All image paths
filepaths = get_filepaths() 

for i, fileidx in enumerate(idxs):
    # TODO: select file from fileidx by searching map for filename and concatenating to DATA_DIR
    # filename = key_from_val(file_map, fileidx)
    filename = file_map[fileidx]
    _, file_ext = os.path.splitext(filename)
    filepath = os.path.join('..', 'data', filename)

    # new neighboring file is identified by fileidx and named according to how close it is to the target (i)
    copyfile(filepath, os.path.join('..', 'output', f'{i}{file_ext}')) 

# %%


# ARGS
# n_neighbors: how many related images to see
# target image file (only works if all images are used)