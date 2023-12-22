from datetime import datetime, timedelta
import random

def generar_fechas_aleatorias(fecha_actual, horarios, fecha_limite, seed=None):
    if seed is not None:
        random.seed(seed)
    with open(horarios, 'a', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO horario(
    parque_id
    , fecha
    , hora_apertura
    , hora_cierre
)
VALUES
''')

        fecha_actual = datetime.strptime(fecha_actual, '%Y-%m-%d')
        hora_inicial = datetime.strptime('10:00:00', '%H:%M:%S')
        hora_inicial_alternativa = datetime.strptime('00:00:00', '%H:%M:%S')
        hora_final = (datetime.strptime('18:00:00', '%H:%M:%S'), datetime.strptime('22:00:00', '%H:%M:%S'))

        random.seed(seed)  # Establecer la semilla antes del bucle

        while fecha_actual <= fecha_limite:
            usar_hora_alternativa = random.choice([True, False])

            hora_aleatoria = hora_inicial_alternativa if usar_hora_alternativa else hora_inicial
            hora_cierre = hora_aleatoria if hora_aleatoria == hora_inicial_alternativa else random.choice(hora_final)

            archivo.write(f"    , ({1}, '{fecha_actual.strftime('%Y-%m-%d')}', '{hora_aleatoria.strftime('%H:%M:%S')}', '{hora_cierre.strftime('%H:%M:%S')}')\n")
            archivo.write(f"    , ({2}, '{fecha_actual.strftime('%Y-%m-%d')}', '{hora_aleatoria.strftime('%H:%M:%S')}', '{hora_cierre.strftime('%H:%M:%S')}')\n")
            fecha_actual += timedelta(days=1)
        archivo.write(''';''')

# Ejemplo de uso con semilla

fecha_actual = '2020-01-01'
archivo_sql = 'horarios.sql'
fecha_limite = datetime.strptime('2024-03-21', '%Y-%m-%d')
semilla = 1  # Puedes cambiar este valor para obtener diferentes secuencias aleatorias

generar_fechas_aleatorias(fecha_actual, archivo_sql, fecha_limite, semilla)