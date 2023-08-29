# descuentos.py

def ejercicio4(monto):
    if monto >= 100000:
        descuento = monto * 0.10
    elif monto >= 200000:
        descuento = monto * 0.20
    else:
        descuento = monto * 0.00
    return descuento
