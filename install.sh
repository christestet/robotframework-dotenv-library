#!/usr/bin/env bash
PYTHON_VENV=my_env

echo "this script uses venv to install pip packages - make shure you have python 3.7 or above and python - venv installed"

echo "creating venv $PYTHON_VENV in repository root directory"
python3 -m venv $PYTHON_VENV   

echo "activating $PYTHON_VENV python venv"
source $PYTHON_VENV/bin/activate 

echo "installing python packages"
pip3 install -r requirements.txt

echo "installation finished"