import random

def generar_valores(size):
    with open('tienda_mercancia.sql', 'w', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO tienda_mercancia (
    tienda_id
    , mercancia_id
)
VALUES 
''')
        for _ in range(size):
            valor1 = random.randint(1, 15)
            valor2 = random.randint(1, 461)
            archivo.write(f'''    , ({valor1}, {valor2})\n''')
        archivo.write(''';''')

# Especifica la cantidad de inserciones que deseas
generar_valores(500)
