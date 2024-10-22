import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker
def main(argv):
    archivo = "input/opal.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo) 
    #lexer es el que usa al filestream, construyo un objeto y le va pidiendo que le entregue caracteres, en algun momento genera token
    lexer = compiladoresLexer(input) 
   
    #token stream representa secuencia de tokens
    stream = CommonTokenStream(lexer)

    #parser hace analisis sintactico y consume el token stream, pide tokens y arma las reglas gramaticales  
    parser = compiladoresParser(stream)
    escucha=Escucha()
    parser.addParseListener(escucha)
    #le pedimos al objeto que arrance el analizis sintactico, programa es raiz del arbol, desde donde quiero empezar
    tree = parser.programa()

    print(tree.toStringTree(recog=parser))

    #caminante = Walker()
    #caminante.visitPrograma(tree)


if __name__ == '__main__':
    main(sys.argv)