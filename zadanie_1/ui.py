# Работа с пользователем

from datetime import datetime as dt
from datetime import timedelta as dt_delta



def action_id() -> int:                 # Вывод запроса действий
    try:
        print()
        print('Заметки для личного пользования.')
        print('Вы можете выполнить следующие действия:')
        print('1. Просмотреть записи за последнюю неделю.')
        print('2. Просмотреть записи за последний месяц.')
        print('3. Просмотреть все записи.')
        print('4. Добавить запись.')
        print('5. Удалить запись.')   
        print('________________________')
        print('0. Завершить программу.')
        id_action = int(input('\n Введите необходимое действие: '))
        while id_action not in [1, 2, 3, 4, 5, 0]:
            print('Вы ввели некорректные данные. Будьте внимательны.')
            raise ValueError
        else: return id_action

    except ValueError:
        print('Выбрать можно только указанные действия. Попробуйте снова.')
        action_id()


def show_all(in_dict: dict[str,dict[str, str]]):            # Вывод свсех записей
    for ii in in_dict.keys():
        print('Заметка id=', ii, ' "', in_dict[ii]['Заголовок'], '":\n')
        print('\t"', in_dict[ii]['Заметка'] , '"\n')


def show_time(in_dict: dict[str,dict[str, str]], in_time: int):           # Вывод списка за неделю
    date_before = dt.now() - dt_delta(in_time)
    id_before = str(date_before.year)
    id_before += sel(date_before.month)
    id_before += sel(date_before.day)
    id_before+='0000'
    
    for ii in in_dict.keys():
        if int(ii) > int(id_before):
            print('Заметка id=', ii, ' "', in_dict[ii]['Заголовок'], '":\n')
            print('\t"', in_dict[ii]['Заметка'] , '"\n')


def add_zap() -> dict[str,dict[str, str]]:                              # Добавление новой записи
    id = ''
    res_dict = {}
    print('Вы хотите добавить новую заметку, введите данные...')
    in_head = input('Заголовок заметки: ')
    in_body = input('Текст заметки: ')
    in_expdate = input('Срок (дата) исполнения (день.месяц.год): ')
    
    while in_head == '':
        print('Вы забыли ввести обязательный параметр "Заголовок заметки". Пробуем снова.')
        in_head = input('Заголовок заметки: ')
    
    good_exp = valid_date(in_expdate)                               # Правильно записанная дата
    while  good_exp =='-1':
        print('Выявлена ошибка ввода контрольной даты. Будбте внимательнее и попробуйте снова.')
        in_expdate = input('Срок (дата) исполнения (день.месяц.год): ')
        good_exp = valid_date(in_expdate)

    id = valid_id()
    res_dict[id] = {'Заголовок':in_head, 'Заметка':in_body, 'Дата_исполнения': good_exp, 'Статус':'активно'}
  
    return res_dict


def valid_date(date_txt: str) -> str:                                  # Проверка правильности ввода контрольной даты 
    rez = ''
    try:
        in_date = date_txt.split('.') 
        int_day = int(in_date[0])
        int_month = int(in_date[1])
        int_year = int(in_date[2])

        if int_day > 0 and int_month > 0 and int_year > 0:
            if int_month > 12 or int_year > 9999:
                return '-1'
            else:
                if int_month in [1, 3, 5, 7, 8, 10, 12] and int_day > 31:
                    return '-1'
                elif int_month in [4, 6, 9, 11] and int_day > 30:
                    return '-1'
                elif (int_month == 2 and int_year%4 == 0) and int_day > 29:
                    return '-1'
                elif (int_month == 2 and int_year%4 != 0) and int_day > 28:
                    return '-1'
                else:
                    rez = ''.join([in_date[2], in_date[1], in_date[0]])
                    return  rez

        else:
            return '-1'        
    
    except ValueError:
        return '-1'
    
    
def valid_id() -> str:
    time = dt.now()
    int_day = time.day
    int_month = time.month
    int_year = time.year
    int_hour = time.hour
    int_minute = time.minute
    
    rez = str(int_year)
    rez += sel(int_month)
    rez += sel(int_day)
    rez += sel(int_hour)
    rez += sel(int_minute)
    
    return rez
    

def sel(tt: int) -> str:
    res = ''
    if tt < 10:
        res = '0' + str(tt)
    else:
        res = str(tt)
    return res








def del_sotr(in_dict: dict[str,dict[str, str]]) -> str:         # Удаление пользователя
    num = 0
    del_txt = input('Введите Фамилию и Имя сотрудника, которого Вы хотите удалить: ')
    while del_txt == '':
        print('Вы забыли ввести данные.')
        del_txt = input('Введите Фамилию и Имя сотрудника, которого Вы хотите удалить: ')
    
    for keys, val in in_dict.items():
        if del_txt in val['Имя Фамилия']:
            num += 1
            return keys            
    if num == 0: 
        print('Сотрудник с такими данными не обнаружен.')
        return str(num)     



""" 

def file_in_name(text: str) -> str:
    in_txt = input(text)
    while in_txt == '':
        print('Вы забыли ввести данные.')
        in_txt = input(text)
    in_txt += '.csv'
    return in_txt
 """



if __name__ == '__main__':
    print(valid_date('02.11.2023'))