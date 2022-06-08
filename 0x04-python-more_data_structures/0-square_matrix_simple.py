#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    inner = []
    for row in matrix:
        inner = []
        for i in row:
            i = i * i
            inner.append(i)
        new_matrix.append(inner)
    return new_matrix


