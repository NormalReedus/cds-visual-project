import os

#! make extensions all lowercase
def get_filepaths(root_dir = '../data/'):
    # define valid file extensions
    extensions = ['.jpg', '.jpeg', '.png']
    # create empty file list
    file_list = []
    # initialise counter
    counter = 1
    # use os.walk to create a list of image filepaths
    for root, directories, filepaths in os.walk(root_dir):
        for filepath in filepaths:
            # keep only those with valid extensions
            if any(ext in filepath.lower() for ext in extensions):
                file_list.append(os.path.join(root, filepath))
                # increment counter
                counter += 1

    filepaths = sorted(file_list)

    return filepaths

