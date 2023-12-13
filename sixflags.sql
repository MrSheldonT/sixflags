DROP SCHEMA IF EXISTS six_flags;
CREATE SCHEMA six_flags;
USE six_flags;

CREATE TABLE IF NOT EXISTS parque (
    parque_id TINYINT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(90) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    ciudad VARCHAR(30) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    pais VARCHAR(15) NOT NULL,
    fecha_inauguracion DATE NOT NULL,
    fecha_cierre DATE NOT NULL,
    area_ha SMALLINT NOT NULL,
    pagina_url VARCHAR(50) NOT NULL,
    mapa_url VARCHAR(100) NOT NULL,
    PRIMARY KEY (parque_id)
);


CREATE TABLE horario (
  horario_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , fecha DATE NOT NULL 
  , hora_apertura TIME NOT NULL
  , hora_cierre TIME NOT NULL
  , PRIMARY KEY (horario_id)
);

ALTER TABLE horario
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS empleado (
  empleado_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , nombre VARCHAR(45) NOT NULL 
  , paterno VARCHAR(45) NOT NULL 
  , materno VARCHAR(45) NOT NULL 
  , genero TINYINT(1) NOT NULL 
  , fecha_nacimiento DATE NOT NULL 
  , correo_electronico VARCHAR(255) NOT NULL 
  , rfc CHAR(13) NOT NULL UNIQUE
  , curp CHAR(18) NOT NULL UNIQUE
  , nss CHAR(11) NOT NULL UNIQUE
  , estado_civil VARCHAR(45) NOT NULL
  , telefono_celular VARCHAR(15) NOT NULL
  , calle VARCHAR(20) NOT NULL
  , no_exterior VARCHAR(10) NOT NULL
  , no_interior VARCHAR(10) NOT NULL
  , colonia VARCHAR(20) NOT NULL
  , municipio VARCHAR(30) NOT NULL
  , estado VARCHAR(30) NOT NULL
  , pais VARCHAR(20) NOT NULL
  , cp CHAR(5) NOT NULL
  , tipo_contrato VARCHAR(30) NOT NULL
  , fecha_contratacion DATE NOT NULL
  , fecha_fin_contrato DATE NOT NULL
  , PRIMARY KEY(empleado_id)
);

ALTER TABLE empleado 
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS excursion (
  excursion_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , punto_partida VARCHAR(30) NOT NULL
  , fecha_hora TIMESTAMP NOT NULL
  , PRIMARY KEY(excursion_id)
);

ALTER TABLE excursion
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS alianza (
    alianza_id TINYINT AUTO_INCREMENT
    , parque_id TINYINT NOT NULL
    , nombre_comercial VARCHAR (20) NOT NULL
    , nombre_fiscal VARCHAR (40) NOT NULL
    , imagen_url VARCHAR(100) NOT NULL
    , descripcion VARCHAR(40) NOT NULL
    , pagina_url VARCHAR(50) NOT NULL
    , PRIMARY KEY (alianza_id)
);

ALTER TABLE alianza
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS tour (
  tour_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , PRIMARY KEY(tour_id)
);

ALTER TABLE tour 
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS servicio (
  servicio_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , punto_partida VARCHAR(30) NOT NULL
  , fecha_hora TIMESTAMP NOT NULL
  , PRIMARY KEY(servicio_id)
);

ALTER TABLE servicio 
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS renta (
  renta_id INT NOT NULL AUTO_INCREMENT
  , contacto_nombre VARCHAR(45) NOT NULL
  , contacto_telefono VARCHAR(15) NOT NULL
  , fecha_hora_inicio TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  , fecha_hora_fin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  , PRIMARY KEY(renta_id)
);

CREATE TABLE IF NOT EXISTS renta_detalle (
  renta_id INT NOT NULL
  , servicio_id INT NOT NULL
  , cantidad INT NOT NULL
);

ALTER TABLE renta_detalle
  ADD FOREIGN KEY (renta_id) REFERENCES renta(renta_id)
  , ADD FOREIGN KEY (servicio_id) REFERENCES servicio(servicio_id) ;


CREATE TABLE IF NOT EXISTS evento (
    evento_id INT AUTO_INCREMENT
    , parque_id TINYINT NOT NULL
    , nombre VARCHAR(45) NOT NULL
    , descripcion VARCHAR(255) NOT NULL
    , patrocinador VARCHAR(20)
    , fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    , fecha_fin TIMESTAMP DEFAULT  CURRENT_TIMESTAMP 
    , PRIMARY KEY (evento_id)
);

ALTER TABLE evento
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS villa (
  villa_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , villa_nombre VARCHAR(45) NOT NULL
  , PRIMARY KEY (villa_id)
);

