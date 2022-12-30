""" Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == [] """

def invert(lst):
    s = len(lst)
    for i in range(0,s):
        lst[i] = lst[i]*-1
    return lst
    pass

print(invert([1,2,3,4,5]))