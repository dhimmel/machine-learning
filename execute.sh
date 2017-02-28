#!/bin/bash

# Exit on error
set -o errexit

source activate cognoma-machine-learning

jupyter nbconvert --inplace --execute --ExecutePreprocessor.timeout=-1 *.ipynb
jupyter nbconvert --to=script --FilesWriter.build_directory=scripts *.ipynb
