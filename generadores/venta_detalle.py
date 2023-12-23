import random


def generar_registro_venta_detalle(venta_id, plus_disponibles):
    plu = random.choice(plus_disponibles)
    precio_unitario = round(random.uniform(5, 100), 2)
    cantidad = random.randint(1, 270)
    return venta_id, plu, f"{precio_unitario:.2f}", cantidad

try:
    with open("plu.txt", "r") as archivo:
        plus_disponibles = [line.strip() for line in archivo.readlines()]
except FileNotFoundError:
    print("Archivo plu.txt no encontrado. Asegúrate de que el archivo esté en el directorio correcto.")
    plus_disponibles = []

registros_sql = []
venta_id = 1
for i in range(1, 10001):
    registro = generar_registro_venta_detalle(venta_id, plus_disponibles)
    reg_sql = f'({registro[0]}, {registro[1]}, {registro[2]}, {registro[3]})'
    registros_sql.append(reg_sql)
    venta_id += 1

codigo_sql = "INSERT INTO venta_detalle (venta_id, plu, precio_unitario, cantidad) VALUES \n" + ",\n".join(
    registros_sql) + ";"

with open("venta_detalle.sql", "w") as archivo:
    archivo.write(codigo_sql)