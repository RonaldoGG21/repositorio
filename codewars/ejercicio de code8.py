""" Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0. """

def sum_array(a):
    s = len(a)
    if s > 0:
        acc = 0
        
        for i in range(0,s):
            acc+=a[i]

        return acc
    return 0


print(sum_array([1, 2, 3]))