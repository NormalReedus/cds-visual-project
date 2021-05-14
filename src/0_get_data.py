from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import os

def run():
    #Setup auth for Kaggle. Authenticate() needs a valid .kaggle json
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('zalando-research/fashionmnist', path='../data', unzip = True)

    #Extract all
    # zf = ZipFile('../data/')

if __name__ == '__main__':
    run()