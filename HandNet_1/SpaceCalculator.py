from typing import NamedTuple
import collections
import numpy as np
class Vector:
    def __init__(self, p1:NamedTuple, p2:NamedTuple):
        self.p1 = p1
        self.p2 = p2
        vec = collections.namedtuple("direction vector", "x y z")
        self.direction_vec = vec((p1.x-p2.x, p1.y-p2.y, p1.y-p2.y))
    def findPoint(self, point:NamedTuple):
        pass


def getAngle(vec1:Vector, vec2:Vector):
    pass