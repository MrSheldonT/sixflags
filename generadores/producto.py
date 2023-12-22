import json
import random
from random import randrange
import datetime

def random_date(start,l):
   current = start
   while l >= 0:
    current = current + datetime.timedelta(days=randrange(365))
    yield current
    l-=1

with open('producto.json', 'r', encoding="utf-8") as json_file:
    json_load = json.load(json_file)

data = json_load['PS']['P']

reemplazar = ['</b>', '\n', '<b>', '<div class =" "inpromo" ">', '<div class="inpromo">','?','</div>"', '</div>', '</li>', '<ul>', '<li>', '</ul>', '\xa0', "'", "Nat'l", '<i>', '</i>', '<font style="color: red;">', '<br>', '</font>', '</br>', '</u>', '<u>', '<b', '<a href="', '" target="_blank">', '</a>', '<FONT COLOR="#ff0000">', '<s>', '</s>', '</FONT>', '<a href=', '<p', '<div class = "inpromo"', '<div class = "inpromo inpromo2"', '<ul',  '<li class = "Featured"', '</p', '/ p', '<div class = "" inpromo inpromo2 ""', '<li class = "" aparece ""', '<li class = "" Featured ""', '<div class="inpromo inpromo2"', '<li class="featured"', '>']

startDate = datetime.datetime(2023, 1, 1, 00, 00, 00)

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
    file.write('''INSERT INTO producto(
    plu
    , categoria_producto_id
    , parque_id
    , nombre
    , descripcion
    , precio_unitario
    , fecha_inicio_venta
    , fecha_fin_venta
    , descontinuacion
    , stock
    , cantidad_minimo_compra
    )
VALUES
''')
    
    descs = []
    info = []

    i = 0
    for x in data:
        raw_descs = [x['desc']]
        try:
            info.append(x['more_info'])
        except KeyError:
            info.append('')

        for desc in raw_descs:
            for str in reemplazar:
                desc = desc.replace(str, ' ')
                info[i] = info[i].replace(str, ' ')
            descs.append(desc + info[i])
        
        fechas = list(random_date(startDate, 2))

        file.write(f'''   , ('{x['id']}', {categorias.get(x['package_class'], 10)}, {parques.get(x['merchant_id'], 3)}, '{x['name'].replace('?', '').replace("'", '')}', '{descs[i]}', {x['min_retail_amount']}, '{fechas[0].strftime("%y/%m/%d %H:%M:%S")}', '{fechas[1].strftime("%y/%m/%d %H:%M:%S")}', {random.randint(0,1)}, {random.randint(0, 1500)}, {x['min_quantity']})\n''')
        i += 1
    file.write(';')