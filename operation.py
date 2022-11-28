import view
import export
import impotr
import logger

def butten_clik():
    temp = view.start()
    while temp != 'q':
        logger.log(temp)
        if temp == '1':
            export.exp_data()
        elif temp == '2':
            search = input('Для поиска по фамилии введите "1" \n Для поиска по имени введите "2"\n Для поиска по номеру телефона введите "3"\n')
            if search == '1': impotr.find_surname(input('Фамилия: '))
            if search == '2': impotr.find_name(input('Имя: '))
            if search == '3': impotr.find_phone(input('Номер телефона: '))
        temp = view.start()
    

butten_clik()