print("Hola Mundo")
 
class persona:
     nombre = str
     edad = int
     
     def __init__ (self, nombre, edad):
         self.nombre  = nombre
         self.edad  = edad
         
     def saluda (self, otra): 
        self.otra  = otra            
        return 'hola {otra.nombre}, me llamo {self.nombre}.'
         
if __name__ == "__main__" :     
        david = persona("david", 30) 
        maria = persona("maria", 20)
        
        print(david)
        print(maria)   
     
class Miclase:
    nombre = str
    edad = int
p1 = Miclase()   
print(p1.nombre)

class persona2:
    nombre = str
    edad = int
    genero = str
    
    def __init__(self, nombre, edad, genero):
       self.nombre = nombre
       self.edad = edad
       self.genero = genero
       
p2 = persona2(Diego, 29, "masculino")

print(p2.nombre)
print(p2.edad)
print(p2.genero)
        
# la funcion __str__()

class persona3:
    nombre = str
    edad = int
    genero = str
    estatura = int
    
    def __init__(self):
       self.nombre = nombre
       self.edad = edad
       self.genero = genero
       self.estatura = estatura
        
    def __str__(self):
        return('Hola me llamo {self.nombre}, tengo {self.edad}, mi genero es {self.genero}, y estatura {self.estatura}')    
    
p3 = persona3("juan", 21, "Masculino", 189)    

print(p3)

# Metodos dentro de obgetos

class persona4:
    nombre = str
    semestre = str
    
    def __init__(self, nombre, semestre):
        self.nombre = nombre
        self.semestre = semestre
        
    def saludo(self):
        print("Bienvenido" + self.nombre + "al" + self.semestre)
        
p4 = persona4("antonio", "segundo")
p4.saludo()

p4.nombre = "Jonathan"            
p4.saludo()

          
    


    
    
     
        
            