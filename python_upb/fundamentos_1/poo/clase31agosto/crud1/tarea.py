class CrudTareas:
    def __init__(self):
        self.tareas = []
    def AgrTarea(self, tarea):
        self.tareas.append(tarea)
    def BusTarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
        return None
    def ModTarea(self, tarea):
        for i in range(len(self.tareas)):
            if self.tareas[i].id == tarea.id:
                self.tareas[i] = tarea
                return True
        return False
    def EliTarea(self, id):
        for i in range(len(self.tareas)):
            if self.tareas[i].id == id:
                del self.tareas[i]
                return True
        return False
    def LisTareas(self):
        return self.tareas
    