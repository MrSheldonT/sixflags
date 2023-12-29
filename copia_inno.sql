DROP DATABASE IF EXISTS six_flags;
CREATE DATABASE six_flags;
USE six_flags;

-- Definición de tablas
CREATE TABLE IF NOT EXISTS parque (
    parque_id TINYINT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(90) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    ciudad VARCHAR(30) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    pais VARCHAR(15) NOT NULL,
    fecha_inauguracion DATE NOT NULL,
    fecha_cierre DATE,
    area_ha SMALLINT,
    pagina_url VARCHAR(100) NOT NULL,
    mapa_url VARCHAR(100) NOT NULL,
    PRIMARY KEY (parque_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS horario (
  horario_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , fecha DATE NOT NULL 
  , hora_apertura TIME NOT NULL
  , hora_cierre TIME NOT NULL
  , PRIMARY KEY (horario_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS empleado (
  empleado_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , nombre VARCHAR(45) NOT NULL 
  , paterno VARCHAR(45) NOT NULL 
  , materno VARCHAR(45) NOT NULL 
  , genero CHAR(1) NOT NULL 
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
  , activo TINYINT(1)
  , PRIMARY KEY(empleado_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS excursion (
  excursion_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , punto_partida VARCHAR(30) NOT NULL
  , fecha_hora TIMESTAMP NOT NULL
  , PRIMARY KEY(excursion_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS alianza (
    alianza_id TINYINT AUTO_INCREMENT
    , parque_id TINYINT NOT NULL
    , nombre_comercial VARCHAR (20) NOT NULL
    , nombre_fiscal VARCHAR (60) NOT NULL
    , imagen_url VARCHAR(100) NOT NULL
    , descripcion VARCHAR(40) NOT NULL
    , pagina_url VARCHAR(50) NOT NULL
    , PRIMARY KEY (alianza_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tour (
  tour_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , fecha_hora TIMESTAMP NOT NULL
  , no_visitantes TINYINT NOT NULL
  , contacto_nombre VARCHAR(60) NOT NULL
  , contacto_correo VARCHAR(255) NOT NULL
  , contacto_telefono VARCHAR(15) NOT NULL
  , PRIMARY KEY(tour_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS empleado_tour (
  empleado_id INT NOT NULL 
  , tour_id INT NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS servicio (
  servicio_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , nombre VARCHAR(70) NOT NULL
  , descripcion TEXT NOT NULL
  , precio DECIMAL(6, 2) NOT NULL 
  , deposito_inicial DECIMAL (6, 2)
  , PRIMARY KEY(servicio_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS renta (
  renta_id INT NOT NULL AUTO_INCREMENT
  , contacto_nombre VARCHAR(60) NOT NULL
  , contacto_telefono VARCHAR(15) NOT NULL
  , fecha_hora_inicio TIMESTAMP NOT NULL
  , fecha_hora_fin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  , PRIMARY KEY(renta_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS renta_detalle (
  renta_id INT NOT NULL
  , servicio_id INT NOT NULL
  , cantidad TINYINT NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS evento (
    evento_id INT AUTO_INCREMENT
    , parque_id TINYINT NOT NULL
    , nombre VARCHAR(45) NOT NULL
    , descripcion TEXT NOT NULL
    , patrocinador VARCHAR(20)
    , fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    , fecha_fin TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    , PRIMARY KEY (evento_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS villa (
  villa_id INT NOT NULL AUTO_INCREMENT
  , parque_id TINYINT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , PRIMARY KEY (villa_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS espectaculo (
  espectaculo_id INT NOT NULL AUTO_INCREMENT
  , villa_id INT NOT NULL
  , nombre VARCHAR(55) NOT NULL
  , descripcion VARCHAR(255) NOT NULL
  , localizacion VARCHAR(70) NOT NULL
  , hora_inicio TIME NOT NULL
  , hora_fin TIME NOT NULL
  , fecha_inicio DATE NOT NULL
  , fecha_fin DATE NULL
  , PRIMARY KEY (espectaculo_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS categoria_restaurante (
  categoria_restaurante_id INT NOT NULL AUTO_INCREMENT
  , nombre VARCHAR(45) NOT NULL
  , PRIMARY KEY(categoria_restaurante_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS restaurante (
  restaurante_id INT NOT NULL
  , categoria_restaurante_id INT NOT NULL
  , villa_id INT NOT NULL
  , nombre VARCHAR(50) NOT NULL
  , descripcion VARCHAR(300) NOT NULL
  , PRIMARY KEY(restaurante_id)
)ENGINE=InnoDB ;

CREATE TABLE IF NOT EXISTS categoria_tienda (
  categoria_tienda_id INT NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  PRIMARY KEY (categoria_tienda_id)
)ENGINE=InnoDB ;

CREATE TABLE IF NOT EXISTS tienda (
  tienda_id INT NOT NULL
  , villa_id INT NOT NULL
  , categoria_tienda_id INT NOT NULL
  , nombre VARCHAR(50) NOT NULL
  , descripcion VARCHAR(300) NOT NULL
  , PRIMARY KEY (tienda_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS mercancia (
  mercancia_id INT NOT NULL
  , nombre VARCHAR(100) NOT NULL
  , descripcion TEXT NOT NULL
  , precio DECIMAL(6, 2) NOT NULL
  , fecha_inicio_venta TIMESTAMP NOT NULL
  , fecha_fin_venta TIMESTAMP NULL
  , descontinuacion TINYINT(1) NULL
  , stock INT NOT NULL
  , url_imagen VARCHAR(200) NOT NULL
  , PRIMARY KEY (mercancia_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tienda_mercancia (
  tienda_id INT NOT NULL
  , mercancia_id INT NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tipo_atraccion (
  tipo_atraccion_id INT AUTO_INCREMENT
  , nombre VARCHAR(30) NOT NULL
  , descripcion VARCHAR(300) NOT NULL
  , PRIMARY KEY (tipo_atraccion_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS nivel_emocion (
    nivel_emocion_id INT AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    PRIMARY KEY (nivel_emocion_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS fabricante (
    fabricante_id INT AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    PRIMARY KEY (fabricante_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS atraccion (
  atraccion_id INT AUTO_INCREMENT
  , villa_id INT NOT NULL
  , tipo_atraccion_id INT NOT NULL
  , nivel_emocion_id INT NOT NULL
  , fabricante_id INT NOT NULL
  , nombre VARCHAR(45) NOT NULL
  , descripcion TEXT NOT NULL
  , caracteristicas_especiales VARCHAR(45)
  , estado VARCHAR(25) NOT NULL
  , consideracion VARCHAR(80) NOT NULL
  , duracion TIME
  , anio_introducido YEAR NOT NULL
  , costo DECIMAL(6, 2) NOT NULL DEFAULT 0.00
  , capacidad TINYINT UNSIGNED
  , velocidad_max_km TINYINT UNSIGNED
  , elevacion_m TINYINT UNSIGNED
  , largo_m SMALLINT
  , PRIMARY KEY (atraccion_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS ciclo (
    ciclo_id INT NOT NULL
    , atraccion_id INT NOT NULL
    , fecha_hora TIMESTAMP NOT NULL
    , PRIMARY KEY (ciclo_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS categoria_producto (
  categoria_producto_id INT NOT NULL AUTO_INCREMENT
  , nombre VARCHAR(45) NOT NULL
  , PRIMARY KEY (categoria_producto_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS producto (
  plu INT NOT NULL
  , categoria_producto_id INT NOT NULL
  , parque_id TINYINT NOT NULL
  , nombre VARCHAR(60) NOT NULL
  , descripcion TEXT NOT NULL
  , precio_unitario DECIMAL(8, 2) NOT NULL DEFAULT 0.00
  , fecha_inicio_venta TIMESTAMP NOT NULL
  , fecha_fin_venta TIMESTAMP NULL
  , descontinuacion TINYINT(1) NULL
  , stock MEDIUMINT UNSIGNED NOT NULL DEFAULT 0
  , cantidad_minimo_compra TINYINT NOT NULL
  , PRIMARY KEY (plu)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS paquete (
  paquete_plu INT NOT NULL
  , producto_plu INT NOT NULL
  , PRIMARY KEY (paquete_plu, producto_plu)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS beneficio (
  beneficio_id INT NOT NULL AUTO_INCREMENT
  , descripcion VARCHAR(200) NOT NULL
  , PRIMARY KEY (beneficio_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS producto_beneficio (
  plu INT NOT NULL
  , beneficio_id INT NOT NULL
  , PRIMARY KEY (plu, beneficio_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS comprador (
    comprador_id INT AUTO_INCREMENT
    , nombre  VARCHAR(60) NOT NULL
    , telefono VARCHAR(15) NOT NULL
    , correo_electronico VARCHAR(255) NOT NULL
    , PRIMARY KEY (comprador_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS venta (
  venta_id INT NOT NULL AUTO_INCREMENT
  , comprador_id INT NOT NULL
  , fecha TIMESTAMP NOT NULL
  , cargo_proceso_linea DECIMAL(6, 2) NOT NULL DEFAULT 40
  , tipo_pago VARCHAR(30) NOT NULL
  , PRIMARY KEY (venta_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS venta_detalle (
  venta_id INT NOT NULL
  , plu INT NOT NULL
  , precio_unitario DECIMAL(8, 2) NOT NULL DEFAULT 0
  , cantidad SMALLINT NOT NULL DEFAULT 1
  , PRIMARY KEY (venta_id, plu)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS ticket (
  ticket_id INT NOT NULL AUTO_INCREMENT
  , venta_id INT NOT NULL
  , codigo_barras CHAR(22) NOT NULL
  , nombre_titular VARCHAR(70)
  , PRIMARY KEY (ticket_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tarjeta (
  tarjeta_id INT NOT NULL AUTO_INCREMENT
  , codigo_barras VARCHAR(20) NOT NULL
  , fecha_activacion TIMESTAMP NULL
  , revocacion TINYINT(1) NULL
  , fecha_inicio_vigencia TIMESTAMP NULL
  , fecha_fin_vigencia TIMESTAMP NULL
  , plu INT NOT NULL
  , ticket_id INT NOT NULL
  , PRIMARY KEY (tarjeta_id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tarjeta_complemento (
  tarjeta_principal INT NOT NULL
  , tarjeta_complemento_id INT NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS flash_pass (
  ciclo_id INT NOT NULL
  , tarjeta_id INT NOT NULL
)ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS admision(
  	admision_id INT NOT NULL AUTO_INCREMENT
  	, fecha_admision TIMESTAMP NOT NULL
  	, parque_id TINYINT NOT NULL
  	, tarjeta_id INT NOT NULL
  	, PRIMARY KEY(admision_id)
)ENGINE=InnoDB;

-- Bloque de alters_______________________________________________________________________________________________
-- Horario con parque
ALTER TABLE horario
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
-- Empleado con parque
ALTER TABLE empleado
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
-- Excursión con parque
ALTER TABLE excursion
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
-- Alianza con parque
ALTER TABLE alianza
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
-- Tour con parque
ALTER TABLE tour
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
  -- empleado_tour
ALTER TABLE empleado_tour
  ADD FOREIGN KEY (empleado_id) REFERENCES empleado(empleado_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (tour_id) REFERENCES tour(tour_id) ON DELETE CASCADE;
-- Servicio con parque
ALTER TABLE servicio
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
-- Detalle de la renta de servicio
ALTER TABLE renta_detalle
  ADD FOREIGN KEY (renta_id) REFERENCES renta(renta_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (servicio_id) REFERENCES servicio(servicio_id) ON DELETE CASCADE;
-- Evento con parque
ALTER TABLE evento
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
-- Villa con parque
ALTER TABLE villa
  ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;
-- Espetaculo con villa
ALTER TABLE espectaculo
  ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id) ON DELETE CASCADE;
-- Categoría del restaurante y villa
ALTER TABLE restaurante
  ADD FOREIGN KEY (categoria_restaurante_id) REFERENCES categoria_restaurante(categoria_restaurante_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id) ON DELETE CASCADE;
-- Tienda
ALTER TABLE tienda
  ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (categoria_tienda_id) REFERENCES categoria_tienda(categoria_tienda_id) ON DELETE CASCADE;
-- Mercancia
ALTER TABLE tienda_mercancia
  ADD FOREIGN KEY (tienda_id) REFERENCES tienda(tienda_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (mercancia_id) REFERENCES mercancia(mercancia_id) ON DELETE CASCADE;

ALTER TABLE tarjeta_complemento
  ADD FOREIGN KEY (tarjeta_principal) REFERENCES tarjeta(tarjeta_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (tarjeta_complemento_id) REFERENCES tarjeta(tarjeta_id) ON DELETE CASCADE;

ALTER TABLE tarjeta
  ADD FOREIGN KEY (plu) REFERENCES producto(plu) ON DELETE CASCADE
  , ADD FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id) ON DELETE CASCADE;

ALTER TABLE ticket
  ADD FOREIGN KEY (venta_id) REFERENCES venta(venta_id) ON DELETE CASCADE;

ALTER TABLE venta_detalle
ADD FOREIGN KEY (venta_id) REFERENCES venta(venta_id) ON DELETE CASCADE
, ADD FOREIGN KEY (plu) REFERENCES producto(plu) ON DELETE CASCADE;

ALTER TABLE atraccion    
  ADD FOREIGN KEY (villa_id) REFERENCES villa(villa_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (tipo_atraccion_id) REFERENCES tipo_atraccion(tipo_atraccion_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (nivel_emocion_id) REFERENCES nivel_emocion(nivel_emocion_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (fabricante_id) REFERENCES fabricante(fabricante_id) ON DELETE CASCADE;

ALTER TABLE ciclo
  ADD FOREIGN KEY (atraccion_id) REFERENCES atraccion(atraccion_id) ON DELETE CASCADE;

ALTER TABLE venta
  ADD FOREIGN KEY (comprador_id) REFERENCES comprador(comprador_id) ON DELETE CASCADE;

ALTER TABLE producto_beneficio
  ADD FOREIGN KEY (plu) REFERENCES producto(plu) ON DELETE CASCADE
  , ADD FOREIGN KEY (beneficio_id) REFERENCES beneficio(beneficio_id) ON DELETE CASCADE;

ALTER TABLE paquete
  ADD FOREIGN KEY (paquete_plu) REFERENCES producto(plu) ON DELETE CASCADE
  , ADD FOREIGN KEY (producto_plu) REFERENCES producto(plu) ON DELETE CASCADE;

ALTER TABLE producto
  ADD FOREIGN KEY (categoria_producto_id) REFERENCES categoria_producto(categoria_producto_id) ON DELETE CASCADE
  , ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE;

ALTER TABLE flash_pass
  ADD FOREIGN KEY (ciclo_id) REFERENCES ciclo(ciclo_id) ON DELETE CASCADE 
  , ADD FOREIGN KEY (tarjeta_id) REFERENCES tarjeta(tarjeta_id) ON DELETE CASCADE ;

 ALTER TABLE admision
  	ADD FOREIGN KEY (parque_id) REFERENCES parque(parque_id) ON DELETE CASCADE
    , ADD FOREIGN KEY (tarjeta_id) REFERENCES tarjeta(tarjeta_id) ON DELETE CASCADE
 ;
