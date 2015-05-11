import math


class ShapeException(Exception):
    pass


def shape(a_list):
    if type(a_list[0]) == list:
        is_shape = len(a_list), len(a_list[0])
    else:
        is_shape = len(a_list),
    return is_shape

###############################################################################


def vector_add(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeException

    new_vector = [vector1[index] + vector2[index]
                  for index in range(len(vector1))]

    return new_vector

###############################################################################


def vector_sub(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeException

    new_vector = [vector1[index] - vector2[index]
                  for index in range(len(vector1))]

    return new_vector

###############################################################################


def vector_sum(*args):
    vector_list = list(args)
    shape_check = [vector
                   for vector in vector_list
                   if len(vector) == len(vector_list[0])]

    if vector_list != shape_check:
        raise ShapeException

    new_vector = [sum([vector[i]
                  for vector in vector_list])
                  for i in range(len(vector_list[0]))]

    return new_vector

###############################################################################


def dot(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeException

    new_scalar = sum([vector1[index] * vector2[index]
                      for index in range(len(vector1))])

    return new_scalar

###############################################################################


def vector_multiply(vector, factor):
    new_vector = [coefficient * factor for coefficient in vector]

    return new_vector

###############################################################################


def find_mean(a_list):

    mean = sum(a_list)/len(a_list)

    return mean

###############################################################################


def vector_mean(*args):
    vector_list = list(args)
    shape_check = [vector
                   for vector in vector_list
                   if len(vector) == len(vector_list[0])]

    if vector_list != shape_check:
        raise ShapeException

    new_vector = [find_mean([vector[i]
                  for vector in vector_list])
                  for i in range(len(vector_list[0]))]

    return new_vector

###############################################################################


def magnitude(vector):
    new_scalar = math.sqrt(sum([coefficient**2 for coefficient in vector]))

    return new_scalar

###############################################################################


def matrix_row(matrix, row):
    return matrix[row]

###############################################################################


def transform_matrix(matrix):
    columns = [[row[i]
               for row in matrix]
               for i in range(len(matrix[0]))]

    return columns

###############################################################################


def matrix_col(matrix, column):
    get_column = transform_matrix(matrix)

    return get_column[column]

###############################################################################


def matrix_scalar_multiply(matrix, factor):
    new_matrix = [[value * factor
                  for value in row]
                  for row in matrix]

    return new_matrix

###############################################################################


def matrix_vector_multiply(matrix, vector):
    if shape(matrix[0]) != shape(vector):
        raise ShapeException

    new_vector = [dot(row, vector) for row in matrix]

    return new_vector

###############################################################################


def matrix_matrix_multiply(matrix1, matrix2):
    if shape(matrix1)[1] != shape(matrix2)[0]:
        raise ShapeException

    transformed_matrix2 = transform_matrix(matrix2)

    new_matrix = [matrix_vector_multiply(transformed_matrix2, row)
                  for row in matrix1]

    return new_matrix
