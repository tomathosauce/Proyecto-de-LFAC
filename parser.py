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

# CUERPO DEL PROGRAMA
def p_start(p):
    """start : INICIO PUNTO list_sentences FIN PUNTO"""

# REGLA DE PRODUCCION PARA 0 O MAS SENTENCIAS
def p_list_sentences(p):
    """list_sentences   : 
                        | list_sentences sentence
                        | sentence"""

# DEFINICION DE SENTENCIAS
def p_sentence(p):
    """sentence : datatype list_id PUNTO
                | control_statement PUNTO
                | assignment_statement PUNTO
                | system_function_call_statement PUNTO"""
                
# REGLA DE PRODUCCION PARA MULTIPLES DECLARACIONES EN 1 LINEA
def p_list_id(p):
    """list_id  : list_id COMA IDENTIF
                | IDENTIF"""
           
# SENTENCIAS DE CONTROL     
def p_control_statement(p):
    """control_statement    : if_statement
                            | while_statement"""

def p_if_statement(p):
    """if_statement : CUANDO expression ENTONCES list_sentences LISTO
                    | CUANDO expression ENTONCES list_sentences SINO list_sentences LISTO"""

def p_while_statement(p):
    """while_statement : MIENTRAS expression ENTONCES list_sentences LISTO"""

# SENTENCIAS DE ASIGNACION    
def p_assignment_statement(p):
    """assignment_statement : IDENTIF IGUAL expression
                            | IDENTIF IGUAL special_expression
                            | IDENTIF IGUAL CADENA_VALOR"""
                            
# LLAMADAS A FUNCIONES DEL SISTEMA INCLUIDAS EN EL LENGUAJE                      
def p_system_function_call_statement(p):
    """system_function_call_statement   : IMPRIMIR PARIZ list_arg PARDE
                                        | LEER PARIZ list_id PARDE"""                

# REGLA PARA ARGUMENTOS DE UNA FUNCION
def p_list_arg(p):
    """list_arg : list_arg COMA arg
                | arg"""
            
# DEFINICION DE ARGUMENTO DE FUNCION
def p_arg(p):
    """arg  : IDENTIF
            | expression
            | CADENA_VALOR"""

def p_operator(p):
    """operator : arithmetic_operator
                | logic_operator
                | relational_operator
                | equality_operator"""

# OPERADORES ARITMETICOS
def p_arithmetic_operator(p):
    """arithmetic_operator  : MAS
                            | MENOS
                            | POR
                            | ENTRE"""
# OPERADORES LOGICOS
def p_logic_operator(p):
    """logic_operator   : O
                        | Y
                        | NO"""
# OPERADORES RELACIONALES
def p_relational_operator(p):
    """relational_operator  : MAYORQUE
                            | MENORQUE
                            | MAYOR_IGUAL
                            | MENOR_IGUAL"""

def p_equality_operator(p):
    """equality_operator  : EQUIVALE
                            | DIFIERE"""
                            
# TIPOS DE DATOS
def p_datatype(p):
    """datatype : ENTERO
                | CADENA
                | REAL
                | BOOLEANO"""

# EXPRESIONES
def p_expression(p):
    """expression   : expression operator expression
                    | PARIZ expression PARDE
                    | NO expression
                    | ABRE_RPN special_expression CIERRA_RPN
                    | IDENTIF
                    | NUMERO
                    | boolean_value"""
                    
def p_boolean_value(p):
    """boolean_value    : CIERTO
                        | FALSO"""
                    
def p_expression_uminus(p):
    """expression : MENOS expression %prec UMINUS"""

# EXPRESIONES ESPECIALES
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
        print("Parsing {}...".format(inputFile))
        try:
            parser.parse(data, debug=debug)
            print("Parse successfully")
        except:
            print("Syntax error")

if __name__=="__main__":
    main()