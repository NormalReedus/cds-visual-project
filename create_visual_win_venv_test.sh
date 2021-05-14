#!/usr/bin/env bash

VENVNAME=testvenv

python -m venv $VENVNAME
source $VENVNAME/Scripts/activate
pip install --upgrade pip

test -f testreq.txt && pip install -r testreq.txt

echo "build $VENVNAME"
