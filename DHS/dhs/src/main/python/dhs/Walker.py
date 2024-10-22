from compiladoresParser import compiladoresParser
from compiladoresVisitor import compiladoresVisitor

class Walker (compiladoresVisitor) : 
    def visitPrograma(self, ctx):
        print("Esta empezando a caminar...")
        temp =  super().visitPrograma(ctx)
        print("fin del recorrido")
        return temp
    
    def visitDeclaracion(self, ctx):
        #return super().visitDeclaracion(ctx)
        print(ctx.getChild(0).getText() + 
              "-" + 
              ctx.getChild(1).getText())
    
    def visitBloque(self, ctx):
        print("Nuevo contexto")
        print(ctx.getText())
        return super().visitInstrucciones(ctx.getChild(1))
    
    def visitTerminal(self, node):
        print("===>> Token" + node.getText() + "--")
        return super().visitTerminal(node)
    
