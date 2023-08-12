# escribir las estructuras que calculen 
# muestre en valor de x de acuerdo con lo siguiente:
# x=0 Si Y < A & (A<B<C)
# x=1 Si A <= Y < B
# x=2 Si B <= Y < C
# x=3 Si C <= Y
# x=4 No cumple con nada

def queesx():
    A = int(input("valor A: "))
    B = int(input("valor B: "))
    C = int(input("valor C: "))
    Y = int(input("valor Y: "))
    
    if Y < A and A < B < C:
        X = 0
    elif A <= Y < B:
        X = 1
    elif B <= Y < C:
        X = 2
    elif C <= Y:
        X = 3
    else:
        X = 4
        
    print(X)

queesx()
