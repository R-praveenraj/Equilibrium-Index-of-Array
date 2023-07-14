#You are given an array A of integers of size N.
#Your task is to find the equilibrium index of the given array
#The equilibrium index of an array is an index such that 
#the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
#If there are no elements that are at lower indexes or at higher indexes, 
#then the corresponding sum of elements is considered as 0.

#PS:
#If there is no equilibrium index then return -1.
#If there are more than one equilibrium indexes then return the minimum index.
#A = [-7, 1, 5, 2, -4, 3, 0]      Output  =3

def equilibrium(array):
    length=len(array)
    prefix=[0]*length
    prefix[0]=array[0]
    for i in range(1,length):
        prefix[i]=prefix[i-1]+array[i]
    for i in range(1,length):
        if prefix[i-1]==prefix[length-1]-prefix[i]:
            return i
    return -1


array=[-7, 1, 5, 2, -4, 3, 0]
print(equilibrium(array))