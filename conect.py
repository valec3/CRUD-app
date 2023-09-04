import mysql.connector

def conectar():    
    cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "toor",
        database = "empresa_tuto"
    )

    cursor = cnx.cursor()
    try:
        sql = """
            CREATE TABLE IF NOT EXISTS empleados (
            id_empleado INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(20) NOT NULL,
            apellido VARCHAR(20) NOT NULL,
            dni VARCHAR(8) NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            fecha_ingreso TEXT NOT NULL,
            activo INT NOT NULL
            );
        """
        cursor.execute(sql)
        # Make sure data is committed to the database
        cnx.commit()
        return cnx
    except mysql.connector.Error as err:
        print("Error al crear tabla: {}".format(err))
    finally:
        cnx.close()