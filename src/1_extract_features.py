# %% IMPORTS
# base tools
import os
import json

# data analysis
import numpy as np
from numpy.linalg import norm
from tqdm import tqdm

# tensorflow
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

from utils import get_filepaths

# ResNet expects a 224x224px image
IMAGE_SHAPE = (224, 224, 3)

# %% HELPERS

# Preprocesses images for ResNet and extracts the image embedding data
def extract_features(img_path, model):
    
    # load image from file path and resizes to IMAGE_SHAPE
    img = load_img(img_path, target_size=(IMAGE_SHAPE[0], 
                                          IMAGE_SHAPE[1]))

    # convert to numpy ndarray since we can manipulate this
    img_array = img_to_array(img)

    # wrap in ndarray to explicitly say that there is just 1 image (ResNet50 expects array of images)
    expanded_img_array = np.expand_dims(img_array, axis=0)

    # preprocess image - see last week's notebook
    preprocessed_img = preprocess_input(expanded_img_array)

    # generate image embedding feature representation of the given image
    features = model.predict(preprocessed_img)

    flattened_features = features.flatten()

    normalized_features = flattened_features / norm(features)

    return normalized_features

# %% LOAD MODEL
# ImageNet is a great, diverse dataset
# We don't include the last layer (top) since we need image embedding features, not the classification part
# Average pooling is good for natural, diverse images with more complex motifs
model = ResNet50(weights='imagenet', 
                  include_top=False,
                  pooling='avg',
                  input_shape=IMAGE_SHAPE)

# %% LOAD FILES, EXTRACT FEATURES & CREATE REFERENCES TO ORIGINAL FILES

# Returns a list of all images in data/
filepaths = get_filepaths() 

# Contains the image embeddings
feature_list = []

# Mapping between filenames and the index of the corresponding image embedding features in feature_list
file_map = []

#! SAMPLE
sample_num = 100
# Do the actual feature (image embedding) extraction for all images
for i in tqdm(range(len(filepaths))):
    feature_list.append(extract_features(filepaths[i], model))
    # Save reference to the original image file
    filename = os.path.basename(filepaths[i])
    # Index of filename in file_map will match index in feature_list
    file_map.append(filename)

# %% SAVE FEATURE_LIST
# Save features to a file, so this script does not have to run every time
np.savetxt(os.path.join('..', 'features', 'feature_list.csv'), feature_list, delimiter=",")

# Save references to the original filenames
with open(os.path.join('..', 'features', 'file_map.json'), 'w') as file:
    json.dump(file_map, file)
# %%


# ARGS
# Where to get data