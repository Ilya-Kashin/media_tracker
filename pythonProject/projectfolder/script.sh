#!/bin/bash
#вставьте путь в формате как в примере 

export PATH_MEDIA=/home/ilya/work_dir/media/
export PATH_DUMP=/home/ilya/work_dir/dump/
pip install -r requirements.txt
python3 /pythonProject/projectfolder/src/tracker.py
