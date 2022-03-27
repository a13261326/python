#Ищет в папке my_project папки Templates(Шаблоны) и копирует их содержимое в папку List_template


import os
import shutil
import os.path
from os import walk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f'Корневая директория нашего проекта - {BASE_DIR}')
list_template = os.path.join(BASE_DIR, 'templates_list')
if not os.path.exists(list_template):
    os.mkdir(list_template)

project_folder = os.path.join(BASE_DIR, 'my_project')
for (dirpath, dirnames, filenames) in walk(project_folder):
    for i in dirnames:
        if i == 'templates' or i == 'Templates' or i == 'TEMPLATES':
            h = str(dirpath).split("\\")[-1]
            #ff = os.path.join(str(dirpath), str(i))
            new_dir_template = f'{os.path.join(list_template, h)}_Template'
            if not os.path.exists(new_dir_template):
                os.mkdir(new_dir_template)
            for item in os.listdir(os.path.join(str(dirpath), str(i))):
                from_file = os.path.join(str(os.path.join(str(dirpath), str(i))), str(item))
                to_file = os.path.join(new_dir_template, str(item))
                shutil.copyfile(from_file, to_file)