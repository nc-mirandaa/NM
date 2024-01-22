x =input("Escoge un año entre 1900 y 2199:")
if int(x)>2199:
    print("Ese año no es válido")
    quit()
if int(x)<1900:
    print("Ese año no es válido")
    quit()
i=int(x)
y=0
while i>=1900:
    if i%4==0 and i%100!=0:
        y+=1
    elif i%100==0 and i%400==0:
        y+=1
    else:
        y+=0
    i-=1    
print("Entre esos años hay ",(y)," bisiestos")
    
