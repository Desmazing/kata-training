"""The constructor should take an array as an argument,
this will contain 3 integers of the form [width, length, height]
from which the Block should be created."""


import math


class Block():
    """Class to create a block"""
    def __init__(self,arr):
        self.arr = arr
    def get_width(self):
        """method to return the block width"""
        return self.arr[0]
    def get_length(self):
        """method to return the block length"""
        return self.arr[1]
    def get_height(self):
        """method to return the block height"""
        return self.arr[2]
    def get_volume(self):
        """method to return the block volume"""
        return math.prod(self.arr)
    def get_surface_area(self):
        """method to return the block surface area"""
        w,l,h = self.arr
        return 2 * ((w*l) + (l*h) + (w*h))
