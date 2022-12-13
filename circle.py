from math import pi

class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        
        Args:
            No
        Returns:
            bool: True if the circle is valid, False otherwise
        """
        return self.radius > 0
    
    def diameter(self):
        '''
        This method finds the diameter of the circle.

        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        if self.radius > 0:
            d = 2 * self.radius
            return d
        else:
            return 0
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.

        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        if self.radius > 0:
            C = 2 * pi * self.radius
            return C
        else:
            return 0
        

    
    def area(self) -> float:
        '''
        This method finds the area of the circle.

        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        if self.radius > 0:
            A = pi * (self.radius ** 2)
            return A
        else:
            return 0

x = Circle(-5)
print(x.is_valid())
print(x.diameter())
print(x.circumference())
print(x.area())