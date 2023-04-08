from fm import *
from ui import *
from os import system

clear = lambda: system('CLS')
current_dict = load_data('base.csv')

if len(current_dict) == 0:
    print('Программа не может найти файл с данными и будет завершена.\n')
    do_it = False
else: do_it = True

while do_it:
    match (action_id()):
        case 1:             # Просмотреть записи за последнюю неделю.
            clear()
            show_time(current_dict, 7) 
           
        case 2:             # Просмотреть записи за последний месяц.
            clear()
            show_time(current_dict, 30)            

        case 3:             # Просмотреть все записи.
            clear()
            show_all(current_dict)

        case 4:             # Добавить запись.
            clear()
            add_txt = add_zap()
            current_dict.update(add_txt)
            save_data('base.csv', current_dict)   

        case 5:             # Редактирование записи
            clear()
            id_str = get_id(current_dict)
            clear()
            current_dict = edit_zap(id_str, current_dict)
            save_data('base.csv', current_dict) 

        
        case 6:             # Удалить запись.
            clear()
            id_str = get_id(current_dict)
            clear()
            current_dict = del_str(id_str, current_dict)
            save_data('base.csv', current_dict) 
                        
        
        case 0:
            clear()
            print('\nПрограмма будет закрыта. Удачи Вам!\n')
            do_it = False
            