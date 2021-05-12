# %% IMPORTS
import os
import numpy as np
from sklearn.neighbors import NearestNeighbors

from utils import get_filepaths
from shutil import copyfile # To show the output images


# %% LOAD FEATURE_LIST
feature_list = np.genfromtxt(os.path.join('..', 'data', 'feature_list.csv'), delimiter=",")

# %% NEAREST NEIGHBORS
neighbors = NearestNeighbors(n_neighbors=10, 
                             algorithm='brute',
                             metric='cosine').fit(feature_list)

distances, indices = neighbors.kneighbors([feature_list[50]])

# Contains indices of the files that are the closest neighbors to the target
# idxs[0] is the target image
idxs = []
for i in range(0,10):
    print(distances[0][i], indices[0][i])
    idxs.append(indices[0][i])

# %% # SAVE OUTPUT
# All image paths
filepaths = get_filepaths() 

for i, fileidx in enumerate(idxs):
    file = filepaths[fileidx]
    _, fileext = os.path.splitext(file)

    # new neighboring file is identified by fileidx and named according to how close it is to the target (i)
    copyfile(filepaths[fileidx], os.path.join('..', 'output', f'{i}{fileext}')) 

# %%
