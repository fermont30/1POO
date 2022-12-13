from acount_driver import Driver
class Car : 
    placa = str
    ao = int
    color = str
    drive = Driver("","","","","","")
   
    def __init__(self , placa , ao , color, driver):
        super().__init__ 
        self.placa = placa
        self.ao= ao
        self.color = color 
        
        self.drive = driver
        
    