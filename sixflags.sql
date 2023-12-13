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

CREATE TABLE IF NOT EXISTS villa (
    villa_id INT NOT NULL AUTO_INCREMENT,
    villa_nombre VARCHAR(45) NOT NULL,
    parque_id TINYINT NOT NULL,
    PRIMARY KEY (villa_id)
);

ALTER TABLE villa 
    ADD CONSTRAINT fk_villa_parque FOREIGN KEY (parque_id) REFERENCES parque(parque_id)
    ON DELETE CASCADE
;

CREATE TABLE IF NOT EXISTS nivel_emocion (
    nivel_emocion_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    PRIMARY KEY (nivel_emocion_id)
);

CREATE TABLE IF NOT EXISTS tipo_atraccion (
    tipo_atraccion_id INT NOT NULL,
    nombre VARCHAR(10) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    PRIMARY KEY (tipo_atraccion_id)
);

CREATE TABLE IF NOT EXISTS fabricante (
    fabricante_id INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    PRIMARY KEY (fabricante_id)
);

-- Tabla atraccion --
CREATE TABLE IF NOT EXISTS atraccion (
    atraccion_id INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    descripcion TEXT NOT NULL,
    villa_id INT NOT NULL,
    localizacion VARCHAR(45) NOT NULL,
    tipo_atraccion_id INT NOT NULL,
    nivel_emocion_id INT NOT NULL,
    fabricante_id INT NOT NULL,
    caracteristicas_especiales VARCHAR(45) NULL,
    estado VARCHAR(25) NOT NULL,
    consideracion VARCHAR(80) NOT NULL,
    duracion TIME NOT NULL,
    anio_introducido YEAR NOT NULL,
    costo DECIMAL NOT NULL,
    hora_apertura TIME NOT NULL,
    hora_cierre TIME NOT NULL,
    capacidad TINYINT UNSIGNED NOT NULL,
    velocidad_max_km TINYINT NULL,
    elevacion_m TINYINT NULL,
    largo_m TINYINT NULL,
    PRIMARY KEY (atraccion_id)
);

ALTER TABLE atraccion    
    ADD CONSTRAINT fk_atraccion_villa FOREIGN KEY (villa_id) REFERENCES villa(villa_id)
	ON DELETE CASCADE;
ALTER TABLE atraccion  
    ADD CONSTRAINT fk_atraccion_tipo_atraccion FOREIGN KEY (tipo_atraccion_id) REFERENCES tipo_atraccion(tipo_atraccion_id)
    ON DELETE CASCADE;
ALTER TABLE atraccion  
    ADD CONSTRAINT fk_atraccion_nivel_emocion FOREIGN KEY (nivel_emocion_id) REFERENCES nivel_emocion(nivel_emocion_id)
    ON DELETE CASCADE;
ALTER TABLE atraccion  
    ADD CONSTRAINT fk_atraccion_fabricante FOREIGN KEY (fabricante_id) REFERENCES fabricante(fabricante_id)
    ON DELETE CASCADE;

-- Tabla ciclo --
CREATE TABLE IF NOT EXISTS ciclo (
    ciclo_id INT NOT NULL,
    atraccion_id INT NOT NULL,
    fecha_hora TIMESTAMP NOT NULL,
    no_visitantes TINYINT UNSIGNED NOT NULL,
    PRIMARY KEY (ciclo_id)
);

ALTER TABLE ciclo
    ADD CONSTRAINT fk_ciclo_atraccion FOREIGN KEY (atraccion_id) REFERENCES atraccion (atraccion_id)
    ON DELETE CASCADE
;

-- Tabla alianza --
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
-- Llaves foráneas de alianza --
ALTER TABLE alianza
    ADD CONSTRAINT fk_alianza_parque FOREIGN KEY alianza(parque_id) REFERENCES parque(parque_id)
    ON DELETE CASCADE
