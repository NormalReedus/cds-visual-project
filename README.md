# cds-visual-project
## Notes
- Find ud af hvordan vi beder brugeren om at hente data
    - Vi kunne lave et script, der downloader dataene og flytter dem ind i `./data/`?
    - Husk en guide til at hente WGET på Windows
- Lav beskrivelse af, at man kan køre en demo for at se at første script virker, og så kan man kopiere all_features ind i /features for at teste anden del på det fulde data
- Forklar at man manuelt skal slette outputs, hvis man vil køre den igen

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
- You will need to fill `../data/` with image files that are either `.jpg`, `.jpeg`, or `.png` files. To do this you can RUN 0_GET_DATA.PY
    - In order to be able to use the kaggle api from python, a valid username and api-key must be present. This is downloaded as a JSON file by clicking on "Create New API Token" on your kaggle "account" page. 
    - The kaggle API will look for this json-file in:
        - ~/.kaggle/kaggle.json if you're on linux
        - C:\users\<Windows-username>\.kaggle\kaggle.json if you're on windows.
- You can now run `python 1_extract_features.py` to generate reusable image embedding features for all images in `../data/`. These features (and a map linking them to the original files) will be saved in `../features/`
    - You can change the path to the data folder with the flag `-d` or `--data_path` (default is `../data/`)
    - Since this process *can* take a while you can run the feature extraction on a sample set of files (for demo purposes if the dataset is too large) with the flag `-s` or `--sample_num`
    - E.g.:
    ```bash
    python 1_extract_features.py -d ../some/other/path/ -s 300
    ```
- MAYBE EXPLAIN THAT YOU CAN DOWNLOAD INSTAFEATURES FROM DRIVE TO TRY THE WHOLE DATASET
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
- Your terminal should show a readout of the images that resemble your target in order (including the target itself), and copy the resembling files into `../output` for inspection. The files will be ordered so number `0` will be the target image, number `1` will be the most resembling image and so on up until `num_neighbors` 
