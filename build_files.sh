#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e  

# Set up the virtual environment
if [ ! -d "$HOME/venv" ]; then
    python3 -m venv $HOME/venv
fi

export VIRTUAL_ENV=$HOME/venv
export PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt

# Run migrations (optional, if using a database)
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic 
