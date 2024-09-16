from lexer import lexer, tokens
from parser_1 import parser
from os import path, getcwd, sep

import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("direccion")
argparser.add_argument("--cwd", action="store_true")
argparser.add_argument("--debug", action="store_true")
argparser.add_argument("--tokens", action="store_true")
args = argparser.parse_args()

if args.cwd:
    inputFile = path.join(getcwd(), args.direccion.replace('/', sep).replace('\\', sep))
else:
    inputFile = args.direccion
    
debug = args.debug
def main():
    with open(inputFile) as file:
        data = file.read()
        print("Data:")
        print("="*30)
        print(data)
        if args.tokens:
            print("="*30)
            print("Tokens")
            n_lexer = lexer.clone()
            n_lexer.input(data)
            while True:
                tok = n_lexer.token()
                if not tok: break
                print(tok)
            
        print("="*30)
        print("Analizando {}".format(inputFile))
        print("="*30)
        try:
            parser.parse(data, debug=debug, lexer=lexer)
            print("👽 Sin errores 👽")
        except Exception as e:
            print("😡 Se encontraron problemas 😡")
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
            
if __name__=="__main__":
    main()