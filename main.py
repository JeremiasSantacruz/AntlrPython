import sys
import re
from antlr4 import *
from tpiLexer import tpiLexer
from tpiParser import tpiParser
from tpiListener import tpiListener
 
def main():
    print ('Ingrese el  nombre del archivo o entrer para escribir desde consola.')
    arg = input()
    if not bool((arg)) :
        f = open("test.txt", "w+")
        arg = "test.txt"
        fin = re.compile("[fF][iI][nN]_[aA][cC][cC][iI][oO][nN]")
        print('Ingrese el Pseudocodigo: \n')
        linea = input()
        while fin.search(linea) == None :
            linea += '\n'
            f.write(linea)
            linea = input() 
        linea += '\n'
        f.write(linea)
        f.close()
    input_stream = FileStream(arg)
    lexer = tpiLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tpiParser(stream)
    tree = parser.start()
    printer = tpiListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    input()
 
if __name__ == '__main__':
    main()
