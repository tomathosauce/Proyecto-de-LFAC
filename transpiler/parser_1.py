import ply.yacc as yacc
from lexer import lexer, tokens
from enum import Enum

# ORDEN DE OPERACIONES
precedence = (
    ('right', 'NO'),
    ('left', 'O'),
    ('left', 'Y'),
    ('left', 'EQUIVALE', 'DIFIERE'),
    ('left', 'MAYORQUE', 'MENORQUE', 'MAYOR_IGUAL', 'MENOR_IGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'ENTRE'),
    ('right', 'UMINUS')
)

# CUERPO DEL PROGRAMA


def p_start(p):
    """start : INICIO PUNTO list_sentences FIN PUNTO
             | INICIO PUNTO FIN PUNTO"""

    if len(p) == 6:
        # print("AST: ")
        # print(p[3])
        p[0] = ('program', p[3])

# REGLA DE PRODUCCION PARA 1 O MAS SENTENCIAS


def p_list_sentences(p):
    """list_sentences   : list_sentences sentence
                        | sentence"""
    if len(p) == 2:
        if p[1] != None:
            p[0] = [p[1]]
    else:
        if p[2] != None:
            if p[1] != None:
                p[0] = p[1] + [p[2]]
            else:
                p[0] = [p[2]]

# DEFINICION DE SENTENCIAS


def p_sentence(p):
    """sentence : datatype list_id PUNTO
                | control_statement
                | assignment_statement PUNTO
                | system_function_call_statement PUNTO"""
    # print('sentence')
    # print(list(p))
    if p[1] in ['entero', 'real', 'booleano', 'cadena']:
        p[0] = ('declare', p[1], p[2])
    else:
        p[0] = p[1]

# REGLA DE PRODUCCION PARA MULTIPLES DECLARACIONES EN 1 LINEA


def p_list_id(p):
    """list_id  : list_id COMA IDENTIF
                | IDENTIF"""
    # print('list_id')
    # print(list(p))
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


# SENTENCIAS DE CONTROL
def p_control_statement(p):
    """control_statement    : if_statement
                            | while_statement"""

    p[0] = p[1]


def p_if_statement(p):
    """if_statement : CUANDO expression ENTONCES list_sentences LISTO
                    | CUANDO expression ENTONCES list_sentences SINO list_sentences LISTO"""
    if len(p) == 6:
        p[0] = ('if', p[2], p[4])
    else:
        p[0] = ('if-else', p[2], p[4], p[6])


def p_while_statement(p):
    """while_statement : MIENTRAS expression ENTONCES list_sentences LISTO"""

    p[0] = ('while', p[2], p[4])

# SENTENCIAS DE ASIGNACION


def p_assignment_statement(p):
    """assignment_statement : IDENTIF IGUAL expression
                            | IDENTIF IGUAL CADENA_VALOR"""

    p[0] = ('assign', p[1], p[3])

# LLAMADAS A FUNCIONES DEL SISTEMA INCLUIDAS EN EL LENGUAJE


def p_system_function_call_statement(p):
    """system_function_call_statement   : IMPRIMIR PARIZ list_arg PARDE
                                        | LEER PARIZ list_id PARDE"""
    if p[1] == 'Imprimir':
        p[0] = ('print', p[3])
    elif p[1] == 'Leer':
        p[0] = ('read', p[3])

# REGLA PARA ARGUMENTOS DE UNA FUNCION


def p_list_arg(p):
    """list_arg : list_arg COMA arg
                | arg"""

    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

# DEFINICION DE ARGUMENTO DE FUNCION


def p_arg(p):
    """arg  : expression
            | CADENA_VALOR"""
    p[0] = p[1]

# TIPOS DE DATOS


def p_datatype(p):
    """datatype : ENTERO
                | CADENA
                | REAL
                | BOOLEANO"""
    # print('datatype: ')
    # print(list(p))
    p[0] = p[1]

# EXPRESIONES


def p_bin_expression(p):
    """expression : expression MAS expression
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
                    """
    p[0] = ('binary_expression', p[2], p[1], p[3])


def p_unary_expression(p):
    """expression : NO expression
    """
    p[0] = ('negated', p[2])


def p_expression_paren(p):
    """expression : PARIZ expression PARDE
                    | ABRE_RPN special_expression CIERRA_RPN
    """
    p[0] = p[2]


def p_value(p):
    """expression : IDENTIF
                | NUMERO
                | boolean_value
    """

    p[0] = p[1]


def p_expression_uminus(p):
    """expression : MENOS expression %prec UMINUS"""
    p[0] = ('uminus', p[2])


def p_boolean_value(p):
    """boolean_value    : CIERTO
                        | FALSO"""

    p[0] = p[1]


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
    if len(p) == 4:
        p[0] = ('binary_expression', p[3], p[1], p[2])
    elif p[1] == '!':
        p[0] = ('negated', p[2])
    else:
        p[0] = p[1]


def p_error(p):
    if p != None:
        raise SyntaxError(
            f"Error de sintaxis: Linea {p.lineno}, Token '{p.value}'")
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
            result = parser.parse(data, debug=debug)
            print("👽 Parse Sin Errores 👽")
            print(result)
        except:
            print("👿 Error de Sintaxis 👿")


if __name__ == "__main__":
    main()
