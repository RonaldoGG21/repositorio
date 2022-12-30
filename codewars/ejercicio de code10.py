#Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
def sum_mix(arr):
    acc = 0
    for i in arr:
        i = int(i)
        acc+=i
    return acc
    #your code here