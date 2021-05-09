# %% IMPORTS
import os
import numpy as np
from sklearn.neighbors import NearestNeighbors

# # matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# %matplotlib inline

from utils import get_filenames
from shutil import copyfile # To show the output images


# %% LOAD FEATURE_LIST
feature_list = np.genfromtxt('../data/feature_list.csv', delimiter=",")

# %% NEAREST NEIGHBORS
neighbors = NearestNeighbors(n_neighbors=10, 
                             algorithm='brute',
                             metric='cosine').fit(feature_list)

distances, indices = neighbors.kneighbors([feature_list[0]])

idxs = []
for i in range(1,6):
    print(distances[0][i], indices[0][i])
    idxs.append(indices[0][i])

# # %% SHOW CLOSEST
# filenames = get_filenames() 

# # plot 3 most similar
# f, axarr = plt.subplots(1,3)
# axarr[0].imshow(mpimg.imread(filenames[idxs[0]]))
# axarr[1].imshow(mpimg.imread(filenames[idxs[1]]))
# axarr[2].imshow(mpimg.imread(filenames[idxs[2]]))
# %% # SAVE OUTPUT
filenames = get_filenames() 

#! Use original file extension
copyfile(filenames[idxs[0]], '../output/img.jpg') 
# %%
