class Vector2D:
    '''
    Reprezinta un vector in spatiul 2D
    '''

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        '''
        Verifica daca doi vectori sunt egali
        :param other:
        :return: boolean
        '''
        return self.__x == other.x and self.__y == other.y

    def __add__(self, other):
        '''
        aduna 2 vectori
        :param other:
        :return: Vrector2D
        '''
        return Vector2D(self.__x + other.x, self.__y + other.y)

    def __str__(self):
        '''
        Afiseaza un vector
        :return: string
        '''
        return f"[{self.__x},{self.__y}]"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def multiply(self, scalar: float):
        '''
        Inmulteste vectorul cu un scalar
        :param scalar:
        :return:
        '''
        self.__x *= scalar
        self.__y *= scalar
        return self
