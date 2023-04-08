def dame_hola_mundo():
  print("Hola mundo")
  print("Hola mundo cruel!!", "Hola mundo asqueroso!!")
  print("hola", "mundo", "bonito!!!")
  
dame_hola_mundo()

def dame_hola_mundo_con_parametros(msg1="holi", msg2 = [], msg3 = []):
  print(f"{msg1}")
  print(f"{msg2[0]}, {msg2[1]}")
  print(f"{msg3[0]}, {msg3[1]}, {msg3[2]}")
  
dame_hola_mundo_con_parametros("Hola mundo", msg2=["Hola mundo cruel!!", "Hola mundo asqueroso!!"], msg3=["hola", "mundo", "bonito!!!"])
