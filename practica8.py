mi_tupla = ("pepe", "ana", "rosa", 5, 3, 1, 5, "rosa")

print(mi_tupla)

print(len(mi_tupla))

try:
  mi_tupla[1] = "esto no se mete y da error"
except TypeError as e:
  print(f"Las Tuplas no pueden ser modificadas (son inmutables). Error: {e}")
  


print(mi_tupla)

print(f"El 5 en la tupla, se repite estas veces: {mi_tupla.count(5)}")
print(f"'ana' en la tupla, se repite estas veces: {mi_tupla.count('ana')}")
print(f"'jon' en la tupla, se repite estas veces: {mi_tupla.count('jon')}")


print("El primer 5 aparece en la posición: ", mi_tupla.index(5))
print("'pepe' aparece en la posición: ", mi_tupla.index('pepe'))
try:
  print("'ernesto' aparece en la posición: ", mi_tupla.index('ernesto'))
except:
  print("Parece que 'ernesto' no se encuentra en la Tupla")
  
  
print(dir(mi_tupla))

print(mi_tupla)

print(mi_tupla[1])
print(mi_tupla[0:])
print(mi_tupla[::-1])

try:
  del mi_tupla[1]
except:
  print("No se puede borrar un elemento de una Tupla")
  
print(mi_tupla)
