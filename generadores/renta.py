from datetime import datetime, timedelta
from faker import Faker

Faker.seed(0)
fake = Faker('es_MX')


def generar_renta(size):
    with open('renta.sql', 'w', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO renta(
    contacto_nombre
    , contacto_telefono
    , fecha_hora_inicio
    , fecha_hora_fin
)
    VALUES 
''')
        renta_id = 0
        for _ in range(size):
            renta_id += 1
            # Generar una hora de inicio aleatoria entre las 11 A.M hasta las 8 P.M
            hora_inicio = fake.random_int(min=11, max=20)
            fecha_hora_inicio = fake.date_time_this_decade()
            fecha_hora_inicio = fecha_hora_inicio.replace(hour=hora_inicio)

            hora_fin = fake.random_int(min=1, max=8)
            fecha_hora_fin = fecha_hora_inicio + timedelta(hours= hora_fin)
            # Establecer la hora de fin como máximo a las 22 horas
            fecha_hora_fin = min(fecha_hora_fin, fecha_hora_inicio.replace(hour=19, minute=45))
            archivo.write(f'''    ('{fake.name()[:45]}', '{fake.phone_number()[:15]}', '{fecha_hora_inicio.strftime('%Y-%m-%d %H:%M:%S')}', '{fecha_hora_fin.strftime('%Y-%m-%d %H:%M:%S')}'),\n''')
        archivo.write(''';''')

generar_renta(5000)