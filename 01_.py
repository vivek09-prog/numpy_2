import numpy as np
# slicing
arr = np.arange(10)
print('basis slicing ', arr[2:8])
print(arr)
# with step
arr = np.arange(10)
print('basis slicing with step ', arr[2:8:3])

# slicing for 2_d array

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print('specific element ', arr_2d[2, 1])
print('entire row', arr_2d[1])
print('entire columb ', arr_2d[:,1])

#Sorting
unsorted_array = np.array([1,4,6,5,9,2,4,5,3,1,2,5,5,7,8,9,])
print('sorted array ', np.sort(unsorted_array) )

#Sorting in 2D arrays
unsorted_2D_array = np.array([[1,2,3],[3,2,5],[6,8,1]])
print('sorted 2D_array by column', np.sort(unsorted_2D_array , axis=0))
# TOP TO BOTTOM
print('sorted 2D_array by row', np.sort(unsorted_2D_array , axis=1))
# LEFT TO RIGHT