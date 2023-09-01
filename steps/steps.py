from behave import given, when, then
from carro import Coche

@given('que tengo un coche con una velocidad máxima de {velocidad_maxima:d} km/h')
def step_given_tengo_coche(context, velocidad_maxima):
    context.coche = Coche("Toyota", "Camry", 2020, velocidad_maxima)

@when('acelero el coche en {velocidad:d} km/h')
def step_when_acelero_coche(context, velocidad):
    context.coche.acelerar(velocidad)

@then('la velocidad actual del coche debería ser {velocidad_actual:d} km/h')
def step_then_verificar_velocidad(context, velocidad_actual):
    assert context.coche.velocidad_actual == velocidad_actual, f"La velocidad actual es {context.coche.velocidad_actual} km/h"
