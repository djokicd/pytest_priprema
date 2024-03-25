import numpy as np 

class sabirac:
    def __init__(self, maxVal):
        self.maxVal = maxVal
    
    def saberi(self, a, b):
        self.rezultat = a + b
        if self.rezultat >= self.maxVal:
            self.rezultat = 0
        return self.rezultat
 
    


    
