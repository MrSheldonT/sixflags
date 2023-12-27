import json
import random

random.seed(1)
with open('producto.json', 'r', encoding="utf-8") as json_file:
    json_load = json.load(json_file)

data = json_load['PS']['P']

reemplazar = ['</b>', '\n', '<b>', '<div class =" "inpromo" ">', '<div class="inpromo">','?','</div>"', '</div>', '</li>', '<ul>', '<li>', '</ul>', '\xa0', "'", "Nat'l", '<i>', '</i>', '<font style="color: red;">', '<br>', '</font>', '</br>', '</u>', '<u>', '<b', '<a href="', '" target="_blank">', '</a>', '<FONT COLOR="#ff0000">', '<s>', '</s>', '</FONT>', '<a href=', '<p', '<div class = "inpromo"', '<div class = "inpromo inpromo2"', '<ul',  '<li class = "Featured"', '</p', '/ p', '<div class = "" inpromo inpromo2 ""', '<li class = "" aparece ""', '<li class = "" Featured ""', '<div class="inpromo inpromo2"', '<li class="featured"', '>']

categorias = {
   'Season Pass - New' : 1
   , 'Annual Pass - Flex' : 1
   , 'Daily Tickets' : 2
   , 'Membership Dining' : 3
   , 'Meal Vouchers' : 3
   , 'Season Dining' : 3
   , 'VIP Tours' : 4
   , 'Group Tickets' : 5
   , 'Memberships' : 6
   , 'Cabanas' : 7
   , 'Parking Vouchers': 8
   , 'Bundles' : 9
}

parques = {
    '54' : 1
    , '60' : 2
}

with open('producto.sql', 'w', encoding = 'utf-8') as file:
    file.write('''INSERT INTO producto
VALUES
''')

    for x in data:
        # desc
        desc = x['desc']
        try:
            info = (x['more_info'])
        except KeyError:
            info = ('')

        for str in reemplazar:
            desc = desc.replace(str, ' ')
            info = info.replace(str, ' ')
        desc = desc + info

        # fechas
        if int(x['id']) <= 10092967:
            fechas = ('2020-01-01 00:00:00', '2021-12-31 11:59:59')
        elif int(x['id']) <= 10104617:
            fechas = ('2022-01-01 00:00:00', '2022-12-31 11:59:59')
        else:
            fechas = ('2023-01-01 00:00:00', '2023-12-31 11:59:59')

        file.write(f'''   , ({x['id']}, {categorias.get(x['package_class'], 10)}, {parques.get(x['merchant_id'], 3)}, '{x['name'].replace('?', '').replace("'", '')}', '{desc}', {x['min_retail_amount']}, '{fechas[0]}', '{fechas[1]}', {random.randint(0,1)}, {random.randint(0, 1500)}, {x['min_quantity']})\n''')
    file.write(';')