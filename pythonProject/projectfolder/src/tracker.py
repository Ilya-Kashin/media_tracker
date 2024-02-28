"""отслеживает поступление новых файлов и открывает их"""

from pickers import *
import os
import psutil
import getpass


class Tracker:
    """Класс для отслеживания и выдачи файлов"""
    @staticmethod
    def check_list():
        """
         Функия проверяет наличие  файлов в дериктории

         Параметры:

         Возвращает:
            True: если  есть
            False: если нет
         """
        list_of_files = os.listdir(path=os.getenv('PATH_1'))
        if len(list_of_files) != 0:
            return True
        else:
            return False

    @staticmethod
    def ckeck_opened():
        """
        Функия проверяет закрыт ли  фото/текстовый файл в системе

        Параметры:

        Возвращает:
            True: если   открыт
            False: если  закрыт
        """
        list_1 = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            if proc.info['username'] == getpass.getuser() and (
                    proc.info['name'] == 'eog' or proc.info['name'] == 'gedit'):
                list_1.append((proc.pid, proc.info['name']))

        if len(list_1) == 0:
            return False
        else:
            return True

    @staticmethod
    def get_file():
        """
        Функция выдает очередной файл

        Параметры:

        Возвращает:
            str:  имя файла
        """
        file = os.listdir(path=os.getenv('PATH_1'))[0]
        return file


class Reader:
    """Класс для чтения файлов"""
    @staticmethod
    def open_file(file):
        command = "xdg-open " + os.getenv('PATH_1') + file
        os.system(command)


B = Pickers()
while True:
    if Tracker.check_list():
        file = Tracker.get_file()
        Reader.open_file(file)
        while Tracker.ckeck_opened():
            continue
        B.move_to_dump(file)
    else:
        continue
