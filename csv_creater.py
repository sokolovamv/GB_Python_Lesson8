import csv
from pathlib import Path

# чтение csv
def read_csv() -> list:
    employee = []
    with open(Path.cwd()/'database.csv','r',encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp['id'] = int(row[0])
            temp['last_name'] = row[1]
            temp['first_name'] = row[2]
            temp['position'] = row[3]
            temp['phone_number'] = row[4]
            temp['salary'] = float(row[5])
            employee.append(temp)
    return employee

# дозапись в csv
def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'a', encoding = 'utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())

# запись в csv
def write_csv_w(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding = 'utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())