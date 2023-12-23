# Modificando el script para que la fecha de admisión esté dentro de los últimos 3 años

import random
import datetime

def generar_fecha_admision():
    fecha_actual = datetime.datetime.now()
    fecha_inicio = fecha_actual - datetime.timedelta(days=3*365)  # 3 años atrás
    dias_random = random.randint(0, 3*365)  # Número aleatorio de días dentro de los últimos 3 años
    fecha_admision = fecha_inicio + datetime.timedelta(days=dias_random)
    return fecha_admision.strftime("%Y-%m-%d %H:%M:%S")

def generar_registro_admision(admision_no, tarjeta_id):
    fecha_admision = generar_fecha_admision()  # Fecha de admisión dentro de los últimos 3 años
    parque_id = random.choice([1, 2])  # Parque_id será 1 o 2 aleatoriamente

    return admision_no, f"'{fecha_admision}'", parque_id, tarjeta_id

registros_sql = []
admision_no = 1  # Inicializar 'admision_no'
tarjeta_id = 1  # Inicializar 'tarjeta_id'
for i in range(1, 10001):  # Generar 10,000 registros
    registro = generar_registro_admision(admision_no, tarjeta_id)
    reg_sql = f'({registro[0]}, {registro[1]}, {registro[2]}, {registro[3]})'
    registros_sql.append(reg_sql)
    admision_no += 1  # Incrementar 'admision_no' para el siguiente registro
    tarjeta_id += 1  # Incrementar 'tarjeta_id' para el siguiente registro

codigo_sql = "INSERT INTO admision (admision_no, fecha_admision, parque_id, tarjeta_id) VALUES \n" + ",\n".join(registros_sql) + ";"

# Este código ahora genera 'fecha_admision' dentro de los últimos 3 años para cada registro.
# Nota: Este código debe ejecutarse en un entorno de Python con acceso a la librería datetime.
with open("admision.sql", "w") as archivo:
    archivo.write(codigo_sql)