DROP TABLE IF EXISTS tbl_name;
DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT
    , nombre VARCHAR(255) NOT NULL DEFAULT ''
    , apellidos VARCHAR(255) NOT NULL DEFAULT ''
    , correo_electronico VARCHAR(255) NOT NULL UNIQUE
    , contraseña VARCHAR(255) NOT NULL
    , fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    , fecha_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    , PRIMARY KEY (`id`)
);

INSERT INTO usuarios (
    nombre
    , apellidos
    , correo_electronico
    , contraseña
)
VALUES (
    'Juan',
    'Pérez',
    'juan.perez@example.com',
    '123456'
);
ALTER TABLE usuarios
    ADD FOREIGN KEY (correo_electronico)
        REFERENCES correos_electronicos(correo_electronico),
    CHECK nombre
    ;
