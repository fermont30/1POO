from archivo1 import Pais
from archivo2 import Provincia

# HERENCIA SIMPLE DENTRO DEL MISMO ARCHIVO

class Padre1:
    nombre   = str
    apellido = str
    edad     = int

    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad

class Hijo1(Padre1):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad = ciudad

#HERENCIA SIMPLE CON METODOS

class Padre2:
    nombre   = str
    apellido = str
    edad     = int

    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad

    def __str__(self):
        return f'Hola {self.nombre} {self.apellido}, tu edad es {self.edad}'

class Hijo2(Padre2):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad = ciudad


#HERENCIA DE CLASES CON OBJETOS
class Continente(Pais):
    nombre                  = str
    habitantesContinente    = int
    areaContinente          = int
    pais                    = Pais("", "", "", "")
    
    def __init__(self, nombre, habitantesContinente, areaContinente, pais):
        self.nombre                 = nombre
        self.habitantesContinente   = habitantesContinente
        self.areaContinente         = areaContinente
        self.pais                   = pais

if __name__ == "__main__":

    objeto1 = Hijo1("Fernando", "Montoya", 30, "Quito")
    print(vars(objeto1))
    
    objeto2 = Hijo2("Fernando", "Montoya", 30, "Quito")
    print(objeto2)
    
    objeto3 = Continente("America", 800046546, 1400006546500, Pais("Ecuador", "Quito", 51012365, Provincia("Pinchincha", 4513213456, "Quito", 648931564)))
    print(vars(objeto3))
    print(vars(objeto3.pais))
    print(vars(objeto3.pais.provincia))
    
    