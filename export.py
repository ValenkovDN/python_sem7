import os
import csv
def exp_data():
    if not os.path.exists('notephone.csv'):
        with open("notephone.csv", mode="w", encoding='utf-8') as np:
            heading = csv.writer(np, delimiter=';')
            heading.writerow(["Surname", "Name", "Number", 'Comment'])
    exit = ''
    while exit != 'q':
        users_data = [
            [input('Фмилия: '), input('Имя: '), input('Телефон: '), input('Комментарий: ')]
        ]
        with open("notephone.csv", mode="a", encoding='utf-8') as np:
            heading = csv.writer(np, delimiter=';')
            heading.writerows(
                users_data
            )
        exit = input('Для завершения работы нажмите "q"\n Для продолжения работы  нажмите "Enter"\n')
