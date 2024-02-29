# in this class we will learn about numpy and its functions 
# 1 waht is numpy
# 2 why we use numpy in our project 
# 3 where we use numpy in our project 
# 4 difference between numpy and list and array 
# 5 what is the difference between numpy and pandas
# 6 which is better numpy or pandas 
# The above question is very important for the interview
# 7 total function in numpy 
# 8 what can we do with numpy 
# 9 what is the difference between numpy and tensorflow
# 10 what is the difference between numpy and pytorch
# 11 what is the difference between numpy and keras  
# 12 what is the difference between numpy and scikit-learn
# 13 what is the difference between numpy and open-cv
# 14 what is the difference between numpy and matplotlib
# 15 what is the difference between numpy and seaborn
# 16 what is the the difference between numpy and plotly
# 17 what is the difference between numpy and bokeh
# 18 what is the difference between numpy and dash
# ---------------------------------------------------------
# 1 what is numpy
# numpy is a library in python which is used for mathematical operations
# and it is very fast and efficient and it is very easy to use 
# 2 why we use numpy in our project
# we use numpy in our project because it is very fast and efficient
# and it is very easy to use and it is very easy to learn 
# 3 where we use numpy in our project
# we use numpy in our project in the following places 
# 1 in data preprocessing
# 2 in data cleaning
# 3 in data transformation
# 4 in data visualization
# 5 in data scaling
# 6 in data normalization
# 7 in data standardization
# 8 in data encoding
# 9 in data imputation
# 10 in data splitting
# 11 in data merging
# 12 in data joining
# 13 in data concatenation
# 14 in data reshaping
# 15 in data filtering
# 16 in data sorting
# 17 in data searching
# 18 in data indexing
# 19 in data slicing
# 20 in data subsetting
# 21 in data sampling
# 22 in data shuffling


# 4 difference between numpy and list and array
# list is a collection of elements and array is a collection of elements
# but the difference between list and array is that list can store different types of data  
# and array can store only one type of data 
#example
# list=[1,22,"hello",3.4] # list can store different types of data like int, float, string  
# array=[1,22,33,44] # array can store only one type of data 
# and list is slow and array is fast or efficient
# and list is not easy to use and array is easy to use 

# 5 what is the difference between numpy and pandas
# numpy is a library in python which is used for mathematical operations and it is very fast and efficient 
# and pandas is a library in python which is used for data manipulation and it is very fast and efficient 

# 6 which is better numpy or pandas 
# both are better in their own place
# numpy is better for mathematical operations and pandas is better for data manipulation 

# 7 total function in numpy
# total function in numpy is 615 
# total attributes in numpy is 10  (numpy.__all__ , numpy.__builtins__ , numpy.__cached__ , numpy.__config__ ,
#  numpy.__doc__ , numpy.__file__ , numpy.__git_revision__ , numpy.__loader__ , numpy.__name__ , numpy.__package__)
# total constants in numpy is 1 that is pi
# total classes in numpy is 1 that is numpy.ndarray


# 8 what can we do with numpy
# we can do the following things with numpy
# 1 we can do mathematical operations
# 2 we can do logical operations
# 3 we can do comparison oper


# 9 what is the difference between numpy and tensorflow
# numpy is a library in python which is used for mathematical operations and it is very fast and efficient
# and tensorflow is a library in python which is used for deep learning and it is very fast and efficient

# 10 what is the difference between numpy and pytorch 
# numpy is a library in python which is used for mathematical operations and it is very fast and efficient
# and pytorch is a library in python which is used for deep learning and it is very fast and efficient


# 11 what is the difference between numpy and keras
# numpy is a library in python which is used for mathematical operations and it is very fast and efficient
# and keras is a library in python which is used for deep learning and it is very fast and efficient


# 12 what is the difference between numpy and scikit-learn
# numpy is a library in python which is used for mathematical operations and it is very fast and efficient
# and scikit-learn is a library in python which is used for machine learning and it is very fast and efficient

# total function in numpy is 615  with examples
# 1 numpy.abs  # this function is used to find the absolute value of the array 
#  example
# a=np.array([-1,2,-3,4,-5])
# print(np.abs(a))  # [1 2 3 4 5]  # this is the absolute value of the array
# 2 numpy.absolute  # this function is used to find the absolute value of the array
# example
# a=np.array([-1,2,-3,4,-5])
# print(np.absolute(a))  # [1 2 3 4 5]  # this is the absolute value of the array
# 3 numpy.add  # this function is used to add two arrays
# example
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# print(np.add(a,b))  # [ 7  9 11 13 15]  # this is the sum of the two arrays


# ---------------------------------------------------------  lecture 2  ---------------------------------------------------------
#.........................................................................................................................................
# ......................................................... learining numpy ...............................................................
import numpy as np
#.........................................................................................................................................
# -----------------------1 how to install numpy
# numpy is a library in python which is used for mathematical operations and it is very fast and efficient
# install numpy using the following command
# pip install numpy  # pip is a package manager in python which is used to install the packages in python
# conda install numpy  # conda is a package manager in anaconda which is used to install the packages in anaconda
# pip install numpy --upgrade  # this command is used to upgrade the numpy package
# pip uninstall numpy  # this command is used to uninstall the numpy package
# pip show numpy  # this command is used to show the information of numpy package
# pip list  # this command is used to show the list of all the packages installed in the python
# pip freeze  # this command is used to show the list of all the packages installed in the python with the version number


# -----------------------2 how to import numpy
# import numpy as np  # np is an alias name of numpy  and it is used to call the functions of numpy and we can use any name instead of np 
# 3 how to create array in numpy

# syntax of creating array in numpy
# np.array([1,2,3,4,5])  # this is a 1-d array 
# what is defualt value of the array in numpy ?
# the default value of the array in numpy is float  like example



