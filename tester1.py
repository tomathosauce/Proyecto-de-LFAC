from lexer import lexer, tokens
from parser_1 import parser
from os import path, getcwd, sep

import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("direccion")
argparser.add_argument("--cwd", action="store_true")
argparser.add_argument("--debug", action="store_true")
argparser.add_argument("--long", action="store_true")
args = argparser.parse_args()

if args.cwd:
    inputFile = path.join(getcwd(), args.direccion.replace('/', sep).replace('\\', sep))
else:
    inputFile = args.direccion
    
debug = args.debug
def main():
    with open(inputFile) as file:
        lines = file.readlines()
        for line in lines:
            try:
                parser.parse(line, debug=debug, lexer=lexer)
                print("👽 Sin errores 👽")
            except Exception as e:
                print("😡 Se encontraron problemas 😡")
                if hasattr(e, 'message'):
                    print(e.message)
                else:
                    print(e)
            
if __name__=="__main__":
    main()