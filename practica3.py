
def dame_tipo_variable(variable):
  return f"{variable} es de tipo: {type(variable)}"

print(dame_tipo_variable("Pablo"))
print(dame_tipo_variable(33))
print(dame_tipo_variable(-34))
print(dame_tipo_variable(None))
print(dame_tipo_variable(True))
print(dame_tipo_variable([1, 2, 3, "hola", ("pepe", "juana", 1)]))
print(dame_tipo_variable((1, 2, 3, "hola")))
print(dame_tipo_variable({"nombre": "pablo", "apellidos": "jimenez", "edad": 38}))

    