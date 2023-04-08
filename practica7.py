lista = ["uno", "tres", 5, "hola", "uno"]

print(lista)

print(len(lista))

print(type(lista))

print(lista[0])

print(lista[1])

print(lista[-1])

print(lista[0:3])

print(lista[2:])

print(lista[::-1])

print(lista)

lista[1] = "me meto aquí"

print(lista)


print(lista)

lista.append("soy el último")

print(lista)

print(lista)

lista.insert(1, "holi")

print(lista)


print(lista)

try:
  print(lista.index("me meto aquí"))
except: 
  print("parece que hay un error o no está ese elemento")
  

print(lista)


try:
  print(lista.pop())
  print(lista.pop(0))
  print(lista.pop(1))
except: 
  print("parece que hay un error o no está ese elemento")


print(lista)

lista.remove("hola")


print(lista)

lista.append(3)
lista.append(5)
lista.append(2)

print(lista)

lista2 = [5, 2, 3, 5, 1, 8]

lista3 = ["hola", "adios", "girafa", "cemento"]

lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)


print(lista)

# lista.clear()
print("-------------------------------------")
print(lista)
print(lista[::-1])

lista_copia = lista.copy()


lista.reverse()


print(lista)

print("copia de la lista: ", lista_copia)

# print(dir(lista))
print("El 5 aparece estas veces: ", lista_copia.count(5))