CREATE TABLE IF NOT EXISTS empleados (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    dni VARCHAR(8) NOT NULL UNIQUE,
    fecha_nacimiento TEXT NOT NULL,
    fecha_ingreso TEXT NOT NULL,
    activo INT NOT NULL
);
