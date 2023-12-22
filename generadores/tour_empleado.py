import random

def generar_tour_empleado(parques_file, tour_empleado_file):
    with open(parques_file, 'r', encoding='utf-8') as archivo_parques, open(tour_empleado_file, 'w', encoding='utf-8') as archivo_tour_empleado:
        for index, line in enumerate(archivo_parques):
            parque_num = int(line.strip())
            num_empleados = random.randint(1, 2)
            
            for empleado_num in range(1, num_empleados + 1):
                numero_aleatorio = random.randint(1, 1000) if '1' in line else random.randint(1001, 2000)
                archivo_tour_empleado.write(f"  , ({numero_aleatorio}, {index+1})\n")
parques_file = 'parques.txt'
tour_empleado_file = 'tour_empleado.sql'

generar_tour_empleado(parques_file, tour_empleado_file)
