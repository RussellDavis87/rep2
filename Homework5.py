# Задание 2 (на создание новых классов)
# Создать классы
# 1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
# Методы:
# 1.	вычисляем площадь,
# 2.	вычисляем периметр.
# 2) Точка на карте (свойства: X, Y).
# Методы:
# 1.	Нужно вычислить расстояние до начала координат,
# 2.	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
# 3.	** перевод в другие системы координат
#
# 3) Для всех классов сделайте __str__, чтоб объекты красиво выводились на экран!



class Rectangle:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.tL = topLeft
        self.tR = topRight
        self.bL = bottomLeft
        self.bR = bottomRight
    def perim(self):
        return (2 * (self.tL + self.tR)) + (2 * (self.bL + self.bR))
    def area(self):
        return (self.tL + self.tR) * (self.bL + self.bR)
    def position(self):
        return (self.tL, self.tR, self.bL, self.bR)
    def __str__(self):
        return "Rectangle(%s, %s, %s, %s)" % (self.tL, self.tR, self.bL, self.bR)

r1 = Rectangle (5, 5, 10, 10)
print(r1)
print("Perimeter: %s" % r1.perim())
print("Area: %s" % r1.area())
print("Position: (%s, %s, %s, %s)" % r1.position())