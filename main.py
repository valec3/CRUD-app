from empleado import Empleado
from peopleData import save, find_all_records, search_dni, update_data

# res=save(juan)
# print(res)
# res=find_all_records()
# for i in res.get("data"):
#     print(i)

juan = Empleado(2, "Pedro", "manfred", "12345678", "01/01/1990", "01/01/2010", 1)
res = update_data(juan)
print(res)
# print(res["data"].__dict__.values())