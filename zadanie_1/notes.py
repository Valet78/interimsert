from fm import *
from ui import *



current_dict = load_data('base.csv')

if len(current_dict) == 0:
    print('Программа не может найти файл с данными и будет завершена.\n')
    do_it = False
else: do_it = True

while do_it:
    match (action_id()):
        case 1:             # Просмотреть записи за последнюю неделю.
            show_time(current_dict, 7) 
           
        case 2:             # Просмотреть записи за последний месяц.
            show_time(current_dict, 30)            

        case 3:             # Просмотреть все записи.
            show_all(current_dict)

        case 4:             # Добавить запись.
            add_txt = add_zap()
            # add_data('base.csv', add_txt)
            current_dict.update(add_txt)
            save_data('base.csv', current_dict)   
           
        
        case 5:             # Удалить запись.
            
            
            """ 
            res_keys = del_sotr(current_dict)
            if res_keys != '0':
                list_del = [res_keys, current_dict[res_keys]['Имя Фамилия'], current_dict[res_keys]['номер телефона'],
                            current_dict[res_keys]['подразделение'], current_dict[res_keys]['должность'], current_dict[res_keys]['e-mail']]
                
            add_data('archive.csv', list_del)
            del current_dict[res_keys]
            save_data('base.csv', current_dict)          """ 
            print()
        
        case 0:
            clear()
            print('\nПрограмма будет закрыта. Удачи Вам!\n')
            do_it = False
            