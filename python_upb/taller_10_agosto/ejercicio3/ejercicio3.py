# Capture 3 valores enteros y diferentes entre si
# y muestre el mayor de ellos

def mayordelostres(A, B, C):
    if A > B and A > C:
        return A
    elif B > A and B > C:
        return B
    elif C > A and C > B:
        return C
    else:
        return "Los tres valores son iguales"


