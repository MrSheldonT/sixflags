from faker import Faker
import random
from datetime import datetime, timedelta

Faker.seed(3)
fake = Faker('es_MX')

def generar_tours(size, fecha_inicio, fecha_fin, hora_inicio, hora_fin):
    with open('tours.sql', 'w', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO tour(
    parque_id
    , fecha_tour
    , hora_tour
    , no_visitantes
    , contacto_nombre
    , contacto_correo
    , contacto_telefono
)
VALUES 
''')
        tours = []  # Lista para almacenar las filas generadas

        for _ in range(size):
            dominio = random.choice(["@outlook.com", "@gmail.com", "@yahoo.com"])
            parque = random.choice([1, 2])
            
            # Generar una fecha aleatoria dentro del rango proporcionado
            fecha_tour = datetime.fromtimestamp(random.uniform(fecha_inicio.timestamp(), fecha_fin.timestamp())).date()
            
            # Limitar la hora aleatoria al rango de 10:00 AM a 12:59 PM
            hora_aleatoria = timedelta(hours=random.randint(hora_inicio, hora_fin - 1), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
            hora_tour = (datetime.min + hora_aleatoria).time()
            
            fecha_tour_str = fecha_tour.strftime('%Y-%m-%d')
            hora_tour_str = hora_tour.strftime('%H:%M:%S')

            tour = f'''    , ({parque}, '{fecha_tour_str}', '{hora_tour_str}', {random.randint(1, 15)}, '{fake.name()}', '{fake.user_name()}{dominio}','+52 {random.randint(1000000000, 9999999999)}')\n'''
            tours.append((f'{fecha_tour_str} {hora_tour_str}', tour))

        # Ordenar la lista de tours por la fecha antes de escribirla en el archivo
        tours = sorted(tours, key=lambda x: x[0])

        for _, tour in tours:
            archivo.write(tour)

        archivo.write(''';''')

# Definir el rango de fechas y horas
fecha_inicio = datetime(2020, 3, 1)
fecha_fin = datetime(2024, 1, 31)
hora_inicio = 10
hora_fin = 13

generar_tours(500, fecha_inicio, fecha_fin, hora_inicio, hora_fin)


