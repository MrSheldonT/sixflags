from faker import Faker
import random
fake = Faker('es_MX')
Faker.seed(0)

def generar_comprador(size):
    with open('compradores.sql', 'w', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO comprador(
    nombre,
    telefono,
    correo_electronico
)
VALUES 
''')
        for _ in range(size):
            dominio = random.choice(["@outlook.com", "@gmail.com", "@yahoo.com"])
            archivo.write(f'''    ,('{fake.name()}',  '{"+52 " + str(fake.random_number(digits=10))}', '{fake.user_name()}{dominio}')\n''')
        archivo.write(''';''')

generar_comprador(150000)
