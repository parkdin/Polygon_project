from math import sqrt

class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        return self.a > 0 and self.b > 0 and self.c > 0

    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        ''' 
        a = self.a
        b = self.b
        c = self.c
        if a != b and a != c and b != c:
            return "A scelene triangle"
        if (a == b or a == c) or b == c:
            return "A isosceles triangle"
        if a == b and a == c and b == c:
            return "A equilateral triangle"
                    


    def perimeter(self):
    
        '''
        This method finds the perimeter of the triangle.

        Args:
            No
        Returns:
            int or float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.a > 0 and self.b > 0 and self.c > 0:
            P = self.a + self.b + self.c
            return P
        else: 
            return 0

    def area(self):
        '''
        This method finds the area of the triangle.

        Args:
            NO
        Returns:
            int or float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        
        a = self.a 
        b = self.b
        c = self.c
        s = (a + b + c) / 2
        Area = sqrt(s * (s - a) * (s -b) * (s -c))
        return Area
x = Triangle(3, 4, 5)
print(x.perimeter())
print(x.area())