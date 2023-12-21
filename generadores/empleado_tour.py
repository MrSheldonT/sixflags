import random

def generar_empleadoTour(size):
    with open('empleadoTour.sql', 'w', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO empleado_tour(
    empleado_id
    , id_tour
)
VALUES 
''')
        for _ in range(size):
            empleado = random.choice(range(1, 201))
            tour = random.choice(range(1, 501))
            archivo.write(f'''    , ({empleado}, {tour})\n''')
        archivo.write(''';''')

generar_empleadoTour(500)
