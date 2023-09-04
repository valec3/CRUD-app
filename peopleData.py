import conect as con

def save(people:object):
    respuesta={}
    try:
        cnx = con.conectar()
        cursor = cnx.cursor()
        fields = people.__dict__.keys()
        values = people.__dict__.values()
        SQL_ADD_PEOPLE = f"INSERT INTO empleados ({fields}) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(SQL_ADD_PEOPLE, (values))
        cnx.commit()
        
        if cursor.rowcount:
            respuesta= {"respuesta":True, "mensaje":"Datos guardados correctamente"}
        else:
            respuesta= {"respuesta":False, "mensaje":"Error al guardar datos"}
        
        cursor.close()
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        respuesta= {"respuesta":False, "mensaje":f"Error {str(e)}"}
    finally:
        cnx.close()
    return respuesta
