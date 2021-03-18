#!/bin/bash
echo "Running File Orgnaizer"
FILE="$PWD/venv/"
echo "Looking for virtual env"  $FILE
if [[ -d $FILE ]]
then
	echo "Activating virtual env"
	source venv/bin/activate
else 
	echo "Virtual Environment is not installed in path"
	python3 -m venv venv 
	source venv/bin/activate
	pip install -r requirements.txt
fi

python main.py

deactivate
