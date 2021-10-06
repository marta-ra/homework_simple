# Задача 3
# Реализовать класс точки в N мерном пространстве.
# Реализовать валидацию точки.
# Реализовать метод получения расстояния этой точки от точки начала координат до этой точки.
# Реализовать метод получение размерности.


# Реализовать класс прямой в N мерном пространстве(применить наследование от точки в н мерном пространстве).
# При инициализации объекта на вход будут приходить два кортежа, которые будут представлять точку A и точку B.

# Предусмотреть валидацию данных.
# Разработать метод подсчета расстояния между точками.
# Разработать метод переноса к началу координат. (то есть точка а становится началом координат, а точка B параллельно переносится. расстояние между точками измениться не должно)

# Примечания:
# точки прямой должны иметь один и тот же порядок\размерность
# для получения расстояния следует использовать расширенную теорему пифагора
# постараться сократить дупликацию кода


from typing import Coroutine


class Point:
    def __init__(self, n, *args): 
        self.space = n
        self.coordinate1 = args[0]
        self.coordinate2 = args[1]
        if self.space == 3:
            self.coordinate3 = args[2]

    def distance_to_center(self):
        if self.space == 2:
            distance = (self.coordinate1**2 + self.coordinate2**2)**0.5
        elif self.space == 3:
            distance = (self.coordinate1**2 + self.coordinate2**2 + self.coordinate3**2)**0.5
        return distance

    def dimension(self):
        return self.space

    def point_coordinate(self):
        if self.space == 2:
            return self.coordinate1, self.coordinate2
        elif self.space == 3:
            return self.coordinate1, self.coordinate2, self.coordinate3


    
class Line(Point):
    def __init__(self): 
        self.point1 = Point.point_coordinate(self)
        self.point2 = Point.point_coordinate(self)
    Определить линию (может на вход сразу координаты 2х точек?)   
 
    def line_length(self):
        if self.space == 2:
            distance = ((self.coordinate1)**2 + self.coordinate2**2)**0.5




point = Point(2, 3, 4)
dist = point.distance_to_center()
print(dist)
N = point.dimension()
print(N)

point1 = Point(3, 3, 4, 5)
dist1 = point1.distance_to_center()
print(dist1)
N = point1.dimension()
print(N)

