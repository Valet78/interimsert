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
            print()

            #show_all(current_dict)           
           
        case 2:             # Просмотреть записи за последний месяц.
            print()
            show_sotr(current_dict)             

        case 3:             # Просмотреть все записи.
            add_dict = add_sotr()
            current_dict.update(add_dict)
            save_data('base.csv', current_dict)        

        case 4:             # Добавить запись.
            res_keys = del_sotr(current_dict)
            if res_keys != '0':
                list_del = [res_keys, current_dict[res_keys]['Имя Фамилия'], current_dict[res_keys]['номер телефона'],
                            current_dict[res_keys]['подразделение'], current_dict[res_keys]['должность'], current_dict[res_keys]['e-mail']]
                
            add_data('archive.csv', list_del)
            del current_dict[res_keys]
            save_data('base.csv', current_dict)          
        
        case 5:             # Импорт данных из файла.
            res_imp = file_in_name('Введите имя файла для импорта: ')
            add_dict = load_data(res_imp)
            current_dict.update(add_dict)
            save_data('base.csv', current_dict)            
            
        case 6:             # Экспорт данных в файл.
            res_exp = file_in_name('Введите имя файла для экспорта: ')            
            save_data(res_exp, current_dict) 
            print('Экспорт данных выполнен.')    

        case 7:             # Удалить запись.

            print()
        
        case 0:
            print('\nПрограмма будет закрыта. Удачи Вам!\n')
            do_it = False
