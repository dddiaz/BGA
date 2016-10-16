#!/bin/bash

# Don't forget chmod +x the_file_name

# setup venv if needed
# pip install virtualenv
# pip install --upgrade virtualenv
# python3 -m venv <DIR>
# source <DIR>/bin/activate
# pip install -r requirements.txt

echo -e "Starting app.py"
export FLASK_APP=app.py
#flask run
python3 app.py

