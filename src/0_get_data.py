from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os
import shutil

#Delete everything in a folder thats not the valid suffix
def filter_only_images(dir_path, valid_suffix):
    dir_contents = os.listdir(dir_path)
    for content in dir_contents:
        _, extension = os.path.splitext(content)
        content_path = os.path.join(dir_path, content)

        if extension.lower() != valid_suffix:
            print(extension)
            print(valid_suffix)
            if os.path.isdir(content_path):
                shutil.rmtree(content_path)
            else:
                os.remove(content_path)
        

#Move all files in a folder to another folder
def move_files(source_folder_path, target_folder_path):
    file_names = os.listdir(source_folder_path)
    for file in file_names:
        shutil.move(os.path.join(source_folder_path, file), target_folder_path)

def run(data_dir_path):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('prithvijaunjale/instagram-images-with-captions', path='../data', unzip = True, quiet=False)

    move_files(os.path.join('..', 'data', 'instagram_data', 'img'), os.path.join('..', 'data'))
    move_files(os.path.join('..', 'data', 'instagram_data2', 'img2'), os.path.join('..', 'data'))
    print('Moved all files')

    print('Trying to remove anything not images')
    filter_only_images(os.path.join('..','data'), '.jpg')

            

if __name__ == '__main__':
    run(os.path.join('..', 'data'))