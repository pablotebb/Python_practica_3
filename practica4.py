frase = "Me gusta el aprendizaje, por lo tanto el objetivo, es que me guste más."
frase2 = "El viejo aprendizaje se basaba en molestar a la mente, para que no aprendiera y fuera sometida por otros (Tu no vales)."
frase3 = "Un nuevo aprendizaje es posible, donde la concentración y la expresividad, no sean herramientas del malestar."
frase4 = "Todo aprendizaje debe ser divertido para la mente."
frase5 = "El cambio de la mente, es el cambio del sistema." 
frase6 = "Mente feliz, mente potente."
frase7 = "El recuerdo es sólo posible, con una mente feliz."
frase8 = "La inteligencia es como un cachorro que juega y juega, y entonces el juego se transforma en el principio de una sociedad equilibrada."
frase9 = "La imaginación es el cachorro y la sociedad el objetivo"

print(frase, frase2, frase3, frase4, frase5, frase6, frase7, frase8, frase9)

print("\nLa frase: ", "\"", frase + frase2 + frase3 + frase4 + frase5 + frase6 + frase7 + frase8 + frase9, "\"", "\nEs de tipo: " + str(type(frase + frase2 + frase3 + frase4 + frase5 + frase6 + frase7 + frase8 + frase9)))

print(len(frase), len(frase2), len(frase3), len(frase4), len(frase5), len(frase6), len(frase7), len(frase8), len(frase9))

num = len(frase)

print("len(frase) es:", num)

print(frase)
print(frase[0], frase[1], frase[2], frase[3], frase[-2],frase[-1])

for i in frase:
  # print(i)
  print(f"{i}")
  
print(frase2)

print("frase2[5:10] ", frase2[5:10])
print("frase2[:10] ", frase2[:10])
print("frase2[5:] ", frase2[5:])
print("frase2[:] ", frase2[:])
print("frase2[:-1] ", frase2[:])
print("frase2[::-1] ", frase2[::-1])

