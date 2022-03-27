#Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
import os


with open('config.yaml', 'r') as fr:
    for row in fr:
        if str(row)[-2] == '/':
            if not os.path.exists(row.rstrip()):
                os.makedirs(row.rstrip())

        else:
            if not os.path.exists(row.rstrip()):
                f = open(row.rstrip(), "x")
                f.close
