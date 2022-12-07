# 3.2 Escribir un diagrama para un programa que encuentre e imprima la sumatoria de los numeros pares comprendidos entre el 2 y el 20

# ESTO ES PYTHON

cont = 0 
acc = 0

for i in range(0,20):
    cont+=1
    if cont%2==0:
        acc+=cont
        
        
print(acc)