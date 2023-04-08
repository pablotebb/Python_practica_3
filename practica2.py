nombre = "Pablo"
edad = 37

def hola_nombre_dame_tu_edad():

  print(f"Hola {nombre}")

  print(f"Hola {nombre} tienes: {edad} anos")

  print("Hola " + nombre + " tienes: " + str(edad) + " anos")
  
hola_nombre_dame_tu_edad()

def hola_nombre_dame_tu_edad(param1="Pepe", param2=10):
  
  print(f"Hola {param1}")

  print(f"Hola {param1} tienes: {param2} anos")

  print("Hola " + param1 + " tienes: " + str(param2) + " anos")
  
hola_nombre_dame_tu_edad("Juanito", 46)

hola_nombre_dame_tu_edad(param2=46, param1="Juanito")

hola_nombre_dame_tu_edad()