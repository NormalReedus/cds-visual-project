# cds-visual-project
## Notes
- Find ud af hvordan vi beder brugeren om at hente data
    - Vi kunne lave et script, der downloader dataene og flytter dem ind i `./data/`?
    - Husk en guide til at hente WGET på Windows
- Husk at forklare noget om hvor lang tid det tager (og giv mulighed for en demo)
- Tilføj mulighed for at passe et custom data-dir ind i begge scripts
- Lav beskrivelse af, at man kan køre en demo for at se at første script virker, og så kan man kopiere all_features ind i /features for at teste anden del på det fulde data
- Forklar at kun nogle filer kan bruges, hvis man kører script 1 med en demo
- Lav forklaring om hvordan filstrukturen skal se ud i projektet (lav mapper, der ikke findes)
- Forklar at man skal køre scripts inde fra src for at paths virker
- Forklar at man skal aktivere venv efter det er bygget (det gør den ikke ad sig selv, i hvert fald på windows)
- Forklar at bash og python er nødvendigt at have
    - Python 3.8.6 (linux) og 3.9.1 (win) er testet 
- Forklar at man manuelt skal slette outputs, hvis man vil køre den igen


## Reproducibility
- Make sure you have permissions to run the `create_visual_venv` bash scripts. On Linux (GNOME) this can be done by right clicking the file, entering 'Permissions' and checking the box that says: 'Allow executing file as program". In bash this can be done by `cd`ing into the containing directory and running `chmod +x create_visual_venv.sh` or `chmod +x create_visual_win_venv.sh` if you are on Windows.
- If the VENV-setup complains that it cannot install dependencies with pip, you can just copy [this script](bootstrap.pypa.io/get-pip.py) as `get-pip.py` in the project root, activate the VENV and run the file with python. Afterwards the file can be deleted, and installing requirements can resume.
