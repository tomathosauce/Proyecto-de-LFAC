from lexer import lexer, tokens
from parser_subset import parser
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

def transform(token: str):
    match token:
        case 'NUMERO':
            return 1
        case 'MAS':
            return '+'
        case 'MENOS':
            return '-'
        case 'POR':
            return '*'
        case 'ENTRE':
            return '/'
        case 'PARIZ':
            return '('
        case 'PARDE':
            return ')'
        case 'IGUAL':
            return '='
        case 'PUNTO':
            return '.'
        case 'COMA':
            return ','
        case 'IDENTIF':
            return 'a'
        case 'CADENA_VALOR':
            return '"a"'
        case 'MAYORQUE':
            return '>'
        case 'MENORQUE':
            return '<'
        case 'MAYOR_IGUAL':
            return '>='
        case 'MENOR_IGUAL':
            return '<='
        case 'EQUIVALE':
            return '=='
        case 'DIFIERE':
            return '!='
        case 'O':
            return '||'
        case 'Y':
            return '&&'
        case 'NO':
            return '!'
        case 'ABRE_RPN':
            return '['
        case 'CIERRA_RPN':
            return ']'
        case 'CIERTO':
            return 'Cierto'
        case 'FALSO':
            return 'Falso'
    return ''
    
def preprocess(s: str):
    return ' '.join([str(transform(x)) for x in s.split()])
    
debug = args.debug
def main():
    with open(inputFile) as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            pp = preprocess(line)
            try:
                # print("Probando: {} ({})".format(pp, line))
                parser.parse(pp, debug=debug, lexer=lexer)
                # print("👽 Sin errores 👽")
            except Exception as e:
                print("Probando: {} ({})".format(pp, line))
                print("😡 Se encontraron problemas 😡")
                if hasattr(e, 'message'):
                    print(e.message)
                else:
                    print(e)
            count += 1
            
if __name__=="__main__":
    main()