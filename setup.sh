#!/bin/bash

deployment_dir = "~/.deployment"


# Create .deployment folder
mkdir $deployment_dir

# Create virtual environment for python
python3 -m venv $deployment_dir/.venv/

# Activate virtual environment for python
source $deployment_dir/.venv/bin/activate

# Change directory to venv

cd $deployment_dir/

# Update Pip Module

python3 -m pip install --upgrade --user

# Install Ansible

python3 -m pip install ansible --user

