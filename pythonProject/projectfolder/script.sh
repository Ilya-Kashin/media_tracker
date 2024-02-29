#!/bin/bash
#вставьте путь в формате как в примере 
read -p "Введите путь до папки с медиа файлами:" PATH_MEDIA
while ! [ -d $PATH_MEDIA ] 
do 
  read -p "Нет такой папки. Попробуйте еще раз:" PATH_MEDIA
  done
read  -p "Введите путь до папки-мусорки:" PATH_DUMP
while ! [ -d $PATH_DUMP ]
do 
  read -p "Нет такой папки. Попробуйте еще раз:" PATH_MEDIA
  done   
export PATH_MEDIA
export PATH_DUMP
pip install -r requirements.txt
python3 $PWD/src/tracker.py
