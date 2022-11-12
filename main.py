# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

import data_provider as dp
import csv_creater as cs
import json_creater as js
import show_menu as sh
import search
#cs.create_table()

work_list = \
{
    'ID': ['1','2','3','4','5'],
    'last_name' : ['Алексеев','Иванов','Петров','Сидоров','Яковлев'],
    'first_name': ['Алексей','Иван','Петр','Сергей','Яков'],
    'position': ['Директор', 'Бухгалтер', 'Секретарь', 'Менеджер', 'Инженер'],
    'phone_number' : ['+79991234567','+79992345678','+79883456789','+79774567890','+79660987654'],
    'salary' : ['1000000','500000','250000','125000','62500']
}

if sh.show_menu() == 1:
    print(search.search_surname(input('Введите фамилию для поиска')))
elif sh.show_menu() ==  2:
    print(search.search_position(input('Введите должность')))
elif sh.show_menu() == 3:
    data = dp.data_collection()
    cs.write_csv(data)
    js.write_json(data)
elif sh.show_menu() == 4:
    search.delete_employee(input('Введите фамилию сотрудника для удаления'))
elif sh.show_menu() == 5:
    search.update_employee(input('Введите фамилию сотрудника для обновления информации'))


    



#    print(cs.read_csv_text())
#elif sh.show_menu() == 2:

#print(cs.read_csv())
#
#print(js.read_json())
#print(js.read_json())
#elif sh.show_menu() == 3:
 #   tx.create_txt()
#else:
 #   print('Перезапустите программу, такого пункта в меню нет')