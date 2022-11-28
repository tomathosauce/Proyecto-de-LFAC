import ply.yacc as yacc
from Lexico import lexer, tokens

precedence = (
    ( 'left', 'MAS', 'MENOS' ),
    ( 'left', 'POR', 'ENTRE' ),
    ( 'right', 'UMINUS' )
)

def p_start(p):
    """start : INICIO PUNTO list_sentences FIN PUNTO"""

def p_list_sentences(p):
    """list_sentences   : list_sentences sentence_with_punto
                        | sentence_with_punto"""

def p_sentence_with_pluto(p):
    """sentence_with_punto  : sentence PUNTO"""

def p_sentence(p):
    """sentence : ENTERO list_id
                | CADENA list_id
                | REAL list_id
                | IMPRIMIR PARIZ list_arg PARDE
                | LEER PARIZ list_id PARDE
                | IDENTIF IGUAL expression
                | IDENTIF IGUAL special_expression
                | IDENTIF IGUAL CADENA_VALOR"""

def p_list_arg(p):
    """list_arg : list_arg COMA arg
                | arg"""

def p_arg(p):
    """arg  : IDENTIF
            | expression
            | special_expression
            | CADENA_VALOR"""

def p_operator(p):
    """operator : MAS
                | MENOS
                | POR
                | ENTRE"""

def p_list_id(p):
    """list_id  : list_id COMA IDENTIF
                | IDENTIF"""

def p_expression_operator(p):
    """expression   : expression operator expression"""

def p_expression_parens(p):
    """expression   : PARIZ expression PARDE"""

def p_expression_num_id(p):
    """expression   : IDENTIF
                    | NUMERO"""

def p_expression_uminus(p):
    """expression   : MENOS expression %prec UMINUS"""

def p_special_expression(p):
    """special_expression   : IDENTIF IDENTIF operator
                            | NUMERO NUMERO operator
                            | NUMERO IDENTIF operator
                            | IDENTIF NUMERO operator"""

def p_error(p):
    raise SyntaxError

parser = yacc.yacc()
debug = False
def main():
    inputFile = input("File path: ")
    with open(inputFile) as file:
        data = file.read()
        print("Data:")
        print("="*30)
        print(data)
        print("="*30)
        print(f"Parsing {inputFile}...",end=" ")
        try:
            parser.parse(data, debug=debug)
            print("Parse successfully")
        except:
            print("Syntax error")

if __name__=="__main__":
    main()