import random
from datetime import datetime, timedelta

def generar_excursion(size, fecha_inicio=None, fecha_fin=None, hora_inicio=None, hora_fin=None):
    with open('excursion.sql', 'w', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO excursion(
    parque_id
    , punto_partida
    , fecha_hora
)
VALUES 
''')
        fecha_inicio = fecha_inicio or datetime.now()  # Si no se proporciona fecha_inicio, usa la fecha y hora actuales
        fecha_fin = fecha_fin or fecha_inicio + timedelta(days=365)  # Si no se proporciona fecha_fin, usa un año después de fecha_inicio
        hora_inicio = hora_inicio or datetime.strptime("08:00:00", "%H:%M:%S")  # Si no se proporciona hora_inicio, usa las 08:00:00
        hora_fin = hora_fin or datetime.strptime("18:00:00", "%H:%M:%S")  # Si no se proporciona hora_fin, usa las 18:00:00

        fechas = []

        for _ in range(size):
            punto_partida = random.choice(["ALCALDÍA IZTACALCO", "VILLA DE CORTÉS", "18 DE MARZO", "CENTRO MÉDICO", "ACATITLA", "TOLUCA", "PUEBLA", "ORIENTE EDOMEX", "NEZA-IXTAPALUCA"])
            parque_destino = random.choice([1, 2])

            fecha_hora = fecha_inicio + random.random() * (fecha_fin - fecha_inicio)
            fecha_hora = fecha_hora.replace(hour=random.randint(hora_inicio.hour, hora_fin.hour), minute=random.randint(0, 59), second=random.randint(0, 59))
            fecha_salida = fecha_hora.strftime('%Y-%m-%d %H:%M:%S')

            fechas.append((parque_destino, punto_partida, fecha_salida))

        # Ordena las fechas antes de escribirlas en el archivo
        fechas = sorted(fechas, key=lambda x: x[2])

        for fecha in fechas:
            archivo.write(f'''    ,({fecha[0]}, '{fecha[1]}', '{fecha[2]}')\n''')

        archivo.write(''';''')

fecha_inicio = datetime(2020, 10, 1)
fecha_fin = datetime(2024, 1, 1)
hora_inicio = datetime.strptime("05:00:00", "%H:%M:%S")
hora_fin = datetime.strptime("09:00:00", "%H:%M:%S")
generar_excursion(1350, fecha_inicio, fecha_fin, hora_inicio, hora_fin)