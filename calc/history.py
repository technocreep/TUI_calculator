'''
This module creates historical log of math operations.
The data is stored in form of dictionary where
the key is date-time and value is math expression.
The functions to read and delete log file are provided.

The log file 'logs.json' is created automatically when first operation is done.
To observe actual history log it is required to press OK-button on the
history page.
'''

import json
import datetime
import os
from pandas import DataFrame as pd_df


def log_create(a_num, b_num, oper, result):
    '''Creates a log file .json'''
    today = datetime.datetime.today()
    date_time = str(today.strftime("%Y-%m-%d-%H.%M.%S"))

    data = {}

    if os.path.isfile('logs.json'):             # файл имеется
        with open('logs.json', 'r') as json_file:           # читаем
            data = json.load(json_file)
        with open('logs.json', 'w') as json_file:
            # дополняем
            data[date_time] = f'{a_num}{oper}{b_num}={result}'
            json.dump(data, json_file, indent=2)              # записываем

    else:                                       # файла нет
        # создаем словарь
        data = {date_time: f'{a_num}{oper}{b_num}={result}'}
        with open('logs.json', 'w') as json_file:             # записываем в файл
            json.dump(data, json_file, indent=2)


def log_read():
    '''Function to read file in case of its presence'''

    if os.path.isfile('logs.json'):

        with open('logs.json', 'r') as json_file:
            data_read = json.load(json_file)
        # create datagrame from dictionary
        data_frame = pd_df(data_read.items(), columns=['Date-Time', 'Expression'])

        return str(data_frame)

    return None


def log_del():
    '''Function deletes log file at once.'''
    if os.path.isfile('logs.json'):
        os.remove('logs.json')
        return 'Log file has been deleted'

    return 'There is no log file'
