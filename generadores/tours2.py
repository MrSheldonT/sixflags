from faker import Faker
import random
from datetime import datetime, timedelta

Faker.seed(3)
fake = Faker('es_MX')

def convertir_a_24_horas(hora, am_pm):
    if am_pm.lower() == 'pm' and hora < 12:
        hora += 12
    elif am_pm.lower() == 'am' and hora == 12:
        hora = 0
    return hora

def generar_tours(size, fecha_inicio, fecha_fin, hora_inicio, am_pm_inicio, hora_fin, am_pm_fin):
    with open('tours2.sql', 'w', encoding='utf-8') as archivo_tours, open('parques.txt', 'w', encoding='utf-8') as archivo_parques:
        archivo_tours.write('''INSERT INTO tour(
    tour_id
    , parque_id
    , fecha_hora
    , no_visitantes
    , contacto_nombre
    , contacto_correo
    , contacto_telefono
)
VALUES 
''')
        tours = []  # Lista para almacenar las filas generadas

        # Convertir horas a formato de 24 horas
        hora_inicio_24 = convertir_a_24_horas(hora_inicio, am_pm_inicio)
        hora_fin_24 = convertir_a_24_horas(hora_fin, am_pm_fin)

        for i in range(size):
            dominio = random.choice(["@outlook.com", "@gmail.com", "@yahoo.com"])
            
            # Utilizar el valor de i directamente para alternar entre 1 y 2
            parque = 1 if i % 2 == 0 else 2

            # Generar una fecha aleatoria dentro del rango proporcionado
            fecha_tour = datetime.fromtimestamp(random.uniform(fecha_inicio.timestamp(), fecha_fin.timestamp()))
            
            # Limitar la hora aleatoria al rango proporcionado con formato de hora cerrada
            hora_aleatoria = timedelta(hours=random.randint(hora_inicio_24, hora_fin_24 - 1), minutes=random.randint(0, 59))
            fecha_tour += hora_aleatoria
            
            # Redondear los segundos a 0
            fecha_tour = fecha_tour.replace(second=0)

            tours.append((i + 1, parque, fecha_tour))

        # Ordenar la lista de tours por fecha y hora antes de asignar IDs
        tours = sorted(tours, key=lambda x: x[2])
        aux = 0
        for _, (tour_id, parque_num, fecha_tour) in enumerate(tours):
            fecha_tour_str = fecha_tour.strftime('%Y-%m-%d %H:%M:%S')
            aux += 1
            # Evitar duplicar la fecha y hora en la cadena de VALUES
            tour = f''' ({aux}, {parque_num}, '{fecha_tour_str}', {random.randint(1, 15)}, '{fake.name()}', '{fake.user_name()}{dominio}','+52 {random.randint(1000000000, 9999999999)}')'''

            if _ == 0:
                archivo_tours.write(f'{tour}\n')
            else:
                archivo_tours.write(f', {tour}\n')

            # Escribir el número de parque en el archivo parques.txt
            archivo_parques.write(f'{parque_num}\n')

        archivo_tours.write(''';''')

# Definir el rango de fechas y horas
fecha_inicio = datetime(2020, 7, 12)
fecha_fin = datetime(2020, 8, 19)
hora_inicio = 10
am_pm_inicio = 'AM'
hora_fin = 2
am_pm_fin = 'PM'

generar_tours(1200, fecha_inicio, fecha_fin, hora_inicio, am_pm_inicio, hora_fin, am_pm_fin)
