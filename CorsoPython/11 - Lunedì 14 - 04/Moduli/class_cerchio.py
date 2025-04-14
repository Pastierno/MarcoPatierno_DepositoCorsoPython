PI = 3.14159

class Cerchio():
    def __init__(self, raggio):
        self.raggio = raggio
        
    def area_cerchio(self):
        return PI * (self.raggio ** 2)
    
    
            