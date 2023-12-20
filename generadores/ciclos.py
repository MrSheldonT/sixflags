from datetime import datetime, timedelta
import random
#chagpt
def generar_hora_aleatoria_con_segundos(rango_inicio, rango_fin):
    inicio = datetime.strptime(rango_inicio, "%H:%M:%S")
    fin = datetime.strptime(rango_fin, "%H:%M:%S")
    diferencia_total_segundos = int((fin - inicio).total_seconds())
    segundos_aleatorios = random.randint(0, diferencia_total_segundos)
    hora_aleatoria = inicio + timedelta(seconds=segundos_aleatorios)
    return hora_aleatoria.strftime("%H:%M:%S")

def ciclos_con_segundos(fecha, hora_inicio, hora_fin, l_atraccion, r_atraccion, size):
    id_ciclo = 1
    intervalo_minimo = 300 
    intervalo_maximo = 600 
    
    with open('ciclos.sql', 'a', encoding='utf-8') as archivo:
        for atraccion_id in range(l_atraccion, r_atraccion):
            hora_actual = datetime.strptime(hora_inicio, "%H:%M:%S")

            while hora_actual <= datetime.strptime(hora_fin, "%H:%M:%S"):
                realizar_ciclo = random.choice([True, False])

                if realizar_ciclo:
                    fecha_ciclo = f"{fecha} {hora_actual.strftime('%H:%M:%S')}"
                    archivo.write(f'({id_ciclo}, {atraccion_id}, \'{fecha_ciclo}\'),\n')
                    id_ciclo += 1

                segundos_intervalo = random.randint(intervalo_minimo, intervalo_maximo)
                hora_actual += timedelta(seconds=segundos_intervalo)

fechas_horarios = [
    ("2023-01-01", "08:00:00", "18:00:00"),
    ("2023-01-02", "09:00:00", "17:30:00"),
]

for fecha, hora_inicio, hora_fin in fechas_horarios:
    ciclos_con_segundos(fecha, hora_inicio, hora_fin, 1, 5, 3)
