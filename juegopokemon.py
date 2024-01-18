x =input("Eres chico o chica?")
w="Bienvenid"
if x == "chico":
    w += 'o'
else:
    w += 'a'
print(w, "al mundo de los pokemon!")
y =input("Que edad tienes?")
if int(y)<10:
    if x == "chico":
      print("No tienes edad", "para ser entrenador")
    else:
     print("No tienes edad", "para ser entrenadora")
reg = input("Necesitarás un compañero de viaje. En qué región te encuentras?")
if reg=="Kanto" and x=="chico":
   print("Tu compañera de viaje es Misty!")
else:
   print("Tu compañero de viaje es Brook!")
tipo = input("Qué tipo de pokemon quieres para empezar?")
if tipo=="agua":
   print("Tu starter es Oshawott")
elif tipo=="fuego":
   print("Tu starter es Cyndaquil")
else:
   print("Tu starter es Rowlet")