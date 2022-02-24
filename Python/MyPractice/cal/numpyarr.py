import numpy as np


"""1. create an array with 0
default type is np.float_
size : 2 * 5
"""
# a = np.zeros((2,3),np.int_)
# array([[ 0, 0, 0], [ 0, 0, 0]])

"""2. craete an array with 1
default type is np.float_
size: 5,
"""
# b = np.ones(5,dtype=np.int_)
# array([1,1,1,1,1])

"""3. create an array from zero
to stop-1
"""
# c = np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

'''4. create an array from start
to stop-step
'''
# d = np.arange(2,3,0.1)
# array([ 2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])

'''5. create an array from start
to stop, the numbers of array is
the third number, every step in the
array is the same'''
# e = np.linspace(1., 4., 6)
# array([ 1. ,  1.6,  2.2,  2.8,  3.4,  4. ])

'''
    create an array of...
    just look the result
'''
# np.indices((3,3))
# array([[[0, 0, 0], [1, 1, 1], [2, 2, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]])


'''
    index
    search one item from an numpy array is
    the same with the default array of python 
'''
# f = np.arange(10)
# x[2] -> 2
# x[-2] -> 8

'''
    index2
    search one item from an 
'''