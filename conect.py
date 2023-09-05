import mysql.connector

def conectar():    
    try:
        cnx = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "toor",
            database = "empresa_tuto"
        )
        if cnx.is_connected():
            print("Conexión exitosa a la base de datos.")
        else:
            print("No se pudo conectar a la base de datos.")
        return cnx
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos: {}".format(err))
        return None
    
        
def create_table_empleados():
    cnx = conectar()
    cursor = cnx.cursor()
    try:
        sql = """
            CREATE TABLE IF NOT EXISTS empleados (
            id_empleado INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(20) NOT NULL,
            apellido VARCHAR(20) NOT NULL,
            dni VARCHAR(8) NOT NULL UNIQUE,
            fecha_nacimiento TEXT NOT NULL,
            fecha_ingreso TEXT NOT NULL,
            activo INT NOT NULL
            );
        """
        cursor.execute(sql)
        # Make sure data is committed to the database
        cnx.commit()
    except mysql.connector.Error as err:
        print("Error al crear tabla: {}".format(err))
    finally:
        cnx.close()

create_table_empleados()