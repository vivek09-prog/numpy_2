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
# TOP TO BOTTOM
print('sorted 2D_array by column', np.sort(unsorted_2D_array , axis=0))
# LEFT TO RIGHT
print('sorted 2D_array by row', np.sort(unsorted_2D_array , axis=1))


# FILTER
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_numbers = numbers[numbers % 2 == 0]
print('even number ', even_numbers)

# filter with mask 
mask = numbers > 5 

print('numbers greater then 5 ', numbers[mask])

# fancy indexing vs np.where()
indicies = [1,4,7]
print(numbers[indicies])

where_result = np.where(numbers > 5)
print('Np where ', numbers[where_result])

conditional_array = np.where(numbers > 5, numbers*5,numbers)
print(conditional_array)

conditional_array = np.where(numbers >=5, 'true','false')
print(conditional_array)