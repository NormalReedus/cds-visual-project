#!/usr/bin/env bash

VENVNAME=testvenv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f testreq.txt && pip install -r testreq.txt

# Makes sure the required directories are present (since git does not clone empty folders)
mkdir -p data/
mkdir -p features/

echo "build $VENVNAME"
