from datetime import datetime, timedelta
from faker import Faker

Faker.seed(0)
fake = Faker('es_MX')

def generar_empleado(size, parques):
    with open('empleados.sql', 'w', encoding='utf-8') as archivo:
        archivo.write('''INSERT INTO empleado(
    empleado_id,
    parque_id,
    nombre,
    paterno,
    materno,
    genero,
    fecha_nacimiento,
    correo_electronico,
    rfc,
    curp,
    nss,
    estado_civil,
    telefono_celular,
    calle,
    no_exterior,
    no_interior,
    colonia,
    municipio,
    estado,
    pais,
    cp,
    tipo_contrato,
    fecha_contratacion,
    fecha_fin_contrato
)
    VALUES 
''')
        id_empleado = 0
        for parque_id in parques:
            for _ in range(size):
            
                id_empleado += 1
                fecha_contratacion = fake.date_this_decade()
                fecha_nacimiento = fake.date_of_birth(minimum_age=18)
                fecha_fin_contrato = fake.date_between_dates(date_start=fecha_contratacion, date_end=datetime.now() + timedelta(days=365))
               #archivo.write(f'''    ({id_empleado}, {parque_id}, '{fake.first_name()[:45]}', '{fake.last_name()[:45]}', '{fake.last_name()[:45] if fake.boolean() else "null"}', '{fake.random_element(elements=('M', 'F'))}', '{fecha_nacimiento.strftime('%Y-%m-%d')}', '{fake.unique.email().replace("'", "''")[:255]}', '{fake.unique.rfc().replace("'", "''")[:13]}', '{fake.unique.curp().replace("'", "''")[:18]}', '{fake.unique.ssn().replace("'", "''")[:11]}', '{fake.random_element(elements=('Casada/o', 'Divorciada/o', 'Soltera/o', 'Unión Libre', 'Viuda/o'))}', '{fake.phone_number()[:15]}', '{fake.street_name().replace("'", "''")[:20]}', '{fake.building_number()}', '{fake.random_int(1, 100)}', '{fake.city().replace("'", "''")[:20]}', '{fake.city().replace("'", "''")[:30]}', '{fake.state().replace("'", "''")[:30]}', '{fake.country().replace("'", "''")[:20]}', '{fake.postcode()[:5]}', '{fake.random_element(elements=('Tiempo completo', 'Temporal', 'Fines de semana'))}', '{fecha_contratacion.strftime('%Y-%m-%d')}', '{fecha_fin_contrato.strftime('%Y-%m-%d')}'),\n''')
                archivo.write(f'''    ({id_empleado}, {parque_id}, '{fake.first_name()[:45]}', '{fake.last_name()[:45]}', '{fake.last_name()[:45] if fake.boolean() else "null"}', '{fake.random_element(elements=('M', 'F'))}', '{fecha_nacimiento.strftime('%Y-%m-%d')}', '{fake.unique.email().replace("'", "''")[:255]}', '{fake.unique.rfc().replace("'", "''")[:13]}', '{fake.unique.curp().replace("'", "''")[:18]}', '{fake.unique.ssn().replace("'", "''")[:11]}', '{fake.random_element(elements=('Casada/o', 'Divorciada/o', 'Soltera/o', 'Unión Libre', 'Viuda/o'))}', '{fake.phone_number()[:15]}', '{fake.street_name().replace("'", "''")[:20]}', '{fake.building_number()}', '{fake.random_int(1, 100)}', '{fake.city().replace("'", "''")[:20]}', '{fake.city().replace("'", "''")[:30]}', '{fake.state().replace("'", "''")[:30]}','{fake.country().replace("'", "''")[:20]}', '{fake.postcode()[:5]}', '{fake.random_element(elements=('Tiempo completo', 'Temporal', 'Fines de semana'))}', '{fecha_contratacion.strftime('%Y-%m-%d')}', '{fecha_fin_contrato.strftime('%Y-%m-%d')}'),\n''')
        archivo.write(''';''')
generar_empleado(1000, [1, 2])