;
-- Tabla comprador --
CREATE TABLE IF NOT EXISTS comprador (
    comprador_id  INT
    , nombre  VARCHAR(45) NOT NULL
    , telefono VARCHAR(15) NOT NULL
    , correo_electronico VARCHAR(78) NOT NULL
    , PRIMARY KEY (comprador_id)
);
-- Tabla evento --
CREATE TABLE IF NOT EXISTS evento (
    evento_id INT AUTO_INCREMENT
    , parque_id TINYINT NOT NULL
    , nombre VARCHAR(45) NOT NULL
    , descripcion VARCHAR(255) NOT NULL
    , patrocinador VARCHAR(20)
    , fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Revisar
    , fecha_fin TIMESTAMP DEFAULT  CURRENT_TIMESTAMP -- Revisar
    , PRIMARY KEY (evento_id)
);
-- Restricciones de evento --
ALTER TABLE evento
    ADD CONSTRAINT fk_evento_parque FOREIGN KEY (parque_id) REFERENCES parque(parque_id)
    ON DELETE CASCADE
;


-- hola, no sé como se le hace con las fk

-- -----------------------------------------------------
-- Tabla producto
-- -----------------------------------------------------
CREATE TABLE producto (
	-- atributos	
	plu INT NOT NULL
	, nombre VARCHAR(45) NOT NULL
    , descripcion TEXT NOT NULL
	, precio_unitario DECIMAL(8,2) NOT NULL DEFAULT 0.00
	, fecha_inicio_venta TIMESTAMP NOT NULL
	, fecha_fin_venta TIMESTAMP NULL
	, fecha_descontinuacion TIMESTAMP NULL
	, stock MEDIUMINT UNSIGNED NOT NULL DEFAULT 0
	, cantidad_minimo_compra TINYINT NOT NULL
	-- pk y fk
	, PRIMARY KEY (plu)
	, categoria_producto_id INT NOT NULL
	, parque_id TINYINT NOT NULL
)
;



-- -----------------------------------------------------
-- Tabla beneficio
-- -----------------------------------------------------

CREATE TABLE beneficio (
	-- atributos
	beneficio_id INT NOT NULL AUTO_INCREMENT
	, descripcion VARCHAR(80) NOT NULL
	-- pk
	, PRIMARY KEY (beneficio_id)
)
;




-- -----------------------------------------------------
-- Tabla tarjeta
-- -----------------------------------------------------

CREATE TABLE tarjeta (
	-- atributos
	tarjeta_id INT NOT NULL AUTO_INCREMENT
	, codigo_barras VARCHAR(20) NOT NULL
	, fecha_activacion TIMESTAMP NULL
	, revocacion TINYINT NULL
	, fecha_inicio_vigencia TIMESTAMP NULL
	, fecha_fin_vigencia TIMESTAMP NULL
  	-- pk y fk
  	, PRIMARY KEY (tarjeta_id)
  	, plu INT NOT NULL
  	, ticket_id INT NOT NULL
)
;


-- -----------------------------------------------------
-- Tabla producto_beneficio
-- -----------------------------------------------------

CREATE TABLE producto_beneficio (
	-- fk 
	producto_producto_plu INT NOT NULL
  , beneficio_beneficio_id INT NOT NULL
  , PRIMARY KEY (
  		producto_producto_plu
		, beneficio_beneficio_id
	)
)
;


-- -----------------------------------------------------
-- Tabla paquete
-- -----------------------------------------------------

CREATE TABLE paquete (
	paquete_plu INT NOT NULL
	, producto_plu INT NOT NULL
  	, PRIMARY KEY (
		paquete_plu
		, producto_plu
	)
)    	
;

-- tabla show --
-- Crear la tabla show --
CREATE TABLE shows (
-- Atributos 
	show_id INT NOT NULL
	, nombre VARCHAR(45) NOT NULL 
	, descripcion VARCHAR(75) NOT NULL
	, localizacion VARCHAR(45) NOT NULL 
	, hora_inicio TIME NOT NULL
	, hora_fin TIME NOT NULL
	, fecha_inicio DATE NOT NULL
	, fecha_fin DATE NULL
	-- pk y fk
	, PRIMARY KEY (show_id)
	, villa_id INT NOT NULL
);

