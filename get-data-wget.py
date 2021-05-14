import wget
from zipfile import ZipFile
import os

def run():
    wget.download('https://www.kaggle.com/zalando-research/fashionmnist/download', './data/tempfile.zip')
    zf = ZipFile('./data/tempfile.zip')
    zf.extractall(path = './data/')
    os.remove('./data/tempfile.zip')

if __name__ == '__main__':
    run()