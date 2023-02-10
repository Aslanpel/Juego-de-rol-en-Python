nombre = input(str("Como te llamas "))
if nombre == "Aslanpel":
  print ("Hola Aslanpel")
if nombre == "2/2/22":
  while nombre == "2/2/22":
    print ("22222222222222222222222222222222222222222222222222")
else:
  print (f"Hola {nombre}")

objetos = ["Pala", "Espada", "Filete"]
print (f"Tus cosas: {objetos}")

life = 100


print (f"vida {life}")

quest1 = input (str("Bien, hay 2 caminos: Izquierda y Derecha, ¿A donde vas? (responde con izq o der) "))

if quest1 == "izq":
  print ("Vas a la izquierda")
  print ("El camino de la izquierda es oscuro")
  print ("Hay algo en el suelo")
  quest1iz = input (str("Cogerla? "))
  if quest1iz == "si":
    print ("Es una linterna")
    objetos.append ("Linterna")
    print (f"tus objetos {objetos}")
    print ("Ves un monstruo que te ataca y te quita 99 de vida")
    life = 1
    print (life)
    ded = input (str("Atacar o Huir? "))
    if ded == "Huir":
      print ("Huyes")
      print ("Ves un edificio")
      print ("ES TU CASA!!!")
      print ("FINAL BUENO")
    if ded == "Atacar":
      print ("El monstruo te ataca a ti tambien")
      life = 0
      print ("HAS MUERTO")

  
  if quest1iz == "no":
    print ("dejas el objeto en el suelo")
    print (f"tus objetos {objetos}")
    print ("Esta oscuro, y caes por un barranco")
    life = 0
    print (f"Vida:{life}")
    print ("HAS MUERTO")
    

if quest1 == "der":
  print ("Vas a la derecha")
  print ("Te han tendido una emboscada")
  print ("HAS MUERTO")
