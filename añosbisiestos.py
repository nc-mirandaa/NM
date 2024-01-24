x =input("Escoge un año entre 1900 y 2199:")
if int(x)>2199:
    print("Ese año no es válido")
    quit()
if int(x)<1900:
    print("Ese año no es válido")
    quit()
e = 0
if int(x)>2100:
    e=e+1
step1 =(int(x)-1900)
step2 =(step1//4)-e
print("Entre esos años hay ",(step2)," bisiestos")
