# cds-visual-project
## Prerequisites
You will need to have Bash and Python 3 installed on your computer. These scripts have been tested with Python 3.9.1 on Windows 10 and Python 3.8.6 on Linux (Ubuntu flavour).

## Installation
- Clone this repository somewhere on your computer
- Open a Bash terminal in the root directory of the cloned repository
- Run the correct Bash script to generate your virtual environment, generate required directories, and install dependencies:

Windows
```bash
./create_venv_win.sh
```

Mac / Linux
```bash
./create_venv_unix.sh
```
- If you have any issues with the last step, make sure your terminal is running as administrator (on Windows) and that you can execute the bash scripts with:

Windows
```bash
chmod +x create_venv_win.sh
```

Mac / Linux
```bash
chmod +x create_venv_unix.sh
```

## Running the scripts
- Make sure the newly created virtual environment is activated with:

Windows
```bash
source cv101/Scripts/activate
```

Mac / Linux
```bash
source cv101/bin/activate
```

Your repository should now have at least these files and directories:

`/`
```
├── create_venv_unix.sh
├── create_venv_win.sh
├── cv101/
├── data/
├── features/
├── get-pip.py
├── output/
├── README.md
├── requirements.txt
└── src/
    ├── 0_get_data.py
    ├── 1_extract_features.py
    ├── 2_knn.py
    └── utils.py
```

**NOTE:** Going forwards we will assume you have an alias set for running `python` such that you will not have to type `python3` if that is normally required on your system (usually Mac / Linux). If this is not the case, you will have to substitute `python` with `python3` in the following commands.

- Change into `/src/` with `cd src/` - this is important to make relative paths work correctly
- You will need to have `../data/` filled with image files that are either `.jpg`, `.jpeg`, or `.png`
    - This repo comes with a demo dataset of objects that you can use, OR
    - You can run `python 0_get_data.py` to download an arbitrary dataset from Kaggle
        - NOTE: The script will automatically find the raw images, but only if these are in the outermost leaf-directories of the data
        - In order to be able to use the kaggle api from python, a valid username and api-key must be present. This is downloaded as a JSON file by clicking on "Create New API Token" on your kaggle "account" page 
        - The kaggle API will look for this json-file in:
            - ~/.kaggle/kaggle.json if you're on a Unix system
            - C:\users\<Windows-username>\.kaggle\kaggle.json if you're on Windows
        - `-ku` or `--kaggle_url` (required) is the location of the dataset to download (e.g. `<username>/<dataset-name>)
        - `-d` or `--data_path` (default is `../data/`) is the path to where you want to save the image files
        - E.g.:
        ```bash
        python 0_get_data.py -ku jessicali9530/coil100 -d ../some/other/path
        ```
- You can now run `python 1_extract_features.py` to generate reusable image embedding features for all images in `../data/`. These features (and a map linking them to the original files) will be saved in `../features/`
    - You can change the path to the data folder with the flag `-d` or `--data_path` (default is `../data/`)
    - Since this process *can* take a while you can run the feature extraction on a sample set of files (for demo purposes if the dataset is too large) with the flag `-s` or `--sample_num`
    - E.g.:
    ```bash
    python 1_extract_features.py -d ../some/other/path/ -s 300
    ```
- If you wish to try identifying similar images without extracting features for all of the data you can use the extracted features that are already present in `../features/`
    - If you wish to both run script `1_extract_features.py` with a sample **and** try to identify images with the included features, you will have to move the included file out of `../features/` first, as this file will be overwritten when running `1_extract_features.py`
- You can now find images in the dataset that most resemble a target image by running `python 2_knn.py -t <some image>`
    - `-t` or `--target_name` is required, this is the name of the image file in `data_path` to find other resembling images from
        - NOTE: This name does not include the path to the image, just the filename
        - NOTE: If features have been extracted from only a sample of images you will need to make sure that the target image is one of them. This can be done by selecting the target image name from the list of files in `../features/file_map.json`
    - `-d` or `--data_path` is the path to where the images are stored (default is `../data/`)
    - `-nn` or `--num_neighbors` is the number of resembling images to show (default is 10)
    - E.g.:
    ```bash
    python 2_knn.py -t image_of_cat.jpg -d ../some/other/path/ -nn 25
    ```
- Your terminal should show a readout of the images that resemble your target in order (including the target itself), and copy the resembling files into `../output/` for inspection. The files will be ordered so number `0` will be the target image, number `1` will be the most resembling image and so on up until `num_neighbors` 
