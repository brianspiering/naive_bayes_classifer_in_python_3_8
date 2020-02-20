#!/bin/bash

# Before running this script, install anaconda or miniconda with Python 3.x
# https://www.anaconda.com/distribution/#download-section

# After installing either anaconda or miniconda, open a new terminal code so conda is on the path.
# Must cd into this directory to run this script successfully.

# Setup the environment for the classroom. TeachOps FTW!
set -e # Exit immediately if a command exits with a non-zero status
set -x # Exit immediately if a pipeline exits with a non-zero status

# Name of environment
envname=$(sed '1!d' environment.yml | sed 's/^.* //')

# Create environment based on environment.yml in the same directory
conda update --name base conda --yes  
conda env create --name $envname --force 

# Start environment
conda activate $envname

# Enable extensions
# May raise an error, not an issue 
# These are only nice-to-have options
jupyter contrib nbextension install --user
jupyter nbextension enable spellchecker/main
jupyter nbextension enable codefolding/main
jupyter nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix
