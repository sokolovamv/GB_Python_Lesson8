# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

import data_provider as dp
import csv_creater as cs
import json_creater as js
import show_menu as sh
import search

if sh.show_menu() == 1:
    print(search.search_surname(input('Введите фамилию для поиска: ')))
elif sh.show_menu() ==  2:
    print(search.search_position(input('Введите должность: ')))
elif sh.show_menu() == 3:
    data = dp.data_collection()
    cs.write_csv(data)
    js.write_json(data)
elif sh.show_menu() == 4:
    search.delete_employee(input('Введите фамилию сотрудника для удаления: '))
elif sh.show_menu() == 5:
    search.update_employee(input('Введите фамилию сотрудника для обновления информации: '))
else: 
    print('Перезапустите программу и введите праильную цифру из меню')