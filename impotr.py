import os
import csv
import view

def find_surname(surname):
    if os.path.exists('notephone.csv'):
        with open("notephone.csv", mode="r", encoding='utf-8') as np:
            reader = csv.reader(np)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if surname == item[0]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{surname} не найден(а)')
    else:
        view.answer('Файл не найден')

def find_name(name):
    if os.path.exists('notephone.csv'):
        with open("notephone.csv", mode="r", encoding='utf-8') as np:
            reader = csv.reader(np)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if name == item[1]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{name} не найден(а)')
    else:
        view.answer('Файл не найден')

def find_phone(phone):
    if os.path.exists('notephone.csv'):
        with open("notephone.csv", mode="r", encoding='utf-8') as np:
            reader = csv.reader(np)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if phone == item[2]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{phone} не найден(а)')
    else:
        view.answer('Файл не найден')