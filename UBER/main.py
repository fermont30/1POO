from acount import Cuenta
from acount_driver import Driver
from acoun_User import User
from car import Car
from payment import Pago
from transfer import Transfer
from Route import Route
from trip import Trip
from uberfx import uberx
from ubercomfort import  ubercomfort
from uberX import uberx 


if __name__ == "__main__" : 
    usuario1 = User(1, "romeo", "masculino", 22222 , 999)
    user2 = User("josue", "homero", 1212121 , 233222 , 999)
    carro1 = Car("pbc-123", "2020","red" ,  Driver("Montoya", "masculino", 100, 99999999, 999646 , "Licencia"))
    ruta1 = Route([-21321321321, -12341654654],[564654 , -4654654] , "5km" , "20min")
    pagooo1 = Pago (1,"115-10-2022", 5555)
    conductor = Driver("homero", "masculino",100, 233222 , 999 , 9998)  
    """
    print (vars(carro_1))
    print (vars(carro_1.drive)) 
    pagooo1 = Transfer ( 1,1,"115-10-2022", 5555 , "pichincha" , [4546545 , 20,"josue" , 54584])
    print(vars(pagooo1))
   
    print( vars(pagooo2))
   
    print( vars(ruta_uno))
    """

     
     
    trip002 = Trip(Car("pbc-123", "2020","red" ,  Driver("Montoya", "masculino", 100, 99999999, 999646 , "Licencia")), Driver("homero", "masculino",100, 233222 , 999 , 9998), User("josue", "homero", 1212121 , 233222 , 999), Route([-21321321321, -12341654654],[564654 , -4654654] , "5km" , "20min"),  Pago(1,"115-10-2022", 5555))
   
    print(vars(trip002))
    print(vars(trip002.driver))
    print(vars(trip002.car))
    print(vars(trip002.user))
    print(vars(trip002.route))
    print(vars(trip002.pago))
    
    
    #trip001 = Trip(carro1, conductor, usuario1 , ruta1 , pagooo1 )
    #print(vars(trip001.car.drive))
    
    
    
    
    