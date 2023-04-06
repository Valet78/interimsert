# Работа с пользователем
from datetime import datetime as dt

def action_id() -> int:                 # Вывод запроса действий
    try:
        print()
        print('Заметки для личного пользования.')
        print('Вы можете выполнить следующие действия:')
        print('1. Просмотреть записи за последнюю неделю.')
        print('2. Просмотреть записи за последний месяц.')
        print('3. Просмотреть все записи.')
        print('4. Добавить запись.')
        print('5. Импорт данных из файла.')
        print('6. Экспорт данных в файл.')     
        print('7. Удалить запись.')   
        print('________________________')
        print('0. Завершить программу.')
        id_action = int(input('\n Введите необходимое действие: '))
        while id_action not in [1, 2, 3, 4, 5, 6, 7, 0]:
            print('Вы ввели некорректные данные. Будьте внимательны.')
            raise ValueError
        else: return id_action

    except ValueError:
        print('Выбрать можно только указанные действия. Попробуйте снова.')
        action_id()


def show_all(in_dict: dict[str,dict[str, str]]):            # Вывод сотрудником подразделения
    num = 1
    seach_data = input('Введите название отдела/подразделения: ')
    while seach_data == '':
        print('Вы забыли ввести данные.')
        seach_data = input('Введите название отдела/подразделения: ')
        
    for ii in in_dict.keys():
        if seach_data in in_dict[ii]['подразделение']:
            print(num, '. ', in_dict[ii]['Имя Фамилия'], '\t') 
            num += 1           
    if num == 1: print('Не существует такого подразделения или сотрудники в нём не числятся.')


def show_sotr(in_dict: dict[str,dict[str, str]]):
    num = 0
    seach_data = input('Введите через пробел Фамилию и Имя искомого сотрудника: ')
    while seach_data == '':
        print('Вы забыли ввести данные.')
        seach_data = input('Введите название отдела/подразделения: ')

    for keys, val in in_dict.items():
        if seach_data in val['Имя Фамилия']:
            print('ID = ', keys, ':')
            print('\tФИ сотрудника: ',val['Имя Фамилия'])
            print('\tЗанимаемая должность: ', val['должность'])
            print('\tПодразделение: ', val['подразделение'])
            print('\tтел.:\t', val['номер телефона'])
            print('\tE-mail:\t', val['e-mail'])
            num += 1
    if num == 0: print('Сотрудник с такими данными не обнаружен.')                


def add_sotr() -> dict[str,dict[str, str]]:
    id, res_dict = '', {}
    print('Ведите данные сотрудника для добавления в базу')
    in_fi = input('Фамилия и имя (через пробел): ')
    in_podr = input('Подразделение: ')
    in_dol = input('Должность: ')
    in_tel = input('Телефон: ')
    in_mail = input('E-mail: ')

    while in_fi == '':
        print('Вы забыли ввести обязательный параметр "Фамилия и имя". Пробуем снова.')
        in_fi = input('Фамилия и имя (через пробел): ')
    
    time = dt.now()
    id = ''.join([str(time.year), str(time.month), str(time.day), str(time.hour), str(time.minute)])
    res_dict[id] = {'Имя Фамилия':in_fi, 'номер телефона':in_tel, 'подразделение':in_podr, 'должность':in_dol, 'e-mail':in_mail}

    return res_dict

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

def file_in_name(text: str) -> str:
    in_txt = input(text)
    while in_txt == '':
        print('Вы забыли ввести данные.')
        in_txt = input(text)
    in_txt += '.csv'
    return in_txt




if __name__ == '__main__':
    add_sotr()