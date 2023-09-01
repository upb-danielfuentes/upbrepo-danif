Feature: Coche Functionality

  Scenario: Acelerar el coche dentro de la velocidad máxima
    Given que tengo un coche con una velocidad máxima de 200 km/h
    When acelero el coche en 50 km/h
    Then la velocidad actual del coche debería ser 50 km/h
