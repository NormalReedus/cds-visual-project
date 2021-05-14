from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os
import shutil

#Delete everything in a folder thats not the valid suffix
def filter_only_images(dir_path, valid_suffix):
    dir_contents = os.listdir(dir_path)
    for content in dir_contents:
        _, extension = os.path.splitext(content)
        if extension is not valid_suffix:
            os.remove(os.path.join(dir_path, content))

#Move all files in a folder to another folder
def move_files(source_folder_path, target_folder_path):
    file_names = os.listdir(source_folder_path)
    for file in file_names:
        shutil.move(os.path.join(source_folder_path, file), target_folder_path)

def run():
    #Setup auth for Kaggle. Authenticate() needs a valid .kaggle json
    # api = KaggleApi()
    # api.authenticate()
    # api.dataset_download_files('prithvijaunjale/instagram-images-with-captions', path='../data', unzip = True, quiet=False)

    yeet = os.walk(os.path.join('..', 'data'))
    print(yeet.files)
    
    #Move around the files
    # data_dir_path = os.path.join('..', 'data')
    # data_subfolders = [content.path for content in os.scandir(data_dir_path) if os.path.isdir(content.path)]
    # for data in data_subfolders:
    #     dirs = os.scandir(data)
    #     for dir in dirs:
    #         print(dir.path)

    # data_subfolders = [content.path for content in os.scandir(data_dir_path) if content.is_dir()]
    

if __name__ == '__main__':
    run()