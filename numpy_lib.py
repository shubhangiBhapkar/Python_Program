import numpy as np

#zero dimentional array
arr0=np.array(2)
print(arr0)

#one dimentional array
arr1=np.array([10,20,30,40,50])
print(arr1)

#two dimentional
arr2=np.array([[1,2,3],[50,60,70],[80,90,100]])
print(arr2)

#three 
arr3=np.array([ [[1,2,3],[50,60,70],[80,90,100]],
                [[1,2,3],[50,60,70],[80,90,100]],
                [[1,2,3],[50,60,70],[80,90,100]]
                ])
print(arr3)

print(arr0.shape)
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

print(arr0.size)
print(arr1.size)
print(arr2.size)
print(arr3.size)

