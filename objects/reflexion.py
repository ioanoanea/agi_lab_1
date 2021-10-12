import copy
from math import sqrt
import numpy as np

from objects.line import Line


class Reflexion:

    def __init__(self, line: Line):
        self.__line = line

    @property
    def ox_reflection_matrix(self):
        '''
        Returneaza matricea reflexiei fata de axa Ox
        :return:
        '''
        return [[1, 0, 0],
                [0, -1, 0],
                [0, 0, 1]]

    @property
    def oy_reflection_matrix(self):
        '''
        eturneaza matricea reflexiei fata de axa Oy
        :return:
        '''
        return [[-1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]

    def ox_translation_matrix(self):
        '''
        Returneaza matricea translatiei care duce dreapta in origine pentru drepte orizontale
        :param line:
        :return:
        '''
        return [[1, 0, 0],
                [0, 1, -self.__line.c / self.__line.b],
                [0, 0, 1]]

    def oy_translation_matrix(self):
        '''
        Returneaza matricea translatiei care duce dreapta in origine pentru drepte verticale
        :param line:
        :return:
        '''
        return [[1, 0, -self.__line.c / self.__line.a],
                [0, 1, 0],
                [0, 0, 1]]

    def inverse_translation_matrix(self, matrix):
        '''
        Retruneaza matricea translatiei inverse pentru o translatie efecetuata
        :param matrix:
        :return:
        '''
        i_matrix = copy.deepcopy(matrix)
        i_matrix[0][2] = -matrix[0][2]
        i_matrix[1][2] = -matrix[1][2]
        return i_matrix

    def rotation_matrix(self):
        '''
        Returneaza matricea rotatiei care face ca dreapta sa fie paralela cu axa Ox
        :param line:
        :return:
        '''
        sin_theta = self.__line.a / sqrt(self.__line.a ** 2 + self.__line.b ** 2)
        cos_theta = -self.__line.b / sqrt(self.__line.a ** 2 + self.__line.b ** 2)
        return [[cos_theta, -sin_theta, 0],
                [sin_theta, cos_theta, 0],
                [0, 0, 1]]

    def inverse_rotation_matrix(self, matrix):
        '''
        Retruneaza matricea rotatiei inverse pentru o rotatie efecetuata
        :param matrix:
        :return:
        '''
        i_matrix = copy.deepcopy(matrix)
        i_matrix[1][0] = -matrix[1][0]
        i_matrix[0][1] = -matrix[0][1]
        return i_matrix

    def final_transformation(self):
        '''
        Returneaza matricea transformarii cautate
        :return:
        '''
        # Daca dreapta e paralela cu Ox
        if self.__line.a == 0:
            # matricea translatiei
            ox_t_matrix = np.array(self.ox_translation_matrix())
            # matricea reflexiei fata de ox
            ox_r_matrix = np.array(self.ox_reflection_matrix)
            # matricea translatiei inversre
            i_ox_t_matrix = np.array(self.inverse_translation_matrix(ox_t_matrix))
            # mareicea transformarii
            return list(ox_t_matrix @ ox_r_matrix @ i_ox_t_matrix)
        # Daca dreapta e paralela cu Oy
        elif self.__line.b == 0:
            # matricea translatiei
            oy_t_matrix = np.array(self.oy_translation_matrix())
            # matricea reflexiei fata de oy
            oy_r_matrix = np.array(self.oy_reflection_matrix)
            # matricea translatiei inversa
            i_oy_t_matrix = np.array(self.inverse_translation_matrix(oy_t_matrix))
            # matricea transformarii
            return list(oy_t_matrix @ oy_r_matrix @ i_oy_t_matrix)
        # Daca dreapta trece prin origine
        elif self.__line.c == 0:
            # matricea rotatiei
            rot_matrix = np.array(self.rotation_matrix())
            # matricea reflexiei fata de ox
            ox_r_matrix = np.array(self.ox_reflection_matrix)
            # matricea rotatiei inverse
            i_rot_matrix = np.array(self.inverse_rotation_matrix(rot_matrix))
            return list(rot_matrix @ ox_r_matrix @ i_rot_matrix)
        # Daca dreapta nu e paralela cu nici o axa si nici nu trece prin origine
        else:
            # matricea translatiei
            ox_t_matrix = np.array(self.ox_translation_matrix())
            # matricea rotatiei
            rot_matrix = np.array(self.rotation_matrix())
            # matricea reflexiei fata de ox
            ox_r_matrix = np.array(self.ox_reflection_matrix)
            # matricea rotatiei inverse
            i_rot_matrix = np.array(self.inverse_rotation_matrix(rot_matrix))
            # matriecea translatiei inverse
            i_ox_t_matrix = np.array(self.inverse_translation_matrix(ox_t_matrix))
            return list(ox_t_matrix @ rot_matrix @ ox_r_matrix @ i_rot_matrix @ i_ox_t_matrix)
