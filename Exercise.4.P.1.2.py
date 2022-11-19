#Lab 4 Exercise.2 1630902656 Kanokporn Hudsree
class pyramid():
    def __init__(self,L,W,H):
        self.length = length_Class(L)
        self.width = width_Class(W)
        self.height = height_Class(H)
    def Calculate(self):
        Calculate = (self.length.l*self.width.w*self.height.h) / 3
        return Calculate

class length_Class():
    def __init__(self,L):
        self.l = L
        
class width_Class():
    def __init__(self,W):
        self.w = W
        
class height_Class():
    def __init__(self,H):
        self.h = H
        
First_pyramid = pyramid(10,7,17)
print("First: ",First_pyramid.Calculate())
