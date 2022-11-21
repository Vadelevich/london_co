#!/usr/bin/env python3

def print_by_key(london_co):
    key = input('Введите имя усройства :')
    new_values = [ x for x in london_co[key].keys()]
    new_values = ','.join(new_values)
    values = input(f'Введите имя параметра ({new_values}) :').lower()
    if values  not in new_values :print ('Такого параметра нет')
    else :print(london_co[key][values])

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

print_by_key(london_co)
