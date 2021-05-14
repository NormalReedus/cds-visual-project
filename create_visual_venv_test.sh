#!/usr/bin/env bash

VENVNAME=testvenv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

test -f testreq.txt && pip install -r testreq.txt

echo "build $VENVNAME"
