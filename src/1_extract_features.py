# base tools
import os
import json
import argparse
from pathlib import Path

# data analysis
import numpy as np
from numpy.linalg import norm
from tqdm import tqdm

# tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # No cuda warnings
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

from utils import get_filepaths

# ResNet expects a 224x224px image
IMAGE_SHAPE = (224, 224, 3)

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

def main(data_path, sample_num):
    # ImageNet is a great, diverse dataset
    # We don't include the last layer (top) since we need image embedding features, not the classification part
    # Average pooling is good for natural, diverse images with more complex motifs
    model = ResNet50(weights='imagenet', 
                    include_top=False,
                    pooling='avg',
                    input_shape=IMAGE_SHAPE)

    # Returns a list of all images in data/
    filepaths = get_filepaths(data_path)

    # Contains the image embeddings
    feature_list = []

    # Mapping between filenames and the index of the corresponding image embedding features in feature_list
    file_map = []

    if sample_num != None:
        num_files = sample_num
    else:
        num_files = len(filepaths)

    # Do the actual feature (image embedding) extraction for all images
    for i in tqdm(range(num_files)):
        feature_list.append(extract_features(filepaths[i], model))
        # Save reference to the original image file
        filename = os.path.basename(filepaths[i])
        # Index of filename in file_map will match index in feature_list
        file_map.append(filename)

    # Save features to a file, so this script does not have to run every time
    np.savetxt(os.path.join('..', 'features', 'feature_list.csv'), feature_list, delimiter=",")

    # Save references to the original filenames
    with open(os.path.join('..', 'features', 'file_map.json'), 'w') as file:
        json.dump(file_map, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "extract image embedding features from the image data")
   
    parser.add_argument("-d", "--data_path", default=Path('../data/'), type = Path, help = "path to the directory containing the image files")
    parser.add_argument("-s", "--sample_num", default=None, type = int, help = "a number of sample files to extract features from (to avoid using the whole dataset). Omit this if you are useing the whole dataset")

    args = parser.parse_args()
    
    main(data_path = args.data_path, sample_num = args.sample_num)