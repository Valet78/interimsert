# Работа с файлами
from csv import *
from os import getcwd #, path


PATHFILE = getcwd() + '\\' 


def load_data(name_f: str) -> dict[str,dict[str, str]]:             # Чтение всех данных 
    name_f = PATHFILE + name_f
    res_dict = {}
    try:        
        with open(name_f, mode='r', encoding='utf-8') as file:
            reader = DictReader(file, delimiter=";")
            for i in reader:
                res_dict[i['Id']] = {'Заголовок':i['Заголовок'], 'Заметка':i['Заметка'], 'Дата_исполнения':i['Дата_исполнения']}                
            return res_dict
           
    except FileNotFoundError:        
        return res_dict           
    

def save_data(name_f: str, in_dict: dict[str,dict[str, str]]):      # Экспорт всех данных
    name_f = PATHFILE + name_f
        
    with open(name_f, mode='w', encoding='utf-8') as file:
        names = ['Id', 'Заголовок', 'Заметка', 'Дата_исполнения']
        file_writer = DictWriter(file, lineterminator="\r", fieldnames=names, delimiter=";") 
        file_writer.writeheader()
        for i  in in_dict.keys():
            file_writer.writerow({'Id':i, 'Заголовок':in_dict[i]['Заголовок'], 'Заметка':in_dict[i]['Заметка'],
                                'Дата_исполнения':in_dict[i]['Дата_исполнения']})



if __name__ == '__main__':
    
    dict_txt = {'00001': {'Заголовок':'Иванов Сергей', 'Заметка':'авваппвапвп', 'Дата_исполнения':'13122003'},
                '00002': {'Заголовок':'Петрик Николай', 'Заметка': '2кснпоошшпнпв', 'Дата_исполнения':'15122010'}}
        
    # save_data('base.csv', dict_txt)
    # load_data('base.csv') 