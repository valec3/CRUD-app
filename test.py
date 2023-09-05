class Empleado:
    def __init__(self, id_empleado, nombre, apellido, dni, fecha_nacimiento, fecha_ingreso, activo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.activo = activo

juan = Empleado(1, "Juan", "Perez", "12345678", "01/01/1990", "01/01/2010", 1)
print(tuple(juan.__dict__.values()))
