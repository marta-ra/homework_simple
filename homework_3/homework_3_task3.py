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


class Point:
    def __init__(self, n, *args): 
        self.space = int(n)
        self.coordinate1 = int(args[0])
        self.coordinate2 = int(args[1])
        if self.space == 3:
            self.coordinate3 = int(args[2])
            
# расстояние до центра:
    def distance_to_center(self):
        if self.space == 2:
            distance = (self.coordinate1**2 + self.coordinate2**2)**0.5
        elif self.space == 3:
            distance = (self.coordinate1**2 + self.coordinate2**2 + self.coordinate3**2)**0.5
        return distance

# вывод размерности:
    def dimension(self):
        return self.space

    def point_coordinate(self):
        if self.space == 2:
            return self.coordinate1, self.coordinate2
        elif self.space == 3:
            return self.coordinate1, self.coordinate2, self.coordinate3
    
    
class Line(Point):
    # С помощью наследования создаю конструктор:
    def __init__(self, n, *args): 
        self.space = n
        if self.space == 2:
            self.point1 = Point(n, args[0][0], args[0][1]).point_coordinate()
            self.point2 = Point(n, args[1][0], args[1][1]).point_coordinate()
        elif self.space == 3:
            self.point1 = Point(n, args[0][0], args[0][1], args[0][2]).point_coordinate()
            self.point2 = Point(n, args[1][0], args[1][1], args[1][2]).point_coordinate()
 
    # Пока не придумала как через наследование сделать,  так вычисляю длину:
    def line_length(self):
        if self.space == 2:
            distance = ((self.point1[0]- self.point2[0])**2 + (self.point1[1]- self.point2[1])**2)**0.5
        if self.space == 3:
            distance = ((self.point1[0]- self.point2[0])**2 + (self.point1[1]- self.point2[1])**2 + (self.point1[2]- self.point2[2])**2)**0.5
        return distance

    # Перенос линии к центру координат:
    def transfer_line(self):
        if self.space == 2:
            self.point2 = (self.point2[0] - self.point1[0], self.point2[1] - self.point1[1])
            self.point1 = (0, 0)
            return self.point1, self.point2
        elif self.space == 3:
            self.point2 = (self.point2[0] - self.point1[0], self.point2[1] - self.point1[1], self.point2[2] - self.point1[2])
            self.point1 = (0, 0, 0)
            return self.point1, self.point2

# Чтобы просто вывести линию, для проверок делала:
    def create_line(self):
        print(self.point1, self.point2)
        return self.point1, self.point2


# Подразумаевается, что к класс Point передается размерность, координата1, коортината2 , координата3 (толкьо если 3хмерное)
#  И в класс Line передается размерность, коорлинаты точки 1 в кортеже, координаты точки 2 в кортеже

# Для тестов:
# point = Point(2, 3, 4)
# dist = point.distance_to_center()
# print(dist)
# N = point.dimension()
# print(N)

# point1 = Point(3, 5, 4, 5)
# dist1 = point1.distance_to_center()
# print(dist1)
# N = point1.dimension()
# print(N)

line = Line(2, (2, 2), (3, 3))
print(line.create_line())
print(line.line_length())

line1 = Line(3, (2, 3, 5), (10, 11, 12))
print(line1.create_line())
print(line1.line_length())

print(line1.transfer_line())

