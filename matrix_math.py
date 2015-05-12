import math
import operator


class ShapeException(Exception):
    pass


def shape(a_list):
    """Takes a list and returns a tuple of form
    (length_of_list, length_of_each_element). The length of each element is
    only used if each element is also a list.
    """
    if type(a_list[0]) == list:
        is_shape = len(a_list), len(a_list[0])
    else:
        is_shape = len(a_list),
    return is_shape

###############################################################################


def list_operator(list1, list2, operation):
    """Takes two lists and an operation. Checks that the lists have the same
    "shape" as defined by the shape() function. Creates a list where each
    element is the result of performing the given operation with each
    pair of corresponding elements from the two given lists.
    """
    if shape(list1) != shape(list2):
        raise ShapeException()

    new_list = [operation(list1[index], list2[index])
                for index in range(len(list1))]

    return new_list
###############################################################################


def vector_add(vector1, vector2):
    """Adds the given vectors. Returns a vector"""
    new_vector = list_operator(vector1, vector2, operator.add)

    return new_vector

###############################################################################


def vector_sub(vector1, vector2):
    """Subtracts the given vectors. Returns a vector."""
    new_vector = list_operator(vector1, vector2, operator.sub)

    return new_vector

###############################################################################


def vector_sum(*args):
    """Takes the sum of any number of vectors.  Returns a vector."""
    vector_list = list(args)
    shape_check = [vector
                   for vector in vector_list
                   if len(vector) == len(vector_list[0])]

    if vector_list != shape_check:
        raise ShapeException()

    new_vector = [sum([vector[i]
                  for vector in vector_list])
                  for i in range(len(vector_list[0]))]

    return new_vector

###############################################################################


def dot(vector1, vector2):
    """Takes the dot product of two vectors. Returns a scalar."""
    new_scalar = sum(list_operator(vector1, vector2, operator.mul))

    return new_scalar

###############################################################################


def vector_multiply(vector, factor):
    """Multiplies two vectors. Returns a vector."""
    new_vector = [coefficient * factor for coefficient in vector]

    return new_vector

###############################################################################


def find_mean(a_list):
    """Finds the mean of the elements of a given list."""
    mean = sum(a_list)/len(a_list)

    return mean

###############################################################################


def vector_mean(*args):
    """Finds the mean of some number of vectors. Returns a vector."""
    vector_list = list(args)
    shape_check = [vector
                   for vector in vector_list
                   if len(vector) == len(vector_list[0])]

    if vector_list != shape_check:
        raise ShapeException()

    new_vector = [find_mean([vector[i]
                  for vector in vector_list])
                  for i in range(len(vector_list[0]))]

    return new_vector

###############################################################################


def magnitude(vector):
    """Finds the magnitude of a vector. Returns a scalar."""
    new_scalar = math.sqrt(sum([coefficient**2 for coefficient in vector]))

    return new_scalar

###############################################################################


def matrix_row(matrix, row):
    """Takes a matrix and row number and returns that row"""
    return matrix[row]

###############################################################################


def transform_matrix(matrix):
    """Transposes the rows and columns of a matrix"""
    columns = [[row[i]
               for row in matrix]
               for i in range(len(matrix[0]))]

    return columns

###############################################################################


def matrix_col(matrix, column):
    """Takes a matrix and a column number and returns the column"""
    get_column = transform_matrix(matrix)

    return get_column[column]

###############################################################################


def matrix_scalar_multiply(matrix, factor):
    """Multiplies a matrix by a scalar. Returns a matrix."""
    new_matrix = [[value * factor
                  for value in row]
                  for row in matrix]

    return new_matrix

###############################################################################


def matrix_vector_multiply(matrix, vector):
    """Multiplies a matrix and a vector (dot product). Returns a vector."""
    if shape(matrix[0]) != shape(vector):
        raise ShapeException()

    new_vector = [dot(row, vector) for row in matrix]

    return new_vector

###############################################################################


def matrix_matrix_multiply(matrix1, matrix2):
    """Multiplies two matrices. Returns a matrix of the same
    shape as matrix1
    """
    if shape(matrix1)[1] != shape(matrix2)[0]:
        raise ShapeException()

    transformed_matrix2 = transform_matrix(matrix2)

    new_matrix = [matrix_vector_multiply(transformed_matrix2, row)
                  for row in matrix1]

    return new_matrix
