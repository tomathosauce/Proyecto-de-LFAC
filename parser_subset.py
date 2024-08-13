import ply.yacc as yacc
from lexer import lexer, tokens

# ORDEN DE OPERACIONES
precedence = (
    ( 'right', 'NO'),
    ( 'left', 'O'),
    ( 'left', 'Y'),
    ( 'left', 'EQUIVALE', 'DIFIERE' ),
    ( 'left', 'MAYORQUE', 'MENORQUE', 'MAYOR_IGUAL', 'MENOR_IGUAL' ),
    ( 'left', 'MAS', 'MENOS' ),
    ( 'left', 'POR', 'ENTRE' ),
    ( 'right', 'UMINUS' )
)

# EXPRESIONES
def p_expression(p):
    """expression   : expression MAS expression
                    | expression MENOS expression
                    | expression POR expression
                    | expression ENTRE expression
                    | expression MAYORQUE expression
                    | expression MENORQUE expression
                    | expression MAYOR_IGUAL expression
                    | expression MENOR_IGUAL expression
                    | expression EQUIVALE expression
                    | expression DIFIERE expression
                    | expression O expression
                    | expression Y expression
                    | PARIZ expression PARDE
                    | NO expression
                    | ABRE_RPN special_expression CIERRA_RPN
                    | IDENTIF
                    | NUMERO
                    | boolean_value"""
                    
def p_expression_uminus(p):
    """expression : MENOS expression %prec UMINUS"""
    
def p_boolean_value(p):
    """boolean_value    : CIERTO
                        | FALSO"""
                    

# EXPRESIONES ESPECIALES
def p_special_expression(p):
    """special_expression   : special_expression special_expression MAS
                            | special_expression special_expression MENOS
                            | special_expression special_expression POR
                            | special_expression special_expression ENTRE
                            | special_expression special_expression MAYORQUE
                            | special_expression special_expression MENORQUE
                            | special_expression special_expression MAYOR_IGUAL
                            | special_expression special_expression MENOR_IGUAL
                            | special_expression special_expression EQUIVALE 
                            | special_expression special_expression DIFIERE 
                            | special_expression special_expression O 
                            | special_expression special_expression Y 
                            | NO special_expression 
                            | IDENTIF
                            | NUMERO
                            | boolean_value"""

def p_expression_uminus(p):
    """special_expression : MENOS special_expression %prec UMINUS"""

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