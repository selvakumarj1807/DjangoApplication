#!/bin/bash

# Ensure the script stops if any command fails
set -e

# Use the correct Python version installed by Vercel
export VIRTUAL_ENV=$HOME/venv
export PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput
