# from abc import ABC,abstractmethod
#
# class button(ABC):
#
#     def __init__(self,link):
#         self.link = link
#
#     @abstractmethod
#     def click(self):
#         pass
#
#     @property
#     @abstractmethod
#     def link(self):
#         pass
#
# class PushButton(button):
#     def click(self):
#         print(f"Go To {self.link}")
#
#         @button.link.setter
#         def link(self,input):
#             self.__link = input
#
#         @link.getter
#         def link(self):
#             return self.__link
#
# tombol = PushButton('hello.py')
# tombol.click()
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Contoh kelas turunan dari Abstract Base Class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Akan menyebabkan error karena kita belum mengimplementasikan metode abstrak dari Shape
# shape = Shape()
# TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

square = Square(5)
print("Area:", square.area())  # Output: Area: 25
print("Perimeter:", square.perimeter())  # Output: Perimeter: 20