ALTER TABLE villa 
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS espectaculo (
  espectaculo_id INT NOT NULL AUTO_INCREMENT
  , villa_id INT NOT NULL
  , nombre VARCHAR(45) NOT NULL 
  , descripcion VARCHAR(75) NOT NULL
  , localizacion VARCHAR(45) NOT NULL 
  , hora_inicio TIME NOT NULL
  , hora_fin TIME NOT NULL
  , fecha_inicio DATE NOT NULL
  , fecha_fin DATE NULL
  , PRIMARY KEY (espectaculo_id)
  
);

ALTER TABLE espectaculo
  ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id);


CREATE TABLE categoria_restaurante (
  categoria_restaurante_id INT NOT NULL AUTO_INCREMENT
  , nombre VARCHAR(45) NOT NULL
  , PRIMARY KEY(categoria_restaurante_id)
);


CREATE TABLE restaurante (
  restaurante_id INT NOT NULL
  , categoria_restaurante_id INT NOT NULL
  , villa_id INT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , descripcion VARCHAR(125) NOT NULL
  , PRIMARY KEY(restaurante_id)
);

ALTER TABLE restaurante
  ADD FOREIGN KEY (categoria_restaurante_id) REFERENCES categoria_restaurante(categoria_restaurante_id)
  , ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id);


CREATE TABLE IF NOT EXISTS categoria_tienda (
  categoria_tienda_id INT NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  PRIMARY KEY (categoria_tienda_id)
);


CREATE TABLE IF NOT EXISTS tienda (
  tienda_id INT NOT NULL
  , villa_id INT NOT NULL
  , categoria_tienda_id INT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , descripcion VARCHAR(125) NOT NULL
  , PRIMARY KEY (tienda_id)
);

ALTER TABLE tienda
  ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id)
  , ADD FOREIGN KEY (categoria_tienda_id) REFERENCES categoria_tienda(categoria_tienda_id) ;


CREATE TABLE IF NOT EXISTS mercancia (
  mercancia_id INT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , descripcion TEXT NOT NULL
  , precio DECIMAL NOT NULL
  , fecha_inicio TIMESTAMP NOT NULL
  , fecha_fin TIMESTAMP NULL
  , fecha_descontinuacion TIMESTAMP NULL
  , stock INT NOT NULL
  , url_imagen VARCHAR(100) NOT NULL
  , PRIMARY KEY (mercancia_id)
);


CREATE TABLE IF NOT EXISTS tienda_mercancia (
  mercancia_id INT NOT NULL
  , tienda_id INT NOT NULL
);

ALTER TABLE tienda_mercancia
  ADD FOREIGN KEY (mercancia_id) REFERENCES mercancia(mercancia_id)
  , ADD FOREIGN KEY (tienda_id) REFERENCES tienda(tienda_id);


CREATE TABLE IF NOT EXISTS tipo_atraccion (
    tipo_atraccion_id INT NOT NULL,
    nombre VARCHAR(10) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    PRIMARY KEY (tipo_atraccion_id)
);


CREATE TABLE IF NOT EXISTS nivel_emocion (
    nivel_emocion_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    PRIMARY KEY (nivel_emocion_id)
);


CREATE TABLE IF NOT EXISTS fabricante (
    fabricante_id INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    PRIMARY KEY (fabricante_id)
);


CREATE TABLE IF NOT EXISTS atraccion (
  atraccion_id INT NOT NULL
  , villa_id INT NOT NULL
  , tipo_atraccion_id INT NOT NULL
  , nivel_emocion_id INT NOT NULL
  , fabricante_id INT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , descripcion TEXT NOT NULL
  , localizacion VARCHAR(45) NOT NULL
  , caracteristicas_especiales VARCHAR(45) NULL
  , estado VARCHAR(25) NOT NULL
  , consideracion VARCHAR(80) NOT NULL
  , duracion TIME NOT NULL
  , anio_introducido YEAR NOT NULL
  , costo DECIMAL NOT NULL
  , hora_apertura TIME NOT NULL
  , hora_cierre TIME NOT NULL
  , capacidad TINYINT UNSIGNED NOT NULL
  , velocidad_max_km TINYINT NULL
  , elevacion_m TINYINT NULL
  , largo_m TINYINT NULL
  , PRIMARY KEY (atraccion_id)
);

ALTER TABLE atraccion    
  ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id)
  , ADD FOREIGN KEY (tipo_atraccion_id) REFERENCES tipo_atraccion(tipo_atraccion_id)
  , ADD FOREIGN KEY (nivel_emocion_id) REFERENCES nivel_emocion(nivel_emocion_id)
  , ADD FOREIGN KEY (fabricante_id) REFERENCES fabricante(fabricante_id);


CREATE TABLE IF NOT EXISTS ciclo (
    ciclo_id INT NOT NULL,
    atraccion_id INT NOT NULL,
    fecha_hora TIMESTAMP NOT NULL,
    no_visitantes TINYINT UNSIGNED NOT NULL,
    PRIMARY KEY (ciclo_id)
);

ALTER TABLE ciclo
  ADD FOREIGN KEY (atraccion_id) REFERENCES atraccion (atraccion_id);


