import matplotlib.pyplot as plt
import numpy as np
from objects.line import Line
from objects.polygon import Polygon


class Plotter:

    def __init__(self):
        self.__plot_axis()

    def __plot_axis(self):
        # plot Ox axis
        x = [-10, 10]
        y = [0, 0]
        plt.plot(x, y, label="Ox, Oy", color="black")
        # plot Oy axis
        x = [0, 0]
        y = [-10, 10]
        plt.plot(x, y, color="black")

    def add_line(self, line: Line, label):
        '''
        Adauga o dreapta
        :param line:
        :return:
        '''
        # Daca dreapta e orizontala
        if line.a == 0:
            x = [-10, 10]
            y = [-line.c / line.b, -line.c / line.b]
            plt.plot(x, y, label=label, color="blue")
        # Daca dreapta e verticala
        elif line.b == 0:
            x = [-line.c / line.a, -line.c / line.a]
            y = [-10, 10]
            plt.plot(x, y, label=label, color="blue")
        else:
            x = [-10, 10]
            y = [(-line.a * -10 - line.c) / line.b, (-line.a * 10 - line.c) / line.b]
            plt.plot(x, y, label=label, color="blue")

    def add_polygon(self, polygon_matrix, label, color):
        '''
        Adauga un polygon
        :param polygon_matrix:
        :return:
        '''
        points = []
        for i in range(len(polygon_matrix[0])):
            points.append([polygon_matrix[0][i], polygon_matrix[1][i]])
        polygon = plt.Polygon(points, label=label, fc=color, ec="blue")
        plt.gca().add_patch(polygon)

    def show(self):
        plt.legend()
        plt.show()
