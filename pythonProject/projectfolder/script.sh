#!/bin/bash
#вставьте путь в формате как в примере 
read -p "Введите путь до папки с медиа файлами:" PATH_MEDIA
export PATH_MEDIA
read  -p "Введите путь до папки-мусорки:" PATH_DUMP
export PATH_DUMP
pip install -r requirements.txt
python3 $PWD/src/tracker.py
