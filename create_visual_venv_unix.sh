#!/usr/bin/env bash

VENVNAME=cv101

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

# Makes sure the required directories are present (since git does not clone empty folders)
mkdir -p data/
mkdir -p features/
mkdir -p output/

echo "build $VENVNAME"