CREATE TABLE IF NOT EXISTS categoria_producto (
  categoria_producto_id INT NOT NULL AUTO_INCREMENT
  , nombre VARCHAR(45) NOT NULL
  , PRIMARY KEY (categoria_producto_id)
);


CREATE TABLE IF NOT EXISTS producto (
  plu INT NOT NULL
  , categoria_producto_id INT NOT NULL
  , parque_id TINYINT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , descripcion TEXT NOT NULL
  , precio_unitario DECIMAL(8, 2) NOT NULL DEFAULT 0.00
  , fecha_inicio_venta TIMESTAMP NOT NULL
  , fecha_fin_venta TIMESTAMP NULL
  , fecha_descontinuacion TIMESTAMP NULL
  , stock MEDIUMINT UNSIGNED NOT NULL DEFAULT 0
  , cantidad_minimo_compra TINYINT NOT NULL
  , PRIMARY KEY (plu)
);

ALTER TABLE producto
  ADD FOREIGN KEY (categoria_producto_id) REFERENCES categoria_producto(categoria_producto_id)
  , ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id);


CREATE TABLE IF NOT EXISTS paquete (
  paquete_plu INT NOT NULL
  , producto_plu INT NOT NULL
  , PRIMARY KEY (paquete_plu, producto_plu)
);

ALTER TABLE paquete
  ADD FOREIGN KEY (paquete_plu) REFERENCES producto(plu)
  , ADD FOREIGN KEY (producto_plu) REFERENCES producto(plu);


CREATE TABLE IF NOT EXISTS beneficio (
  beneficio_id INT NOT NULL AUTO_INCREMENT
  , descripcion VARCHAR(80) NOT NULL
  , PRIMARY KEY (beneficio_id)
);


CREATE TABLE IF NOT EXISTS producto_beneficio (
  producto_plu INT NOT NULL
  , beneficio_id INT NOT NULL
  , PRIMARY KEY (producto_plu, beneficio_id)
);

ALTER TABLE producto_beneficio
  ADD FOREIGN KEY (producto_plu) REFERENCES producto(plu)
  , ADD FOREIGN KEY (beneficio_id) REFERENCES beneficio(beneficio_id);


CREATE TABLE IF NOT EXISTS comprador (
    comprador_id  INT
    , nombre  VARCHAR(45) NOT NULL
    , telefono VARCHAR(15) NOT NULL
    , correo_electronico VARCHAR(78) NOT NULL
    , PRIMARY KEY (comprador_id)
);


CREATE TABLE IF NOT EXISTS venta (
  venta_id INT NOT NULL AUTO_INCREMENT
  , comprador_id INT NOT NULL
  , fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
  , cargo_proceso_linea DECIMAL(6, 2) NOT NULL DEFAULT 40
  , PRIMARY KEY (venta_id)
);

ALTER TABLE venta
  ADD FOREIGN KEY (comprador_id) REFERENCES comprador(comprador_id);


CREATE TABLE IF NOT EXISTS venta_detalle (
  venta_id INT NOT NULL
  , plu INT NOT NULL
  , precio_unitario DECIMAL(8, 2) NOT NULL DEFAULT 0
  , cantidad SMALLINT NOT NULL DEFAULT 1
  , PRIMARY KEY (venta_id, plu)
);

ALTER TABLE venta_detalle
ADD FOREIGN KEY (venta_id) REFERENCES venta(venta_id)
, ADD FOREIGN KEY (plu) REFERENCES producto(plu);


CREATE TABLE IF NOT EXISTS ticket (
  ticket_id INT NOT NULL
  , venta_id INT NOT NULL
  , codigo_barras CHAR(22) NOT NULL
  , nombre_titular VARCHAR(70)
  , PRIMARY KEY (ticket_id)
);

ALTER TABLE ticket
  ADD FOREIGN KEY (venta_id) REFERENCES venta(venta_id);


CREATE TABLE IF NOT EXISTS tarjeta (
  tarjeta_id INT NOT NULL AUTO_INCREMENT
  , codigo_barras VARCHAR(20) NOT NULL
  , fecha_activacion TIMESTAMP NULL
  , revocacion TINYINT NULL
  , fecha_inicio_vigencia TIMESTAMP NULL
  , fecha_fin_vigencia TIMESTAMP NULL
  , plu INT NOT NULL
  , ticket_id INT NOT NULL
  , PRIMARY KEY (tarjeta_id)
);

ALTER TABLE tarjeta
  ADD FOREIGN KEY (plu) REFERENCES producto(plu)
  , ADD FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id);


CREATE TABLE tarjeta_complemento (
  tarjeta_principal INT NOT NULL
  , tarjeta_complemento_id INT NOT NULL
);

ALTER TABLE tarjeta_complemento
  ADD FOREIGN KEY (tarjeta_principal) REFERENCES tarjeta(tarjeta_id)
  , ADD FOREIGN KEY (tarjeta_complemento_id) REFERENCES tarjeta(tarjeta_id);
