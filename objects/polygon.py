from objects.vector_2d import Vector2D


class Polygon:

    def __init__(self):
        self.__points = []

    @property
    def points(self):
        return self.__points

    def add_point(self, point: Vector2D):
        '''
        Adauga un punct in lista punctelor poligonului
        :param point:
        :return:
        '''
        self.__points.append(point)

    def get_matrix(self):
        '''
        Returneaza matricea poligonului
        :return:
        '''
        return [[point.x for point in self.__points],
                [point.y for point in self.__points],
                [1 for _ in self.__points]]
