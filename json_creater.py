import json
from pathlib import Path

# 
def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding = 'utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'a', encoding = 'utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')

def write_json_w(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding = 'utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')
