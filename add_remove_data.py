import numpy as np

arr1 = np.array([1,2,3])                    
arr2 = np.array([4,5,6])   

combined = arr1 + arr2
print(combined)

# using concatente
combined = np.concatenate((arr1,arr2))
print(combined)

# array compatiblity
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])

print('array compatibility ', a.shape == b.shape)

a = np.array([1,2,3])
b = np.array([4,5,9,6])
c = np.array([7,8,9])

print('array compatibility ', a.shape == b.shape)

row = np.array([[1,2],[4,5]])
new_row = np.array([5,9])
with_new_row = np.vstack((row ,new_row)) #vstack always add row(left to right)
print(with_new_row)

new_col = np.array([[7],[9],[8]])
with_new_col = np.hstack((with_new_row,new_col)) #hstack always add col(top to bottom)
print(with_new_col)

# deleting

arr = np.array([1,2,3,4,5])
deleted = np.delete(arr ,3)
print(deleted)