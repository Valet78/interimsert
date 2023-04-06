# Работа с файлами
from csv import *
from os import getcwd
PATHFILE = getcwd() + '\\sem_8\\'


def load_data(name_f: str) -> dict[str,dict[str, str]]:                           # Чтение всех данных 
    name_f = PATHFILE + name_f
    res_dict = {}
    try:        
        with open(name_f, mode='r', encoding='utf-8') as file:
            reader = DictReader(file)
            for i in reader:
                res_dict[i['Id']] = {'Имя Фамилия':i['Имя Фамилия'], 'номер телефона':i['номер телефона'],
                                'подразделение':i['подразделение'], 'должность':i['должность'], 'e-mail':i['e-mail']}                
            return res_dict
           
    except FileNotFoundError:        
        return res_dict           


def add_data(name_f: str, in_txt: list[str]):                       # Добавление строки 
    name_f = PATHFILE + name_f
    try:
        with open(name_f, mode='a', encoding='utf-8', newline='\r') as file:
                names = ['Id', 'Имя Фамилия', 'номер телефона', 'подразделение', 'должность', 'e-mail']
                file_writer = DictWriter(file, lineterminator="\r", fieldnames=names) 
                file_writer.writeheader()
                file_writer.writerow({'Id':in_txt[0], 'Имя Фамилия':in_txt[1], 'номер телефона':in_txt[2],
                                    'подразделение':in_txt[3], 'должность':in_txt[4], 'e-mail':in_txt[5]})   
    except FileNotFoundError:
        with open(name_f, mode='w', encoding='utf-8', newline='\r') as file:
                names = ['Id', 'Имя Фамилия', 'номер телефона', 'подразделение', 'должность', 'e-mail']
                file_writer = DictWriter(file, lineterminator="\r", fieldnames=names) 
                
                file_writer.writerow({'Id':in_txt[0], 'Имя Фамилия':in_txt[1], 'номер телефона':in_txt[2],
                                    'подразделение':in_txt[3], 'должность':in_txt[4], 'e-mail':in_txt[5]})          


def save_data(name_f: str, in_dict: dict[str,dict[str, str]]):      # Экспорт всех данных
    name_f = PATHFILE + name_f
    with open(name_f, mode='w', encoding='utf-8') as file:
        names = ['Id', 'Имя Фамилия', 'номер телефона', 'подразделение', 'должность', 'e-mail']
        file_writer = DictWriter(file, lineterminator="\r", fieldnames=names) 
        file_writer.writeheader()
        for i  in in_dict.keys():
            file_writer.writerow({'Id':i, 'Имя Фамилия':in_dict[i]['Имя Фамилия'], 'номер телефона':in_dict[i]['номер телефона'],
                                'подразделение':in_dict[i]['подразделение'], 'должность':in_dict[i]['должность'], 'e-mail':in_dict[i]['e-mail']})
            






if __name__ == '__main__':
    
    dict_txt = {'00001': {'Имя Фамилия':'Иванов Сергей', 'номер телефона':'234-01', 'подразделение':'технический', 'должность':'начальник отдела', 'e-mail':'xcv@nail.ru'},
                '00002': {'Имя Фамилия':'Петрик Николай', 'номер телефона': '233-02', 'подразделение':'бухгалтерия', 'должность':'бухгалтер', 'e-mail':'sdf@nail.ru'}}
    list_txt = ['00002', 'Сергеев Дмитрий', '231-04', 'технический', 'техник', 'sdfix@nail.ru']
    
    # save_data('base.csv', dict_txt)
    # add_data('base.csv', list_txt)
    load_data('base.csv') 