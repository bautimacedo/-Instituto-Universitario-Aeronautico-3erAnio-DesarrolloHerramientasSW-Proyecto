class Contexto():

    def __init__(self) :
        self.tabla = {}
        #self.variables={}
        #self.funciones={}


    # def agregar_variable(self, nombre, tipo):
    #     if nombre in self.variables:
    #         print("El nombre " + nombre + " ya esta siendo utilizado")
    #     else:
    #         print("Se agrego la variable " + nombre + " de tipo " + tipo)
    #         self.variables[nombre] = tipo
    # def agregar_funcion(self, nombre, tipo):
    #     if nombre in self.funciones:
    #         print("El nombre " + nombre + " ya esta siendo utilizado")
    #     else:
    #         print("Se agrego la variable " + nombre + " de tipo " + tipo)
    #         self.funciones[nombre] = tipo


    def traerVariable(self, nombre):
        if nombre in self.tabla:
            return self.tabla[nombre]  # Devuelve la instancia de la variable
        else:
            return None
        
    def imprimirTabla(self):
        for clave, valor in self.tabla.items():
            print(f"{clave}: {valor}")