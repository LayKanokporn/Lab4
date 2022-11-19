#Lab 4 Exercise.1 1630902656 Kanokporn Hudsree
class cylinder():
    def __init__(self,R,H):  
        self.radius = R
        self.height = H
    
    def Calculate(self):
        Calculate = 3.14 * ((self.radius**2) * self.height)
        return Calculate 

First = cylinder(5,10)
print("First: ",First.Calculate())
Second = cylinder(7,13)
print("Second: ",Second.Calculate())
