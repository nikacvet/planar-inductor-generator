import math
from typing import List


class Coordinates():
    """
    A class that helps with the calculation of coordinates.

    ...

    Attributes
    ----------
    x : int
        x coordinate
    y : int
        y coordinate
    outline : List
        list of all coordinates
    x_down: int
        first via x coordinate
    y_down:
        first via y coordinate

    Methods
    -------
    create_coordinates(self, n:int, w:int, s:int, d_out:int, d_tmp:int) -> List:
        Creates first layer coordinates.
    rotate(self, coords:List, x_pivot:int, y_pivot:int, angle:int) -> List:
        Rotates coordinates.
    """
    def __init__(self) -> None:
        """
        Constructs all the necessary attributes.

        Parameters
        ----------
            x : int
                x coordinate
            y : int
                y coordinate
            outline : List
                list of all coordinates
            x_down: int
                first via x coordinate
            y_down:
                first via y coordinate
        """
        self.x = 0
        self.y = 0
        self.outline = []
        self.x_down = 0
        self.y_down = 0
        

    def create_coordinates(self, n:int, w:int, s:int, d_out:int, d_tmp:int) -> List:
        """
        Creates list with coordinates of the initial metal.
            Parameters:
                n: number of turns
                w: width
                s: space between
                d_out:
                d_tmp: holds initial d_out value
        """

        self.outline.append((self.x,self.y))
        self.x,self.y = d_out+self.x,self.y
        self.outline.append((self.x,self.y))
        self.x,self.y = self.outline[len(self.outline)-1][0],d_out + self.y
        self.outline.append((self.x,self.y))
        self.x,self.y = (self.outline[len(self.outline)-1][0])-d_out,self.outline[len(self.outline)-1][1]
        self.outline.append((self.x,self.y))


        orientation = ["down","right","up","left"]
        count = 2

        for _ in range(n-1):
            for direction in orientation:
                if count % 2 == 0:
                    d_out = d_out - (w+s)
                    count = 0
                if direction == "down":
                    self.x, self.y = self.x, self.y - d_out
                elif direction == "up":
                    self.x, self.y = self.x, self.y + d_out
                elif direction == "right":
                    self.x, self.y = self.x + d_out, self.y
                elif direction == "left":
                    self.x, self.y = self.x - d_out, self.y
                count += 1
                self.outline.append((self.x,self.y))


        d_out = d_out - (w+s)


        self.x,self.y = self.x,self.y - ((d_tmp / 2 - ((n-1)*w+(n-1)*s)) + (w / 2))
        self.x_down,self.y_down = self.x,self.y
        self.outline.append((self.x,self.y))
        self.x, self.y = self.x + w, self.y
        self.outline.append((self.x,self.y))
        d_out = d_out - w
        self.x,self.y = self.x,self.y + ( (d_tmp / 2 - ((n-1)*w+(n-1)*s)) + (w / 2)) - w
        self.outline.append((self.x,self.y))


        orientation = ["right","down","left","up"]

        count = 0
        d_out = d_out +s

        for _ in range(n-1):
            for direction in orientation:
                if direction == "down":
                    self.x, self.y = self.x, self.y - d_out
                elif direction == "up":
                    self.x, self.y = self.x, self.y + d_out
                elif direction == "right":
                    self.x, self.y = self.x + d_out, self.y
                elif direction == "left":
                    self.x, self.y = self.x - d_out, self.y
                count += 1
                if count % 2 == 0:
                    d_out = d_out + (w+s)
                    count = 0
                self.outline.append((self.x,self.y))


        self.x, self.y = self.x + d_out, self.y
        self.outline.append((self.x,self.y))
        self.x, self.y = self.x, self.y - d_out
        self.outline.append((self.x,self.y))
        d_out = d_out + w
        self.x, self.y = self.x - d_out, self.y
        self.outline.append((self.x,self.y))
        self.x, self.y = self.x, self.y - w
        self.outline.append((self.x,self.y))
    
    # To rotate an object
    def rotate(self, coords:List, x_pivot:int, y_pivot:int, angle:int) -> List:
        """
        Rotates points in given array.
            Parameters:
                coords: current coordinates
                x_pivot: 
                y_pivot: 
                angle: angle of shifting
            Returns:
                rotated_points: shifted points
        """
        sin = int(math.sin(angle * math.pi / 180))
        cos = int(math.cos(angle * math.pi / 180))
        shifted_points = [(x - x_pivot, y - y_pivot, z) if z else (x - x_pivot, y - y_pivot) for x, y, *z in coords]

        rotated_points = [(x_pivot + (x * cos - y * sin), y_pivot + (x * sin + y * cos), z) \
                        if z \
                        else (x_pivot + (x * cos - y * sin), y_pivot + (x * sin + y * cos)) for x, y, *z in shifted_points]
        return rotated_points
    



        



