# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#

# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
# под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о
# вложенных папках и файлах (добавлять детали)?
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os


dirs = ('settings', 'mainapp', 'mainapp', 'adminapp', 'authapp', 'testdir')
# в списке меняем именя, количество и т.д
for d in dirs:
    dir_path = os.path.join('DZ7/my_project', d)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

for dirpath, dirnames, filenames in os.walk('DZ7/my_project'):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
        # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))

