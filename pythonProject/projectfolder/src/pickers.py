"""перемещает отработавший файл в dump"""

import os
import time
class Pickers:
    path_media = os.environ['PATH_1']
    path_dump= os.environ['PATH_2']
    def _get_names_or_extension(self, type, list_of_files):
        file = list_of_files.split(".")
        if type== 'name':
            names=[]
            names.append(file[0])
            return names
        elif type=='extension':
            extensions = []
            extensions.append(file[1])
            return extensions

    def _change_name(self, list_of_files, type=True):
        names = self._get_names_or_extension('name', list_of_files)
        extensions=self._get_names_or_extension('extension', list_of_files)
        names_new = []
        if type:
            for i in range(len(names)):
                names_new.append(names[i] + str(time.time())+'.'+str(extensions[i]))
            return names_new
        else:
            for i in range(len(names)):
                names_new.append(names[i]+'.'+str(extensions[i]))
            return names_new

    def move_to_dump (self, list_of_files):
        new_path=[]
        old_path=[]
        for name in self._change_name(list_of_files):
            new_path.append(self.path_dump+str(name))

        for name in self._change_name(list_of_files ,False):
            old_path.append(self.path_media+str(name))

        for i in range(len(new_path)):
            os.replace(old_path[i], new_path[i])