def get_id():
    flag = False
    while not flag:
        id = input("Введите id: ")
        if id.isdigit():
            flag = True   
        else:
            print('Пожалуйста, введите id в правильном формате')
    return id

# ввод фамилии с проверкой
def get_surname():
    surname = input("Введите фамилию: ")
    while not surname.isalpha():
        surname = input("Введите фамилию: ")
    return surname

# ввод имени с проверкой
def get_name():
    name = input("Введите имя: ")
    while not name.isalpha():
        name = input("Введите имя: ")
    return name
    
# ввод должности
def get_position():
    name = input("Введите должность: ")
    while not name.isalpha():
        name = input("Введите должность: ")
    return name

# ввод номера с проверкой
def get_phone_number():
    flag = False
    while not flag:
        phone_number = input("Введите номер телефона без кода страны (10 символов): ")
        if phone_number.isdigit() and len(phone_number) == 10:
            flag = True   
        else:
            print('Пожалуйста, введите номер телефона в правильном формате')
    return '+7' + phone_number

# ввод зарплаты
def get_salary():
    flag = False
    while not flag:
        salary = input("Введите зарплату сотрудника: ")
        if salary.isdigit():
            flag = True   
        else:
            print('Пожалуйста, введите зарплату в правильном формате')
    return salary

def data_collection():
    temp = {}
    employee = []
    temp['id'] = get_id()
    temp['last_name'] = get_surname()
    temp['first_name'] = get_name()
    temp['position'] = get_position()
    temp['phone_number'] = get_phone_number()
    temp['salary'] = get_salary()
    employee.append(temp)
    return employee