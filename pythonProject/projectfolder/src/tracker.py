"""отслеживает поступление новых файлов и открывает их"""
import time

from pickers import *
import os
import psutil
import getpass
class Tracker:

    @staticmethod
    def check_list(path_media):
        list_of_files = (os.listdir(path=path_media))
        if len(list_of_files)!=0:
            return True
        else: return False
    @staticmethod
    def ckeck_closed ():
        list_1 = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            if proc.info['username'] == getpass.getuser() and proc.info['name']=='eog' :
                list_1.append((proc.pid, proc.info['name']))

        if len(list_1) == 0:
            list=[]
            return False
        else: return True
    @staticmethod
    def path_to_file(path_media):
        list_of_files=os.listdir(path=os.environ['PATH_1'])
        return path_media+str(list_of_files[0])

class Reader():
    def open_file(self):
        command="xdg-open "+str(Tracker.path_to_file(os.environ['PATH_1']))
        os.system(command)
A=Reader()
B=Pickers()
while True:
    print(Tracker.check_list(os.environ['PATH_1']))
    if Tracker.check_list(os.environ['PATH_1']):
        A.open_file()
        while Tracker.ckeck_closed():
            continue
        list_of_files = os.listdir(path=os.environ['PATH_1'])
        B.move_to_dump(list_of_files[0])
    else: time.sleep(1)