# ---------------------data types in numpy array--------------------------------
print("-----------------------data types in numpy array------------------------")
# what is total  data type of the array in numpy ? 
# total data type of the array in numpy is 24 

# 1 bool_  # this is the boolean data type 
# bool is used to store the boolean values like True and False  and it is 1 byte 
# example 
a=np.array([True,False,True,False])
print(a)  # [ True False  True False]  # this is the boolean array
print(a.dtype)  # bool  # this is the data type of the array
print(a.itemsize)  # 1  # this is the size of the each element in the array (1 byte)

#-------------------------------------

# 2 int8  # this is the integer data type
# int8 is used to store the integer values and it is 1 byte 
# example
a=np.array([1,2,3,4,5],dtype="int8") 
# this is the integer array and the data type of the array is int8 
# int8 is used to store the integer values and it is 1 byte 
# int8 means the size of the each element in the array is 1 byte
# int8 stores the integer values from -128 to 127
# if we do not provide the data type of the array then the default data type of the array is int32
# if we provide the data type of the array then the data type of the array is the provided data type

# it means the size of the each element in the array is 1 byte 
print(a)  # [1 2 3 4 5]  # this is the integer array
print(a.dtype)  # int8  # this is the data type of the array
print(a.itemsize)  # 1  # this is the size of the each element in the array (1 byte) 

# 3 int16  # this is the integer data type
# 4 int32  # this is the integer data type
# 5 int64  # this is the integer data type
# 6 uint8  # this is the unsigned integer data type
# 7 uint16  # this is the unsigned integer data type
# 8 uint32  # this is the unsigned integer data type
# 9 uint64  # this is the unsigned integer data type
# 10 float16  # this is the float data type
# 11 float32  # this is the float data type
# 12 float64  # this is the float data type
# 13 complex64  # this is the complex data type
# 14 complex128  # this is the complex data type
# 15 object_  # this is the object data type
# 16 bytes_  # this is the bytes data type
# 17 string_  # this is the string data type
# 18 unicode_  # this is the unicode data type
# 19 int0  # this is the integer data type
# 20 uint0  # this is the unsigned integer data type
# 21 float0  # this is the float data type
# 22 complex0  # this is the complex data type
# 23 datetime64  # this is the datetime data type
# 24 timedelta64  # this is the timedelta data type

#------------------
import numpy as np
a=np.array(1)
print(a)  # [1]  # this is a 0-d array
print(a.ndim)  # 0


#------------------
b=np.array([1,2,3,4,5]) # this is a 1-d array
print(b)  # [1 2 3 4 5] # this is a 1-d array
print(b.ndim)  # 1  # this is the dimension of the array
print(b.dtype)  # int32  # this is the data type of the array
print(b.shape)  # (5,)  # this is the shape of the array shape is the number of elements in the array
print(b.size)  # 5  # this is the size of the array size is the number of elements in the array
print(b.itemsize)  # 4  # this is the size of the each element in the array (4 bytes) like int32 is 4 bytes  and float64 is 8 bytes 
print(b.nbytes)  # 20  # this is the total size of the array in bytes 
print(b.strides)  # (4,) # this is the total size of the array in bytes (4*5=20)
print(b.flags)  # C_CONTIGUOUS : True  # this is the memory layout of the array  C_CONTIGUOUS means row major order  and F_CONTIGUOUS means column major order
print(b.base)  # None  # this is the base of the array
print(b.T)  # [1 2 3 4 5]  # this is the transpose of the array
print(b.real)  # [1 2 3 4 5]  # this is the real part of the array
print(b.imag)  # [0 0 0 0 0]  # this is the imaginary part of the array
print(b.flat)  # <numpy.flatiter object at 0x0000021F6C3D5E40>  # this is the flat of the array
print(b.ctypes)  # <numpy.core._internal._ctypes object at 0x0000021F6C3D5D80>  # this is the ctypes of the array 
print(b.data)  # <memory at 0x0000021F6C3E3A00>  # this is the data of the array 
#------------------
b=np.array([1,2,3,4,"babar",True])
print(b)  # ['1' '2' '3' '4' 'babar' 'True']  # this is a 1-d array
print(b.itemsize) # 44  # this is the size of the each element in the array (44 bytes) like int32 is 4 bytes  and float64 is 8 bytes
# how its itemsize is 44 bytes because the default data type of the array is string and the size of the string is 44 bytes
# lets see the size of the string
print(b[4])  # babar  # this is the string
print(b[4].itemsize)  # 44  # this is the size of the string

#------------------
c=np.array([[1,2,3,4,5],[6,7,8,9,10]]) # this is a 2-d array 
print(c)  # [[ 1  2  3  4  5]


#------------------
b=np.array([1,2])
print(b)  # [1 2]  # this is a 1-d array
print(b.itemsize) # 4  # this is the size of the each element in the array (4 bytes) like int32 is 4 bytes  and float64 is 8 bytes
# how its itemsize is 4 bytes because the default data type of the array is int and the size of the int is 4 bytes
# lets see the size of the int
print(b[0])  # 1  # this is the int
print(b[0].itemsize)  # 4  # this is the size of the int
print(b[1])  # 2  # this is the int
print(b[1].itemsize)  # 4  # this is the size of the int
# so total size of the array is 8 bytes (4*2=8)
#------------------
print("-----------------------itemsize------------------------")
b=np.array([1,2,3,4,"babar",True])
for i in b:
    print(i.itemsize)  # 44  # this is the size of the each element in the array (44 bytes) 
    # like int32 is 4 bytes  and float64 is 8 bytes
# output is 4 4 4 4 20 16 # but 


