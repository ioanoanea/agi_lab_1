from objects.draw import draw
from objects.reflexion import *
from objects.line import Line
import numpy as np

from objects.polygon import Polygon
from objects.vector_2d import Vector2D


def print_matrix(matrix):
    '''
    Afiseaza o matrice (lista) pe randuri
    :param matrix:
    :return:
    '''
    for l in matrix:
        print(l)


print("Adaugati dreapta")
print("1. Dreapta data prin ecuatia dreptei")
print("2. Dreapta data prin punct si vector director")
option = input("Alegeti o optiune: ")

line = Line()
# Daca dreapta este data prin ecuatia dreptei
if option == "1":
    # Citim coeficientii ecuatiei
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
    line = Line(a, b, c)
# Altfel, daca dreapta este data prin punct si vector director
elif option == "2":
    # Citim coordonatele punctullui si versorii vectorului director
    x = float(input("x punct: "))
    y = float(input("y punct: "))
    i = float(input("i vector: "))
    j = float(input("j vector: "))
    line.create(x, y, Vector2D(i, j))
else:
    print("Optiune invalida")

nr_points = int(input("Nr. varfuri poligon: "))


polygon = Polygon()
# Citeste fiecare varf al poligonului
for i in range(nr_points):
    # Citeste coordonatele poligonului
    x = float(input("x varf: "))
    y = float(input("y varf: "))
    # adauga varful in lista de varfuri a poligonului
    point = Vector2D(x, y)
    polygon.add_point(point)


reflexion = Reflexion(line)
# Daca dreapta e paralela cu Ox
if line.a == 0:
    print("Dreapta este paralela cu axa Ox")
    # Afisam matricea translatiei
    print("Matricea translatiei este:")
    print_matrix(reflexion.ox_translation_matrix())
    # Afisam matricea reflexiei fata de Ox
    print("Matricea reflexiei este:")
    print_matrix(reflexion.ox_reflection_matrix)
    # Afisam matricea translatiei invere
    print("Matricea translatiei inverse este:")
    print_matrix(reflexion.inverse_translation_matrix(reflexion.ox_translation_matrix()))
# Daca dreapta e paralela cu Ox
elif line.b == 0:
    print("Dreapta este paralela cu axa Oy")
    # Afisam matricea translatiei
    print("Matricea translatiei este:")
    print_matrix(reflexion.oy_translation_matrix())
    # Afisam matricea reflexiei fata de Ox
    print("Matricea reflexiei este:")
    print_matrix(reflexion.oy_reflection_matrix)
    # Afisam matricea translatiei invere
    print("Matricea translatiei inverse este:")
    print_matrix(reflexion.inverse_translation_matrix(reflexion.oy_translation_matrix()))
    # Afisam matricea transformarii
# Daca dreapta trece prin origine
elif line.c == 0:
    print("Dreapta trece prin origine")
    # Afisam matricea rotatiei
    print("Matricea rotatiei este:")
    print_matrix(reflexion.rotation_matrix())
    # Afisam matricea reflexiei fata de axa Ox
    print("Matricea reflexiei este:")
    print_matrix(reflexion.ox_reflection_matrix)
    # Afisam matricea rotatiei inverse
    print("Matricea rotatiei inverse este:")
    print_matrix(reflexion.inverse_rotation_matrix(reflexion.rotation_matrix()))
else:
    # Afisam matricea translatiei
    print("Matricea translatiei este:")
    print_matrix(reflexion.ox_translation_matrix())
    # Afisam matricea rotatiei
    print("Matricea rotatiei este:")
    print_matrix(reflexion.rotation_matrix())
    # Afisam matricea reflexiei fata de axa Ox
    print("Matricea reflexiei este:")
    print_matrix(reflexion.ox_reflection_matrix)
    # Afisam matricea rotatiei inverse
    print("Matricea rotatiei inverse este:")
    print_matrix(reflexion.inverse_rotation_matrix(reflexion.rotation_matrix()))
    # Afisam matricea translatiei invere
    print("Matricea translatiei inverse este:")
    print_matrix(reflexion.inverse_translation_matrix(reflexion.ox_translation_matrix()))

# Afisam matricea transformarii
print("Transformarea cautata este:")
print_matrix(reflexion.final_transformation())
