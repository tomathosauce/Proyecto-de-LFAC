from lexer import lexer, tokens
from parser import parser
from os import path, getcwd, sep

import argparse, re

argparser = argparse.ArgumentParser()
argparser.add_argument("direccion")
argparser.add_argument("--cwd", action="store_true")
args = argparser.parse_args()

if args.cwd:
    inputFile = path.join(getcwd(), args.direccion.replace('/', sep).replace('\\', sep))
else:
    inputFile = args.direccion
    
debug = False
def main():
    with open(inputFile) as file:
        data = file.read()
        print("Data:")
        print("="*30)
        print(data)
        print("="*30)
        
        print("Tokens")
        
        lexer.input(file.read())
        while True:
            tok = lexer.token()
            if not tok: break
            print(tok)
            
        print("="*30)
        print("Analizando {}".format(inputFile))
        print("="*30)
        try:
            parser.parse(data, debug=debug, lexer=lexer)
            print("Sin errores")
        except Exception as e:
            print("Errores de sintaxis encontrados")
            
if __name__=="__main__":
    main()