# Cree una versión modificada de su programa anterior en la que las clases que halla definido (Barco, Avión, Carro, etc.) 
# hereden de una clase general "Vehicle". Trate de que hereden todo lo que sea posible.

class vehiculos:
    def _init_(self, color, ano):
        self.color = color
        self.ano = ano
    def mostrar(self):
        return "Color : {}, Ano : {}".format(self.color, self.ano)
    
class barco(vehiculos):
    def _init_(self, color, ano, puertas):
        super()._init_(color, ano)
        self.puertas = puertas
    def mostrar(self):
        return "Color :  {}, Ano : {}, Puertas : {}".format(self.color, self.ano, self.puertas)
    
class avion(vehiculos):
    def _init_(self, color, ano, pasajeros):
        super()._init_(color, ano)
        self.pasajeros = pasajeros
    def mostrar(self):
        return "Color : {}, Ano : {}, Pasajeros : {}".format(self.color, self.ano, self.pasajeros)
    
class carro(vehiculos):
    def _init_(self, color, ano, marca, modelo):
        super()._init_(color, ano)
        self.marca = marca
        self.modelo = modelo
    def mostrar(self):
        return "Color : {}, Ano : {}, Marca : {}, Modelo : {}".format(self.color, self.ano, self.marca, self.modelo)
    
print("Ingrese los datos del Vehiculo:")
tipovehi = input("Tipo de vehiculo (c=Carro / b=Barco / a=Avión): ")

if tipovehi == 'b':
    Barco = barco(input("Color: "), input("Ano: "), input("Puertas: "))
    print(Barco.mostrar())

elif tipovehi == 'a':
    Avion = avion(input("Color: "), input("Ano: "), input("Pasajeros: "))
    print(Avion.mostrar())
  
elif tipovehi == "c" :
    Carro = carro(input("Color: "), input("Ano: "), input("Marca: "), input("Modelo: "))
    print(Carro.mostrar())
    
else: 
    print("No eligio una opcion")