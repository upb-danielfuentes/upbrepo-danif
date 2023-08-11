# Capture 3 valores enteros y diferentes entre si
# y muestre el mayor de ellos


A = int(input("valor A: "))
B = int(input("valor B: "))
C = int(input("valor C: "))

if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
elif C > A and C > B:
    print(C)
else:
    print("los iguales")
