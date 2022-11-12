import csv_creater as csv

# создать текстовый файл из csv
def create_txt(): 
    file_txt = 'Phonebook.txt'   
    with open(file_txt, 'w', encoding = 'utf-8') as file_txt:
        file_txt.write(csv.read_csv_text())
    