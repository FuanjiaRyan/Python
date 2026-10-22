from array import *

arr1 = array("i",[33,4,55,5,66])
arr2 = array(arr1.typecode, (n for n in arr1))

arr1[2] = 54

print(arr1)
print(arr2)