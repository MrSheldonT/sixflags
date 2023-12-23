import random
import datetime

# Semilla
random.seed(123)

def generar_registro_venta():
    comprador_id = random.randint(1, 150000)
    fecha = generar_fecha()
    metodo_pago = generar_metodo_pago()

    return (comprador_id, fecha, metodo_pago)

def generar_fecha():
    fecha_actual = datetime.datetime.now()
    fecha_inicio = datetime.datetime(2020, 1, 1)
    fecha_fin = datetime.datetime(2023, 12, 31)
    delta = fecha_fin - fecha_inicio
    dias_transcurridos = delta.days
    fecha_generada = fecha_inicio + datetime.timedelta(days=random.randint(0, dias_transcurridos))

    # Formatear la fecha en formato estadounidense
    fecha_formateada = fecha_generada.strftime("%Y-%m-%d")

    return fecha_formateada

def generar_metodo_pago():
    metodos_pago = ["Visa", "Mastercard", "American Express", "Efectivo", "Six Flags Gift Card", "Six Flags Membership", "Paypal"]
    metodo_pago = random.choice(metodos_pago)

    return metodo_pago

registros_sql = []
for _ in range(500000):
    registro = generar_registro_venta()
    reg_sql = f'({registro[0]}, \'{registro[1]}\', \'{registro[2]}\')'
    registros_sql.append(reg_sql)

registros_sql.sort(key=lambda x: datetime.datetime.strptime(eval(x)[1], "%Y-%m-%d"))

codigo_sql = "INSERT INTO venta (comprador_id, fecha, metodo_pago) VALUES \n" + ",\n".join(registros_sql) + ";"

with open("venta.sql", "w") as archivo:
    archivo.write(codigo_sql)