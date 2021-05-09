# %% IMPORTS
# base tools
import os

# data analysis
import numpy as np
from numpy.linalg import norm
from tqdm import tqdm

# tensorflow
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

from utils import get_filenames

# %% HELPERS
def extract_features(img_path, model):
    """
    Extract features from image data using pretrained model (e.g. VGG16)
    """
    # Define input image shape - remember we need to reshape
    input_shape = (224, 224, 3)
    # load image from file path
    img = load_img(img_path, target_size=(input_shape[0], 
                                          input_shape[1]))
    # convert to array
    img_array = img_to_array(img)
    # expand to fit dimensions
    expanded_img_array = np.expand_dims(img_array, axis=0)
    # preprocess image - see last week's notebook
    preprocessed_img = preprocess_input(expanded_img_array)
    # use the predict function to create feature representation
    features = model.predict(preprocessed_img)
    # flatten
    flattened_features = features.flatten()
    # normalise features
    normalized_features = flattened_features / norm(features)
    return flattened_features


# %% LOAD MODEL
model = ResNet50(weights='imagenet', 
                  include_top=False,
                  pooling='avg',
                  input_shape=(224, 224, 3))

# %% EXTRACT FEATURES & LOAD FILES
filenames = get_filenames() 

feature_list = []

#! SAMPLE
sample_num = 200
for i in tqdm(range(sample_num)):
    feature_list.append(extract_features(filenames[i], model))

# %% SAVE FEATURE_LIST
np.savetxt('../data/feature_list.csv', feature_list, delimiter=",")
# %%
