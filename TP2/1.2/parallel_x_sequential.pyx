from cython.parallel import prange
import numpy as np
cimport numpy as np
from time import time
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def parallel_sum(double[:] arr) -> double:
    cdef Py_ssize_t i
    cdef double total = 0.0

    with nogil:
        for i in prange(arr.shape[0], schedule='static'):
            total += arr[i]
    return total

@cython.boundscheck(False)
@cython.wraound(False)
def sequential_sum(double[:] arr) -> double:
    cdef Py_ssize_t i
    cdef double total = 0.0

    for i in range(arr.shape[0]):
        total += arr[i]
    return total