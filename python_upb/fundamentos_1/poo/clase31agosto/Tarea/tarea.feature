Feature: Gestión de Tareas

  Scenario: Agregar una tarea a la lista
    Given que el usuario inicia la aplicación
    When el usuario selecciona la opción "Agregar Tarea"
    And el usuario ingresa "Comprar leche" como la nueva tarea
    Then la tarea "Comprar leche" debe estar en la lista de tareas

  Scenario: Eliminar una tarea de la lista
    Given que el usuario inicia la aplicación
    And existe una tarea "Hacer la compra" en la lista de tareas
    When el usuario selecciona la opción "Eliminar Tarea"
    And el usuario ingresa el índice 1
    Then la tarea "Hacer la compra" no debe estar en la lista de tareas

  Scenario: Mostrar todas las tareas
    Given que el usuario inicia la aplicación
    And existen las tareas "Hacer la compra" y "Llamar al cliente" en la lista de tareas
    When el usuario selecciona la opción "Mostrar todas las Tareas"
    Then el usuario debe ver las tareas en el siguiente orden:
      """
      1. Hacer la compra
      2. Llamar al cliente
      """

  Scenario: Obtener una tarea específica de la lista
    Given que el usuario inicia la aplicación
    And existen las tareas "Hacer la compra" y "Llamar al cliente" en la lista de tareas
    When el usuario selecciona la opción "Obtener una Tarea de la lista"
    And el usuario ingresa el índice 2
    Then el usuario debe ver la tarea "Llamar al cliente"

  Scenario: Actualizar una tarea en la lista
    Given que el usuario inicia la aplicación
    And existen las tareas "Hacer la compra" y "Llamar al cliente" en la lista de tareas
    When el usuario selecciona la opción "Actualizar Tarea"
    And el usuario ingresa el índice 1
    And el usuario ingresa la nueva tarea "Comprar pan"
    Then la tarea "Hacer la compra" debe ser reemplazada por "Comprar pan" en la lista de tareas

  Scenario: Salir de la aplicación
    Given que el usuario inicia la aplicación
    When el usuario selecciona la opción "Salir de las Tareas"
    Then la aplicación debe cerrarse
