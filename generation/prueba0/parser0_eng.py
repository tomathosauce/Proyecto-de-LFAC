import ply.yacc as yacc
from lexer import lexer, tokens

# ORDEN DE OPERACIONES
precedence = (
    ( 'left', 'MAS', 'MENOS' ),
    ( 'left', 'POR', 'ENTRE' ),
)

# EXPRESIONES
def p_expression(p):
    """expression   : expression MAS expression
                    | expression MENOS expression
                    | expression POR expression
                    | expression ENTRE expression
                    | PARIZ expression PARDE
                    | ABRE_RPN special_expression CIERRA_RPN
                    | variable
                    | number"""
                    
    

# EXPRESIONES ESPECIALES
def p_special_expression(p):
    """special_expression   : special_expression special_expression MAS
                            | special_expression special_expression MENOS
                            | special_expression special_expression POR
                            | special_expression special_expression ENTRE
                            | variable
                            | number"""

def p_error(p):
    if p != None:
        raise SyntaxError("Error de sintaxis: Linea {}, Token '{}'".format(p.lineno, p.value))
    else:
        raise SyntaxError("Error de EOF")

parser = yacc.yacc()
debug = False

def main():
    inputFile = input("Ingrese la ruta del archivo: ")
    with open(inputFile) as file:
        data = file.read()
        print("Archivo:")
        print("="*30)
        print(data)
        print("="*30)
        print("Parsing {}...".format(inputFile))
        try:
            parser.parse(data, debug=debug)
            print("👽 Parse Sin Errores 👽")
        except:
            print("👿 Error de Sintaxis 👿")

if __name__=="__main__":
    main()