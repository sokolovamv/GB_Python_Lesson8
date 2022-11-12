import json_creater as js
import csv_creater as cs
import data_provider as dt

# поиск по сотруднику
def search_surname(surname):
    list_of_surname = []
    data = js.read_json()
    for dict in data:
        if surname in dict.values():
            list_of_surname.append(dict)
    return list_of_surname

# Сделать выборку сотрудников по должности
def search_position(position):
    list_of_position = []
    data = js.read_json()
    for dict in data:
        if position in dict.values():
            list_of_position.append(dict)
    return list_of_position

# Удалить сотрудника
def delete_employee(surname):
    data = js.read_json()
    for i in range(len(data)):
        if surname in data[i].values():
            del data[i]
    js.write_json_w(data)
    cs.write_csv_w(data)


# обновить информацию сотрудника
def update_employee(surname):
    data = js.read_json()
    for dict in data:
        if surname in dict.values():
            dict.update(id = dt.get_id(), last_name = dt.get_surname(), \
                first_name = dt.get_name(), position = dt.get_position(), \
                phone_number = dt.get_phone_number(), salary = dt.get_salary())
    js.write_json_w(data)
    cs.write_csv_w(data)