import os

def get_filepaths(data_dir = os.path.join('..', 'data')):
    # Valid file extensions
    extensions = ['.jpg', '.jpeg', '.png']

    # Create a list of image filepaths
    file_list = []
    for root, directories, filepaths in os.walk(data_dir):
        for filepath in filepaths:
            # Keep only those with valid extensions
            if any(ext in filepath.lower() for ext in extensions):
                file_list.append(os.path.join(root, filepath))

    if len(file_list) == 0:
        raise Exception(f'cannot find data in: {data_dir}')

    return file_list
