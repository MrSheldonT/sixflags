# Modificando el código para incluir 'venta_id' de forma incremental en la generación de registros para la tabla 'ticket'

import random
from faker import Faker

faker = Faker('es_MX')


def generar_registro_ticket(ticket_id, venta_id):
    codigo_barras = generar_codigo_barras()
    nombre_titular = faker.name()

    # Agregar 'venta_id' al registro
    return ticket_id, venta_id, f"'{codigo_barras}'", f"'{nombre_titular}'"


def generar_codigo_barras():
    return ''.join(random.choices('ABCDE0123456789', k=22))


registros_sql = []
venta_id = 1  # Inicializar 'venta_id' de forma incremental
for i in range(1, 10001):  # Generar 10,000 registros
    registro = generar_registro_ticket(i, venta_id)
    reg_sql = f'({registro[0]}, {registro[1]}, {registro[2]}, {registro[3]})'
    registros_sql.append(reg_sql)
    venta_id += 1  # Incrementar 'venta_id' para el siguiente registro

codigo_sql = "INSERT INTO ticket (ticket_id, venta_id, codigo_barras, nombre_titular) VALUES \n" + ",\n".join(
    registros_sql) + ";"

with open("tickets.sql", "w") as archivo:
    archivo.write(codigo_sql)

# Este código ahora incluye 'venta_id' incrementado de forma automática para cada registro.
# Nota: Este código debe ejecutarse en un entorno de Python con las librerías Faker y random instaladas.
