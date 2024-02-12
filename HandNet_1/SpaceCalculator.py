from typing import NamedTuple
import collections
import numpy as np

class Vector:
    """Class for vectors to represent model of hand created by the neural network\n
    Vector.p to get <x0, y0, z0> location of vector obj.\n
    Vector.direction_vec to get direction of vector.\n
    Vector.get_scale_to_point(*point to find here*) will check if the point in params lies on the vector obj. If it does, 
    will return the scalar needed to get to the point, otherwise will return None.\n
    Vector.scale(*scale*) returns point on the vector with the given scalar."""
    def __init__(self, p1:NamedTuple, p2:NamedTuple):
        self.p = p1
        self.dirVecTuple = collections.namedtuple("direction_vector", "x y z")
        self.pointTuple = collections.namedtuple("point", "x y z")
        self.direction_vec = self.dirVecTuple(self.p.x-p2.x, self.p.y-p2.y, self.p.y-p2.y)
    def get_scale_to_point(self, point:NamedTuple):
    #<x, y, z> = <x0, y0, z0> + t<direction_vec>
    #t = (x-x0)/direction_vec.x    
        a = (point.x-self.p.x)/self.direction_vec.x
        s = self.scale(a)
        if (s.x == point.x and s.y == point.y and s.z == point.z):
            return a
        return None
    def scale(self, t_scale):
        return self.pointTuple((self.direction_vec.x*t_scale)+self.p.x, (self.direction_vec.y*t_scale)+self.p.y, (self.direction_vec.z*t_scale)+self.p.z)
    def __str__(self) ->str:
        return f'<x, y, z> = {self.p} + t<{self.direction_vec.x}, {self.direction_vec.y}, {self.direction_vec.z}>'
    
class VectorCalculator:
    """Class for vector operations to make code more readable.\n
    For all functions: vec1 *operation* vec2"""
    def __init__(self):
        self.vectorTuple = collections.namedtuple("vector", "x y z")
    def divide(self, vec1:Vector, vec2:Vector):
        return self.vectorTuple(vec1.x/vec2.x, vec1.y/vec2.y, vec1.z/vec2.z)
    def multiply(self, vec1:Vector, vec2:Vector):
        return self.vectorTuple(vec1.x*vec2.x, vec1.y*vec2.y, vec1.z*vec2.z)
    def add(self, vec1:Vector, vec2:Vector):
        return self.vectorTuple(vec1.x-vec2.x, vec1.y-vec2.y, vec1.z-vec2.z)
    def subtract(self, vec1:Vector, vec2:Vector):
        return self.vectorTuple(vec1.x+vec2.x, vec1.y+vec2.y, vec1.z+vec2.z)



def three_D_dist(p1:NamedTuple, p2:NamedTuple):
    """Returns dist from p1 to p2, assuming p1 and p2 are 3 points on a 3 dimensional plane"""
    return abs(np.sqrt(np.square(p2.x-p1.x)+np.square(p2.y-p1.y)+np.square(p2.z-p1.z)))

    

def calcAngle(vec1:Vector, vec2:Vector, int_point:NamedTuple):
    """Returns angle between vec1 and vec2 IF they intersect at int_point.\n
    If they do not intersect at int_point, returns None type"""
    
    #make sure vec1 and vec2 both exist at int_point
    if (vec1.get_scale_to_point(int_point)==None or vec2.getScale_to_point(int_point)==None): return None
    

    point = collections.namedtuple("point", "x y z")
    l1 = three_D_dist(int_point, vec1.p)
    l2 = three_D_dist(int_point, vec2.p)
    l3 = three_D_dist(vec1.p, vec2.p)
    theta = np.arccos((np.square(l1) + np.square(l2) - np.square(l3)) / (2*l1*l2))
    return theta

