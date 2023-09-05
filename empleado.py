class Empleado:
    def __init__(self, 
                id_empleado = "",
                nombre = "", 
                apellido="", 
                dni="", 
                fecha_nacimiento="", 
                fecha_ingreso="", 
                activo=""):
        
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido=apellido
        self.dni=dni
        self.fecha_nacimiento=fecha_nacimiento
        self.fecha_ingreso=fecha_ingreso
        self.activo=activo

