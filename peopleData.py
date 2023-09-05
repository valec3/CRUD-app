import conect as con
from empleado import Empleado

def save(people:object):
    respuesta={}
    try:
        cnx = con.conectar()
        cursor = cnx.cursor()
        fields = ",".join(tuple(people.__dict__.keys()))
        values = tuple(people.__dict__.values())
        SQL_ADD_PEOPLE = f"INSERT INTO empleados ({fields}) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(SQL_ADD_PEOPLE, values)
        cnx.commit()
        print(f"Se guardaron {cursor.rowcount} registros")
        if cursor.rowcount > 0:
            respuesta= {"respuesta":True, "mensaje":"Datos guardados correctamente"}
        else:
            respuesta= {"respuesta":False, "mensaje":"Error al guardar datos"}
        
        cursor.close()
    except Exception as e:
        if "Duplicate entry" in str(e):
            msg = "ya existe una persona con este DNI" if "dni" in str(e) else "ya existe una persona con este ID"
        print(f"Error al guardar datos: {e}")
        respuesta= {"respuesta":False, "mensaje":f"Error {msg}"}
    finally:
        cnx.close()
        
    return respuesta

def find_all_records():
    try:
        cnx = con.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM empleados")
        people = cursor.fetchall()
        
        cursor.close()
        if people:
            return {"respuesta":True, "mensaje":"Datos listados correctamente", "data":people}
        return {"respuesta":False, "mensaje":"No hay datos para listar", "data":[]}
    except  Exception as e:
        print(f"Error al listar datos: {e}")
        return {"respuesta":False, "mensaje":f"Error al listar datos: {e}"}
    finally:
        print("Cerrando conexión...")
        cnx.close()
        
def search_dni(dni):
    try:
        cnx = con.conectar()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM empleados WHERE dni = %s", (dni,))
        found_people = Empleado(cursor.fetchone())
        cursor.close()
        if found_people.id_empleado:
            return {"respuesta":True, "mensaje":"Se encontró a la persona:", "data":found_people}
        else:
            return {"respuesta":False, "mensaje":"No se pudo encontrar a la persona con este dni", "data":[]}
    except  Exception as e:
        print(f"Error al buscar por dni: {e}")
        return {"respuesta":False, "mensaje":f"Error al listar datos: {e}"}
    finally:
        print("Cerrando conexión...")
        cnx.close()
def update_data(people:object):
    try:
        cnx = con.conectar()
        cursor = cnx.cursor()
        SQL_UPDATE_PEOPLE = """
                            UPDATE empleados SET
                            nombre = %s,
                            apellido = %s,
                            dni = %s,
                            fecha_nacimiento = %s,
                            fecha_ingreso = %s,
                            activo = %s
                            WHERE id_empleado = %s
                        """

        data = (
            people.nombre,
            people.apellido,
            people.dni,
            people.fecha_nacimiento,
            people.fecha_ingreso,
            people.activo,
            people.id_empleado
        )
        cursor.execute(SQL_UPDATE_PEOPLE, data)
        modified = cursor.rowcount>0
        # Confirmamos la ejecución de la consulta
        cursor.close()
        cnx.commit()
        
        return {"respuesta":True, "mensaje":"Datos actualizados correctamente"}
        
    except Exception as e:
        print(f"Error al actualizar datos: {e}")
        return {"respuesta":False, "mensaje":"No se pudo actualizar los datos"}
        
    finally:
        cnx.close()