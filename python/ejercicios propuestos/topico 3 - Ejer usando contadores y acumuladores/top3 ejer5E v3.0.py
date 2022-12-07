# e) Escribir un diagrama para un programa que imprima serie fibonaci cuyo ultimo numero de la serie sea 34

# ESTO ES PYTHON

a=1
b=0
c=0

for i in range(0,14):
    print(b)
    if b==34:
        break
    b=c+a
    a=c
    c=b
