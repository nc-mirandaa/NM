class Vehicle:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand, self.model, self.color, self.year)

x = input("Elige que opcion de carro quieres (solo puedes poner 1 o 2): ")

carro1 = Vehicle("Toyota", "R4", "verde", 2000)
carro2 = Vehicle("Volkswagen", "Beetle", "blue", 1990)

if int(x)==1:
    print("Carro: ", carro1.show_attr())
else:
    print("Carro: ", carro2.show_attr())

class Ship:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand, self.model, self.color, self.year)

x = input("Elige que opcion de barco quieres (solo puedes poner 1 o 2): ")

barco1 = Ship("Jeanneau", "NC", "blanco", 2018)
barco2 = Ship("Hanse", "630e", "negro", 2006)

if int(x)==1:
    print("Carro: ", barco1.show_attr())
else:
    print("Carro: ", barco2.show_attr())

class Airplane:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand, self.model, self.color, self.year)

x = input("Elige que opcion de barco quieres (solo puedes poner 1 o 2): ")

avion1 = Airplane("Cessna", "Citation Mustang", "blanco", 2007)
avion2 = Airplane("Dassault Aviation", "Falcon 100", "blanco", 1984)

if int(x)==1:
    print("Carro: ", avion1.show_attr())
else:
    print("Carro: ", avion2.show_attr())
