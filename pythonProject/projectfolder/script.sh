#!/bin/bash
#вставьте путь в формате как в примере 

export PATH_MEDIA=/home/ilya/work_dir/media/
export PATH_DUMP=/home/ilya/work_dir/dump/
echo $PATH_MEDIA
pip install -r requirements.txt
python3 /home/ilya/PycharmProjects/media_tracker/pythonProject/projectfolder/src/tracker.py
