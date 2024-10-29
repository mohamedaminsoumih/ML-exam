import numpy as np


def make_array_from_list(some_list):
    return np.array(some_list)



class NumpyBasics:
    def add_arrays(self, a, b):
        # Addition élément par élément de deux tableaux
        return np.add(a, b)

    def add_array_number(self, a, num):
        # Addition d'un tableau et d'un nombre
        return a + num

    def multiply_elementwise_arrays(self, a, b):
        # Multiplication élément par élément de deux tableaux
        return np.multiply(a, b)

    def dot_product_arrays(self, a, b):
        # Produit scalaire euclidien de deux tableaux
        return np.dot(a, b)

    def dot_1d_array_2d_array(self, a, m):
        # Produit scalaire d'un tableau 1D et d'une matrice (2D)
        return np.dot(a, m)

