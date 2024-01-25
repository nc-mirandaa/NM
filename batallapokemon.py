import random #para decidir el ataque del oponente
#batalla
PS_jugador=100 #puntos de salud del jugador
PS_oponente=100
defensa_oponente=100
defensa_jugador=100

ataques=['latigo','ascuas','placaje']

while PS_jugador>0 and PS_oponente>0:
    ataque_jugador= ""
    while ataque_jugador=="":
        ataque_jugador = input("Introduzca el ataque: ")
        if ataque_jugador =="malisioso":
            defensa_oponente-=10
            ataque_jugador=""
            print("la vida de tu oponente es: ", defensa_oponente)
        elif ataque_jugador=="placaje":
            PS_oponente-=35/defensa_oponente/100
            ataque_jugador=""
            print("la vida de tu oponente es: ", PS_oponente)
        elif ataque_jugador=="ascuas":
            PS_oponente-=20
            ataque_jugador=""
            print("la vida de tu oponente es: ", PS_oponente)
        else:
            print("Que estas haciendo? tus ataque son","malicioso, placaje y ascuas")
        #No borramos ataque_jugador para que vuelva a preguntar
    #el jugador ha atacado, le toca al oponente
    
    while not ataque_jugador=="":
         ataque_oponente =""
         ataque_oponente = random.randrage(1,1+3)
         if ataque_oponente==1: #latigo
             defensa_jugador-=10
             print(ataques[0],"lo uso tu oponente")
         elif ataque_oponente==2: #placaje
             PS_jugador-=35 * defensa_jugador/100
             print(ataques[1],"lo uso tu oponente")
         elif ataque_oponente==3:
             PS_jugador-=40
             print(ataques[2],"lo uso tu oponente")
             #randrange garantizado a ser uno de estos 3 valore

#La batalla ha terminado
if PS_oponente<=0 and PS_jugador<=0:
    print("empate")
elif PS_jugador>=0:
    print("felicidades, has ganado")
elif PS_jugador<=0:
    print("Lo siento, has perdido")
