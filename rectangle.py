
class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b


    def is_valid(self) -> bool:
        """
        This method checks if the rectangle is valid
        
        Args:
            No
        Returns: 
            bool: True if the rectangle is valid, False otherwise
        """ 
        return self.a > 0 and self.b > 0


    def perimeter(self):
        """
        This method finds the perimeter of the rectangle.

        Args:
            No
        Returns:
            float or int: return perimeter of the rectangle if the rectangle is valid, 0 otherwise
        """
        if self.a > 0 and self.b > 0:
            P = 2 * (self.a + self.b)
            return P
        else: 
            return 0


    def area(self):   
        """
        This method finds the area of the rectangle.

        Args:
            No
        Returns:
            float or int:  return area of the rectangle if the rectangle is valid, 0 otherwise 
        """
        if self.a > 0 and self.b > 0:
            S = self.a * self.b
            return S
        else:
            return 0
        
x = Rectangle(-4, 5)
print(x.is_valid())
print(x.perimeter())
print(x.area())
