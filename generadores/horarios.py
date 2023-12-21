from datetime import datetime, timedelta
import random

def generar_fechas_aleatorias(fecha_actual, start_time, end_time, start_time2, end_time2, horarios2_sql, fecha_limite):
    with open(horarios2_sql, 'a', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO horario(
    parque_id
    , fecha
    , hora_apertura
    , hora_cierre
)
VALUES
''')

        fecha_actual = datetime.strptime(fecha_actual, '%Y-%m-%d')
        start_time = datetime.strptime(start_time, '%H:%M:%S')
        end_time = datetime.strptime(end_time, '%H:%M:%S')
        start_time2 = datetime.strptime(start_time2, '%H:%M:%S')
        end_time2 = datetime.strptime(end_time2, '%H:%M:%S')

        while fecha_actual <= fecha_limite:
            
            random_seconds = random.randint(0, (end_time - start_time).seconds)
            hora_aleatoria = start_time + timedelta(seconds=random_seconds)
            hora_aleatoria2 = start_time2 + timedelta(seconds=random_seconds)

            archivo.write(f"    , ({2}, '{fecha_actual.strftime('%Y-%m-%d')}', '{hora_aleatoria.strftime('%H:%M:%S')}', '{hora_aleatoria2.strftime('%H:%M:%S')}')\n")
            fecha_actual += timedelta(days=1)
        archivo.write(''';''')

#1
fecha_actual = '2021-09-14'
hora_inicial = '10:00:00'
hora_final = '10:00:00'
hora_inicial2 = '22:00:00'
hora_final2 = '22:00:00'
archivo_sql = 'horarios.sql'
fecha_limite = datetime.strptime('2022-01-23', '%Y-%m-%d')

generar_fechas_aleatorias(fecha_actual, hora_inicial, hora_final, hora_inicial2, hora_final2, archivo_sql, fecha_limite)

#2
fecha_actual = '2022-03-23'
hora_inicial = '10:00:00'
hora_final = '10:00:00'
hora_inicial2 = '18:00:00'
hora_final2 = '18:00:00'
archivo_sql = 'horarios.sql'
fecha_limite = datetime.strptime('2022-08-27', '%Y-%m-%d')

generar_fechas_aleatorias(fecha_actual, hora_inicial, hora_final, hora_inicial2, hora_final2, archivo_sql, fecha_limite)

#3
fecha_actual = '2022-12-20'
hora_inicial = '10:00:00'
hora_final = '10:00:00'
hora_inicial2 = '18:00:00'
hora_final2 = '18:00:00'
archivo_sql = 'horarios.sql'
fecha_limite = datetime.strptime('2023-01-25', '%Y-%m-%d')

generar_fechas_aleatorias(fecha_actual, hora_inicial, hora_final, hora_inicial2, hora_final2, archivo_sql, fecha_limite)

#4
fecha_actual = '2023-03-23'
hora_inicial = '10:00:00'
hora_final = '10:00:00'
hora_inicial2 = '18:00:00'
hora_final2 = '18:00:00'
archivo_sql = 'horarios.sql'
fecha_limite = datetime.strptime('2023-08-27', '%Y-%m-%d')

generar_fechas_aleatorias(fecha_actual, hora_inicial, hora_final, hora_inicial2, hora_final2, archivo_sql, fecha_limite)

#5
fecha_actual = '2023-12-20'
hora_inicial = '10:00:00'
hora_final = '10:00:00'
hora_inicial2 = '18:00:00'
hora_final2 = '18:00:00'
archivo_sql = 'horarios.sql'
fecha_limite = datetime.strptime('2024-01-25', '%Y-%m-%d')

generar_fechas_aleatorias(fecha_actual, hora_inicial, hora_final, hora_inicial2, hora_final2, archivo_sql, fecha_limite)