import numpy as np
import time

from numba import njit

@njit(cache=True)
def get_arr(num):
    arr_1 = np.empty(num)
    arr_2 = np.empty(num)
    for i in range(0, num):
        arr_1[i] = i
        arr_2[i] = i
    arr_3 = arr_1+arr_2
    return arr_3

num = 20000

t1 = time.time()
arr_1 = []
arr_2 = []
arr_3 = []
for i in range(0, num):
    arr_1.append(i)
    arr_2.append(i)
    arr_3.append(arr_1[i]+arr_2[i])
print(len(arr_3))
print(" Total time taken is :", time.time() - t1)

t1 = time.time()
arr_1 = np.empty(num)
arr_2 = np.empty(num)
for i in range(0, num):
    arr_1[i] = i
    arr_2[i] = i
arr_3 = arr_1+arr_2
print(len(arr_3))
print(" Total time taken is :", time.time() - t1)

t1 = time.time()
arr_1 = get_arr(num)
print(len(arr_1))
print(" Total time taken is :", time.time() - t1)

t1 = time.time()
arr_1 = get_arr(num)
print(len(arr_1))
print(" Total time taken is :", time.time() - t1)

