from objects.vector_2d import Vector2D


class Line:
    '''
    Reprezinta o dreapta in spatiul 2D printr-o ecuatie de forma: ax+by+c=0
    a - coeficientul lui x
    b - coeficientul lui y
    c - constanta
    '''

    def __init__(self, a: float = 0, b: float = 1, c: float = 0):
        self.__a = a
        self.__b = b
        self.__c = c

    def __str__(self):
        return f"{self.__a}x+{self.__b}y+{self.__c}=0"

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def create(self, x: float, y: float, vector: Vector2D):
        '''
        Initializeaza drepata data prin punct si vector director
        :param x:
        :param y:
        :param vector:
        :return:
        '''
        self.__a = vector.y
        self.__b = -vector.x
        self.__c = vector.x * y - vector.y * x
