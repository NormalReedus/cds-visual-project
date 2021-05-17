from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os
import shutil

#Should this be argparsed? As long as the downloaded dataset has its data at the bottom of directories, this will work but..?

#Delete everything in a folder that doesnt have the valid_suffix as extension   
def filter_dir(dir_path, valid_suffixes):
    dir_contents = os.listdir(dir_path)
    for content in dir_contents:
        _, extension = os.path.splitext(content)
        content_path = os.path.join(dir_path, content)

        if extension.lower() not in valid_suffixes:
            if os.path.isdir(content_path):
                shutil.rmtree(content_path)
            else:
                os.remove(content_path)

#Move all files in a folder to another folder
def move_files(list_of_paths, target_folder_path):
    for path in list_of_paths:
        shutil.move(path, target_folder_path)

#Runs to the bottom of all dirs in the root-dir.
#once the bottom is reached in each dir, return a list of all the files on the bottom of each dir. 
def get_bottom_dir_paths(root_dir_path):
    dir_contents = os.listdir(root_dir_path)
    bottom_dir_paths = []

    for content in dir_contents:
        dir_path = os.path.join(root_dir_path, content)
        if os.path.isdir(dir_path):
            for root, dirs, files in os.walk(dir_path):
                if not dirs:
                    for file in files:
                        bottom_dir_paths.append(os.path.join(root, file))

    return bottom_dir_paths

#Checks if a dir contains anything.
def dir_is_empty(dir_path):
    print(len(os.listdir(dir_path)))
    if len(os.listdir(dir_path)) == 0:
        return True
    else:
        return False

#Deletes all subdirectories aswell as files inside a dir. 
def delete_everything_in_dir(dir_path):
    dir_contents = os.listdir(dir_path)
    for content in dir_contents:
        content_path = os.path.join(dir_path, content)
        if os.path.isdir(content_path):
            shutil.rmtree(content_path)
        else:
            os.remove(content_path)

def run(data_dir_path):
    user_input = input('This script will download and place the files from our kaggle dataset. In doing so, it will delete everything inside the data-directory within this repo and replace it. Continue? [yes/no] ')
    if user_input == 'yes' or user_input == 'Yes' or user_input == 'y' or user_input == 'Y':
        if not dir_is_empty(data_dir_path):
            print('Deleting everythinging in data folder')
            delete_everything_in_dir(data_dir_path)

        #Kaggle download
        api = KaggleApi()
        api.authenticate()
        
        print('Downloading dataset from kaggle - the delay after the bar hits 100 is the script unzipping. Please be patient.')
        api.dataset_download_files('prithvijaunjale/instagram-images-with-captions', force=True, path='../data', unzip = True, quiet=False)

        #Moving files - housekeeping
        print('Moving files')
        bottom_dir_paths = get_bottom_dir_paths(data_dir_path)
        move_files(bottom_dir_paths, data_dir_path)
        filter_dir(data_dir_path, ['.jpg', '.png', '.jpeg'])

    elif user_input == 'no' or user_input == 'No' or user_input == 'n' or user_input == 'N':
        print('Abandon ship!')
    else:
        print('Please input either "yes" or "no"')
    
if __name__ == '__main__':
    run(os.path.join('..', 'data'))