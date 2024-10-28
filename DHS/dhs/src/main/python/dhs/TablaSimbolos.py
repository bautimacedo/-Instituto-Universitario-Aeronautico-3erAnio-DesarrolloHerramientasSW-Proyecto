from Contexto import Contexto
from ID import ID

class TablaSimbolos(object) :
    
    __instance = None
    contextos = []

    def __new__(cls):
        if TablaSimbolos.__instance is None:
            TablaSimbolos.__instance = object.__new__(cls)
        return TablaSimbolos.__instance
    
    def __init__(self) :
        contextoGlobal = Contexto()
        self.contextos.append(contextoGlobal)

    def addContexto(self, contexto) :
        self.contextos.append(contexto)
        print("largo de la lista de contextos: "+ str(len(self.contextos)))

    def delContexto(self) :
        if self.contextos: #Verifica si hay o no contextos antes de eliminar
            self.contextos.pop()
        else:
            print("No hay contextos para eliminar.")

    def addIdentificador(self, nombre, tipoDato) :
        contexto = self.contextos[-1]
        id = ID(nombre, tipoDato, 1, 1)
        contexto.tabla.update({nombre:id})
        print("--- Se agrego un Identificador! ---")

    def buscarLocal(self, nombre) : # 
        if (self.contextos[-1].traerVariable(nombre)) != None:
            #print('"' + nombre + '" se esta usando a nivel LOCAL\n') 
            return 1
        return 0

    def buscarGlobal(self, nombre) : # =1 ya existe a nivel global - =0 no 
        if(self.contextos[0].traerVariable(nombre)) != None:
            #print('"' + nombre + " se esta usando a nivel GLOBAL\n")
            return 1
        return 0