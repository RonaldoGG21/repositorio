""" Simple, remove the spaces from the string, then return the resultant string. """

def no_space(x):
    x = x.split(" ")
    x = "".join(x)
    
    return x

print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))