"""перемещает отработавший файл в dump"""

import os
import time
class Pickers:
    path_media = os.getenv('PATH_MEDIA')
    path_dump= os.getenv('PATH_DUMP')
    @staticmethod
    def _get_names_or_extension(file):
        pos=file.rfind('.')
        name=file[:pos]
        extension=file[pos:]
        return name, extension

    def _change_name(self, file):
        name = self._get_names_or_extension(file)[0]
        extension=self._get_names_or_extension(file)[1]
        name_new = name + str(time.time())+extension
        return  name_new
    def move_to_dump(self, file):
        new_path= self.path_dump+ self._change_name(file)
        old_path= self.path_media+os.listdir(path=os.environ['PATH_MEDIA'])[0]
        os.replace(old_path, new_path)