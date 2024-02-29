"""отслеживает поступление новых файлов и открывает их"""

from pickers import *
import os
import subprocess


class Reader:
    """Класс для чтения файлов"""
    proc_poll= None
    def open_file(self, file):
        """Проверяет формат файла. Если формат допустимый, октрывает документ"""

        extension=Pickers()._get_names_or_extension(file)[1]
        if extension in ['.jpg', '.jpeg', '.png']:
            command = os.getenv('PATH_MEDIA') + file
            proc_open=subprocess.Popen(['eog', command])
            proc_open.wait()
            self.proc_poll=proc_open.poll()
        elif Pickers()._get_names_or_extension(file)[1] in ['.txt']:
            command = os.getenv('PATH_MEDIA') + file
            proc_open = subprocess.Popen(['gedit', command])
            self.proc_pid = proc_open.pid
            self.proc_poll=proc_open.poll()
        else:
            self.proc_pid = None
            print('НЕдопустимый формат файла')


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
        list_of_files = os.listdir(path=os.getenv('PATH_MEDIA'))
        if len(list_of_files) != 0:
            return True
        else:
            return False

    @staticmethod
    def check_opened(poll=Reader.proc_poll):
        """
        Функия проверяет закрыт ли  фото/текстовый файл в системе

        Параметры:

        Возвращает:
            True: если   открыт
            False: если  закрыт
        """
        if poll==None:
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
        file = os.listdir(path=os.getenv('PATH_MEDIA'))[0]
        return file




def run ():
  pickers = Pickers()
  reader = Reader()
  while True:
      if Tracker.check_list():
          file = Tracker.get_file()
          reader.open_file(file)
          while Tracker.check_opened():
              continue
          pickers.move_to_dump(file)
      else:
          continue


if __name__=="__main__":
    run()



