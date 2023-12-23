-- Tabla tipos de atraciiónes
CREATE TABLE IF NOT EXISTS tipo_atraccion (
    tipo_atraccion_id INT NOT NULL AUTO_INCREMENT,
    , nombre VARCHAR(10) NOT NULL
    , descripcion VARCHAR(300) NOT NULL
    PRIMARY KEY (tipo_atraccion_id)
);

-- Tipos de atracción
INSERT INTO tipo_atraccion_id(
    tipo_atraccion_id
    , nombre
    , descripcion
)
VALUES 
    (1,'Juegos Familiares', 'En Six Flags Mexico la diversión familiar es nuestra especialidad. Por eso, prepárate para desahogarte y reír con ganas. Desde las alturas más extremas, hasta las aventuras más tranquilas, tenemos atracciones para que todos puedan disfrutar.')
    , (2, 'Juegos X-Tremos', '¿Estás buscando emoción? La encontraste. De hecho, has encontrado algunas de las atracciones más rápidas, más altas y más impactantes del país incluyendo unas cuantas que baten récords mundiales.')
    , (3, 'Juegos Infantiles', '¡Las nuevas zonas infantiles BUGS BUNNY BOOMTOWN y DC SUPER FRIENDS ya están abiertas! Los más pequeños disfrutarán de 15 juegos y atracciones, ¡6 de ellas completamente nuevas!')
;