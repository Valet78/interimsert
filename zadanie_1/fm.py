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
                res_dict[i['Id']] = {'Заголовок':i['Заголовок'], 'Заметка':i['Заметка'], 'Дата_исполнения':i['Дата_исполнения'], 'Статус':i['Статус']}                
            return res_dict
           
    except FileNotFoundError:        
        return res_dict           

""" 
def add_data(name_f: str, in_txt: list[str]):                       # Добавление строки 
    name_f = PATHFILE + name_f
    is_file = path.isfile(name_f)    
    with open(name_f, mode='a', encoding='utf-8', newline='\r') as file:
        names = ['Id', 'Заголовок', 'Заметка', 'Дата_исполнения', 'Статус']
        file_writer = DictWriter(file, lineterminator="\r", fieldnames=names, delimiter=";") 
        if is_file==False: 
            file_writer.writeheader()            

        file_writer.writerow({'Id':in_txt[0], 'Заголовок':in_txt[1], 'Заметка':in_txt[2],
                            'Дата_исполнения':in_txt[3], 'Статус':in_txt[4]})   
     """
    

def save_data(name_f: str, in_dict: dict[str,dict[str, str]]):      # Экспорт всех данных
    name_f = PATHFILE + name_f
        
    with open(name_f, mode='w', encoding='utf-8') as file:
        names = ['Id', 'Заголовок', 'Заметка', 'Дата_исполнения', 'Статус']
        file_writer = DictWriter(file, lineterminator="\r", fieldnames=names, delimiter=";") 
        file_writer.writeheader()
        for i  in in_dict.keys():
            file_writer.writerow({'Id':i, 'Заголовок':in_dict[i]['Заголовок'], 'Заметка':in_dict[i]['Заметка'],
                                'Дата_исполнения':in_dict[i]['Дата_исполнения'], 'Статус':in_dict[i]['Статус']})





if __name__ == '__main__':
    
    dict_txt = {'00001': {'Заголовок':'Иванов Сергей', 'Заметка':'авваппвапвп', 'Дата_исполнения':'13122003', 'Статус':'нет'},
                '00002': {'Заголовок':'Петрик Николай', 'Заметка': '2кснпоошшпнпв', 'Дата_исполнения':'15122010', 'Статус':'сполнено'}}
    list_txt = ['00002', 'Сергеев Дмитрий', 'ddddddddddd', '12032012', 'активна']
    
    # save_data('base.csv', dict_txt)
    # add_data('base.csv', list_txt)
    # load_data('base.csv') 