import numpy as np

#ALL ONLY FOR 3 DIMENSIONAL VECTORS

class Vector:
    def __init__(self, p1, p2, name):
        #will create using p2 as the origin
        self.name = name
        self.x = p1.x
        self.y = p1.y
        self.z = p1.z
        m = np.sqrt(np.square(self.x) + np.square(self.y) + np.square(self.z))
    def __str__(self):
        return f'Vector {self.name} = {self.x}I + {self.y}J + {self.z}K where I, J K are basis vectors'


def dotProduct(vec1: Vector, vec2: Vector):
    """dot product of vec1 and vec2"""
    res = 0
    res+=(vec1.x*vec2.x)
    res+=(vec1.y*vec2.y)
    res+=(vec1.z*vec2.z)
    return res

def angle_between(vec1:Vector, vec2: Vector):
    #vecA DOT vecB = ||a||(||b||)cos(theta)
    return np.arccos(dotProduct(vec1, vec2)/(vec1.m * vec2.m))