-- Tabla restaurante --
CREATE TABLE restaurante(
	restaurante_id INT NOT NULL
	, nombre VARCHAR(45) NOT NULL
	, descripcion VARCHAR(125) NOT NULL
	, PRIMARY KEY(restaurante_id)
	, categoria_restaurante_id INT NOT NULL
	, villa_id INT NOT NULL
);

-- Tabla categoria_restaurante --
-- Crear tabla categoria restaurante
CREATE TABLE categoria_restaurante (
	-- atributos
	categoria_restaurante_id INT NOT NULL
	, nombre VARCHAR(45) NOT NULL
	-- pk
	, PRIMARY KEY(categoria_restaurante_id)
);

-- Tabla venta
CREATE TABLE venta (
	venta_id INT NOT NULL AUTO_INCREMENT
	, comprador_id INT NOT NULL
	, fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
	, cargo_proceso_linea DECIMAL(6, 2) NOT NULL DEFAULT 40
	, PRIMARY KEY (venta_id)
);


-- Tabla venta_detalle
CREATE TABLE venta_detalle (
	venta_id INT NOT NULL
	, plu INT NOT NULL
	, precio_unitario DECIMAL(8, 2) NOT NULL DEFAULT 0
	, cantidad SMALLINT NOT NULL DEFAULT 1
	, PRIMARY KEY (venta_id, plu)
);

-- Tabla ticket
CREATE TABLE IF NOT EXISTS ticket (
    ticket_id INT NOT NULL
    , codigo_barras CHAR(22) NOT NULL
    , nombre_titular VARCHAR(70)
    , venta_id INT NOT NULL
    , PRIMARY KEY (ticket_id)
);

-- Restricciones ticket
ALTER TABLE ticket
    ADD CONSTRAINT fk_ticket_venta FOREIGN KEY (venta_id) REFERENCES venta(venta_id)
    ON DELETE CASCADE;


-- Tabla categoria_producto
CREATE TABLE categoria_producto (
	categoria_producto_id INT NOT NULL AUTO_INCREMENT
	, nombre VARCHAR(45) NOT NULL
	, PRIMARY KEY (categoria_producto_id)
);


-- Tabla horario
CREATE TABLE horario (
	horario_id INT NOT NULL AUTO_INCREMENT
	, parque_id TINYINT NOT NULL
	, fecha DATE NOT NULL 
	, hora_apertura TIME NOT NULL
	, hora_cierre TIME NOT NULL
	, PRIMARY KEY (horario_id)
);
CREATE TABLE IF NOT EXISTS empleado (
	empleado_id INT NOT NULL AUTO_INCREMENT
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

CREATE TABLE IF NOT EXISTS excursion (
	excursion_id INT NOT NULL AUTO_INCREMENT
    , punto_partida VARCHAR(30) NOT NULL
    , fecha_hora TIMESTAMP NOT NULL
    , PRIMARY KEY(excursion_id)
);

CREATE TABLE IF NOT EXISTS servicio (
	servicio_id INT NOT NULL AUTO_INCREMENT
    , punto_partida VARCHAR(30) NOT NULL
    , fecha_hora TIMESTAMP NOT NULL
    , PRIMARY KEY(servicio_id)
);
CREATE TABLE IF NOT EXISTS renta (
	renta_id INT NOT NULL AUTO_INCREMENT
    , contacto_nombre VARCHAR(45) NOT NULL
    , contacto_telefono VARCHAR(15) NOT NULL
    , fecha_hora_inicio TIMESTAMP NOT NULL
    , fecha_hora_fin TIMESTAMP NOT NULL
    , PRIMARY KEY(renta_id)
);
