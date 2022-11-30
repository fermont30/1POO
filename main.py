print ("Hola Mundo")
 
 class persona:
     nombre = str
     edad = int
     
     def __init__ (self, nombre, edad):
         self.nombre  = nombre
         self.edad  = edad
         
     def saluda (self, otra_persona)    
        return 'hola {otra_persona.nombre}, me llamo {self.nombre}.'
         
     if __name__ == "__main__"      
        david = persona("david", 30) 
        maria = persona("maria", 20)
        
        print(david)
        print(maria)   
         