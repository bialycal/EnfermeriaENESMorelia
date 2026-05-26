CREATE DATABASE bd_enfermeria CHARSET 'UTF8';

-- tabla alumno
CREATE TABLE alumno
(
no_cuenta CHAR(9) NOT NULL,
nombre VARCHAR(50) NOT NULL,
apellidos VARCHAR(50) NOT NULL,
semestre TINYINT NOT NULL,
licenciatura ENUM(
    'GEOCIENCIAS',
    'MATERIALES',
    'TICS',
    'ECOLOGIA',
    'AMBIENTALES',
    'AGROFORESTALES',
    'ESTUDIOS_SOCIALES',
    'GEOHISTORIA',
    'DERECHO',
    'ADMINISTRACION',
    'LITERATURA',
    'HISTORIA_DEL_ARTE',
    'MUSICA',
    'ARTE_Y_DISENO',
    'ARCHIVOS'
) NOT NULL,
PRIMARY KEY (no_cuenta)
);

-- tabla personal
CREATE TABLE personal
(
    clave_personal INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL, 
    apellidos VARCHAR(50) NOT NULL,
    cargo ENUM ('ENFERMERO', 'MEDICO') NOT NULL,
    PRIMARY KEY (clave_personal)
);

-- tabla atencion
CREATE TABLE atencion
(
clave_atencion INT NOT NULL AUTO_INCREMENT,
fecha DATE NOT NULL, 
hora TIME NOT NULL,
tipo_servicio ENUM ('URGENCIA', 'INSUMO', 'CONSULTA', 'OTROS') NOT NULL,

no_cuenta CHAR(9) NOT NULL,
clave_personal INT NOT NULL,

PRIMARY KEY (clave_atencion),
FOREIGN KEY (no_cuenta) REFERENCES alumno(no_cuenta),
FOREIGN KEY (clave_personal) REFERENCES personal(clave_personal)
);

-- insert personal
INSERT INTO personal (nombre, apellidos, cargo)
VALUES
('Luis Francisco', 'Ambriz Vazquez', 'MEDICO'),
('Margarita', 'Hernandez Bedolla', 'ENFERMERO'),
('Anel', 'Rodriguez Sosa', 'MEDICO'),
('Juan', 'Cruz', 'MEDICO');


-- insert alumno
INSERT INTO alumno (no_cuenta, nombre, apellidos, semestre, licenciatura)
VALUES
('425004298', 'Indra Yaxeni', 'Cortes Delgado', 4, 'TICS'),
('425092112', 'Paola', 'Castillo Camacho', 4, 'TICS'),
('425089314', 'Bialy', 'Calderon Magana', 4, 'TICS'),
('425032877', 'Grecia Leilani', 'Arias Avalos', 4, 'TICS');

-- insert atencion
INSERT INTO atencion (fecha, hora, tipo_servicio, no_cuenta, clave_personal)
VALUES
('2026-05-23', '9:48:00', 'URGENCIA',  '425089314', 1),
('2026-05-23', '10:31:00', 'INSUMO',    '425092112', 3),

('2026-05-24', '8:51:00', 'CONSULTA',  '425089314', 2),
('2026-05-24', '12:17:00', 'OTROS',  '425004298', 4),
('2026-05-24', '15:11:00', 'INSUMO',  '425032877', 2),

('2026-05-25', '10:01:00', 'CONSULTA',  '425032877', 1),
('2026-05-25', '11:43:00', 'INSUMO',  '425092112', 3);
