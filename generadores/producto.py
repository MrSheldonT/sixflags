import json
from random import randrange
import datetime
import random

def random_date(start,l):
   current = start
   while l >= 0:
    current = current + datetime.timedelta(days=randrange(365))
    yield current
    l-=1

with open('producto.json', 'r', encoding="utf-8") as json_file:
    json_load = json.load(json_file)

data = json_load['PS']['P']

reemplazar = ['</b>', '\n', '<b>', '<div class =" "inpromo" ">', '<div class="inpromo">','?','</div>"', '</div>', '</li>', '<ul>', '<li>', '</ul>', '\xa0', "'"]

startDate = datetime.datetime(2023, 1, 1, 00, 00, 00)

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
    
    parque_id = []
    categories = []
    descs = []

    
    i = 0
    for x in data:

        match x['merchant_id']:
            case '54':
                parque_id.append(1)
            case '60':
                parque_id.append(2)
        
        match x['package_class']:
            case 'Season Pass - New':
                categories.append(1)
            case 'Daily Tickets':
                categories.append(2)
            case 'Membership Dining':
                categories.append(3)
            case 'Meal Vouchers':
                categories.append(3)
            case 'Season Dining':
                categories.append(3)
            case 'VIP Tours':
                categories.append(5)
            case 'Group Tickets':
                categories.append(6)
            case 'Memberships':
                categories.append(11)
            case 'Annual Pass - Flex':
                categories.append(12)
            case 'Cabanas':
                categories.append(13)
            case _:
                categories.append(10)

        
        raw_descs = [x['desc']]
        for desc in raw_descs:
            temp_desc = desc
            for str in reemplazar:
                temp_desc = temp_desc.replace(str, ' ')
            descs.append(temp_desc)
        
        fechas = list(random_date(startDate, 2))

        file.write(f'''   , ('{x['id']}', {categories[i]} , {parque_id[i]}, '{x['name'].replace('?', '')}', '{descs[i]}', {x['min_retail_amount']}, '{fechas[0].strftime("%y/%m/%d %H:%M:%S")}', '{fechas[1].strftime("%y/%m/%d %H:%M:%S")}', {random.randint(0,1)}, {random.randint(0, 1500)}, {x['min_quantity']})\n''')
        i += 1
    file.write(';')