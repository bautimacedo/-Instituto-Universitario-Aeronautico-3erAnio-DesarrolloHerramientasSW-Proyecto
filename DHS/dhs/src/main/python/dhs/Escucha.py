from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Contexto import Contexto
from ID import ID

class Escucha (compiladoresListener) :
    tablaDeSimbolos=TablaSimbolos()

    #contadores para el total del programa
    numTokensTotal = 0
    numNodosTotal = 0

    #contadores para cada bloque
    numTokens=0
    numNodos=0


    
    # se llam al entrar en el contexto del programa principal
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienza compilacion\n')


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print('***Se entra a un WHILE***\n')
        #print('\tCantidad de hijos: '+ str(ctx.getChildCount()))
        #print('\tTOKENS
        #: '+ ctx.getText())

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print('Fin de WHILE')
        print('Cantidad de hijos: '+ str(ctx.getChildCount()))
        print('TOKENS: '+ str(ctx.getText())+"\n")


    # Enter a parse tree produced by compiladoresParser#declaracion.
    #se llama cuando entra a la decaracion de una variable
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print(' ### Declaracion ###')

    # Exit a parse tree produced by compiladoresParser#declaracion.
    # se llama cuando sale de una declaracion de variable
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        tipoDeDato= ctx.getChild(0).getText() #obtiene el tipo de dato (int,float)
        nombreVariable= ctx.getChild(1).getText() #obtiene el nombre 

        if(self.tablaDeSimbolos.buscarGlobal(nombreVariable)!=1): 
        #comprueba si la variable ya esta deifnida a nivel global
        # antes de agregarla a la tabla de simbolos para asegurarse
        # que no s este redefiniendo una variable que ya existe
            self.tablaDeSimbolos.buscarLocal(nombreVariable) 
            #si no existe a nivel global, busca si la variable ya fue declarada
            #en el contexto local actual, si la encuentra no la agrega a la tabla
        self.tablaDeSimbolos.addIdentificador(nombreVariable,tipoDeDato)


#para saber si estoy en una hoja
    def visitTerminal(self, node: TerminalNode):
        self.numTokensTotal+=1 
        self.numTokens +=1 
    

    def visitErrorNode(self, node: ErrorNode):
        print('----> ERROR')  
    
    #se llama al entrar en cualquier regla de la gramatica
    def enterEveryRule(self, ctx):
        self.numNodosTotal +=1
        self.numNodos +=1

    #se llama al entrar en un bloue de codigo es decir contexto
    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        print('***Entre a un CONTEXTO***\n')
        contexto = Contexto() #crea un objeto contexto
        self.tablaDeSimbolos.addContexto(contexto) #agrega el objeto a la tabla de simbolos
        

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print('***Sali de un CONTEXTO***')
        print('Cantidad de hijos: '+ str(ctx.getChildCount())) #imprime cantidad de hijos
        print('TOKENS: '+ ctx.getText()) #imprime texto del bloque

        print("En este contexto se encontro lo siguiente:")
        self.tablaDeSimbolos.contextos[-1].imprimirTabla() #imprime la tabla de simbolos del contexto actual
        print("********************************************\n")
        self.tablaDeSimbolos.delContexto() #elimina el bloque

    
    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Fin compilacion\n')
        print('Se encontraron: ')
        print('Nodos: '+ str(self.numNodosTotal))
        #tokens son las hojas
        print('\tTokens: '+ str(self.numTokensTotal))
        #print("Cantidad de contextos encontrados en esta tabla de simbolos: "+self.tablaDeSimbolos.nombre)

    def enterFunction(self, ctx:compiladoresParser.FuncionContext):
        print(' ### Entrando a una funcion ###')
        contexto = Contexto()
        self.tablaDeSimbolos.addContexto(contexto)

    def exitFunction(self, ctx:compiladoresParser.FuncionContext):
        nombreFuncion = ctx.declaracionFunc().getChild(1).getText()
        Tiporetorno = ctx.declaracionFunc().getChild(0).getText()
        
        if self.tablaDeSimbolos.buscarGlobal(nombreFuncion)==1 or self.tablaDeSimbolos.buscarLocal(nombreFuncion)==1:
            print("Este nombre de funcion ya esta definida a nivel global")
            return None
        
        print("Parametros Encontrados")
        parametros = ctx.declaracionFunc().getChild(3)
        if parametros: #en caso de que hayan parametros
            numHijos = parametros.getChildCount()
            i=0

            while(i < numHijos):
                tipoParametro = parametros.getChild(i).getText() #accede al i porque el tipo va antes que el nombre
                nombreParametro = parametros.getChild(i+1).getText()
                self.tablaDeSimbolos.addIdentificador(tipoParametro,nombreParametro)
                if i+3 < numHijos: #si queda espacio para un proximo parametro
                    i+=3 #usamos +3 porque saltea tipo,nombre y coma
                else:
                    break 
         
        self.tablaDeSimbolos.addIdentificador(nombreFuncion, Tiporetorno)
        print("En esta funcion se encontro lo siguiente:")
        self.tablaDeSimbolos.contextos[-1].imprimirTabla() #imprime la tabla de simbolos del contexto actual
        self.tablaDeSimbolos.delContexto()




