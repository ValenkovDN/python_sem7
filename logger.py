from datetime import datetime as dt

def log(action):
    if action == '1':
        dat = 'record'
    elif action == '2':
        dat = 'read'
    time = dt.now().strftime('%H:%M:%S')
    with open('log.txt', 'a',encoding='utf=8') as rec:
        rec.write(f'{dat}, {time}\n')
