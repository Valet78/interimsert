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
        print('5. Редактировать запись.')
        print('6. Удалить запись.')   
        print('________________________')
        print('0. Завершить программу.')
        id_action = int(input('\n Введите необходимое действие: '))
        while id_action not in [1, 2, 3, 4, 5, 6, 0]:
            print('Вы ввели некорректные данные. Будьте внимательны.')
            raise ValueError
        else: return id_action

    except ValueError:
        print('Выбрать можно только указанные действия. Попробуйте снова.')
        action_id()


def show_all(in_dict: dict[str,dict[str, str]]):            # Вывод свсех записей
    for ii in in_dict.keys():
        print('Заметка id=', ii, ' "', in_dict[ii]['Заголовок'], '": "', in_dict[ii]['Заметка'] , '"\t', 'Срок до ', rev_date(in_dict[ii]['Дата_исполнения']))


def get_id(in_dict: dict[str,dict[str, str]]) -> str:
    list_str = []
    dict_id = {}
    nom_str = 1
    try:
        for ii in in_dict.keys():
            print(nom_str, '. Заметка от ', rev_date(ii), '"', in_dict[ii]['Заголовок'], '": "', in_dict[ii]['Заметка'] , '"')
            dict_id[nom_str] = ii
            list_str.append(nom_str)
            nom_str += 1
        id_action = int(input('\n Введите номер записи, которую Вы желаете отредактировать или удалить: '))
        while id_action not in list_str:
            print('Вы ввели некорректные данные. Будьте внимательны.')
            raise ValueError
        else: 
            return dict_id[id_action]
    
    except ValueError:
        print('Выбрать можно только имеющиеся строки. Попробуйте снова.\n')
        get_id(in_dict)


def show_time(in_dict: dict[str,dict[str, str]], in_time: int):           # Вывод списка за неделю
    date_before = dt.now() - dt_delta(in_time)
    id_before = str(date_before.year)
    id_before += sel(date_before.month)
    id_before += sel(date_before.day)
    id_before+='0000'
    
    for ii in in_dict.keys():
        if int(ii) > int(id_before):
            print('Заметка id=', ii, ' "', in_dict[ii]['Заголовок'], '": "', in_dict[ii]['Заметка'] , '"\t',  'Срок до ', rev_date(in_dict[ii]['Дата_исполнения']))


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
    res_dict[id] = {'Заголовок':in_head, 'Заметка':in_body, 'Дата_исполнения': good_exp}
  
    return res_dict


def edit_zap(id: str, in_dict: dict[str,dict[str, str]]) -> dict[str,dict[str, str]]:
    try:
        print()
        print("Итак, укажите, что именно Вы желаете изменить:")
        print('1. Заголовок')
        print('2. Заметку')
        print('3. Сроки исполнения')
        print('________________________')
        id_action = int(input('\n Введите необходимое действие: '))
        while id_action not in [1, 2, 3]:
            print('Вы ввели некорректные данные. Будьте внимательны.')
            raise ValueError
        else: 
            print('Вы решили изменить следующую заметку:')
            print('Заметка id=', id, ' "', in_dict[id]['Заголовок'], '": "', in_dict[id]['Заметка'] , '"\t',  'Срок до ', rev_date(in_dict[id]['Дата_исполнения']), '\n')
            match id_action:
                case 1:
                    new_txt = input('Введите новое название заметки: ')
                    in_dict[id]['Заголовок'] = new_txt
                case 2:
                    new_txt = input('Введите новое значение заметки: ')
                    in_dict[id]['Заметка'] = new_txt
                case 3:
                    new_txt = input('Введите новое значение срока (день.месяц.год): ')
                    good_exp = valid_date(new_txt)  
                    while  good_exp =='-1':
                        print('Выявлена ошибка ввода контрольной даты. Будбте внимательнее и попробуйте снова.')
                        in_expdate = input('Введите новое значение срока (день.месяц.год): ')
                        good_exp = valid_date(in_expdate)

                    in_dict[id]['Заметка'] = good_exp
            
            return in_dict

    except ValueError:
        print('Выбрать можно только указанные действия. Попробуйте снова.\n')
        edit_zap(id, in_dict)


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

def rev_date(in_txt: str) -> str:
    year = in_txt[0:4]
    month = in_txt[4:6]
    day = in_txt[6:8]

    return ''.join([day, '.', month, '.', year, ' г.'])

def del_str(ind_zap: str, in_dict: dict[str,dict[str, str]]) -> dict[str,dict[str, str]]:
    
    print('Заметка от ', rev_date(ind_zap), '"', in_dict[ind_zap]['Заголовок'], '": "', in_dict[ind_zap]['Заметка'] , '"')
    print('Будет удалена по Вашему запросу...')
    del in_dict[ind_zap]
    return in_dict


if __name__ == '__main__':
    # print(valid_date('02.11.2023'))
    print(rev_date('202312241255'))