import peopleData as perDt

class Empleado:
    def __init__(self, id_empleado = None,nombre = None, apellido=None, dni=None, fecha_nacimiento=None, fecha_ingreso=None, activo=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido=apellido,
        self.dni=dni,
        self.fecha_nacimiento=fecha_nacimiento,
        self.fecha_ingreso=fecha_ingreso,
        self.activo=activo

juan    = Empleado(1,"Juan","Perez","12345678","01/01/1990","01/01/2010",1)


res = perDt.save(juan)

print(res)