import data_provider as prov
# ввод информации
def surname_view():
    data = prov.get_surname()
    return data

def name_view():
    data = prov.get_name()
    return data

def position_view():
    data = prov.get_position()
    return data


def phone_number_view():
    data = prov.get_phone_number()
    return data

def description_view():
    data = prov.get_description()
    return data