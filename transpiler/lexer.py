import ply.lex as lex
from ply.lex import TOKEN

tokens = [
    'NUMERO',
    'MAS',
    'MENOS',
    'POR',
    'ENTRE',
    'PARIZ', # PARENTESIS IZQUIERDO
    'PARDE', # PARENTESIS DERECHO
    'IGUAL',
    'PUNTO',
    'COMA',
    'IDENTIF',
    'IDENTIF_ILEGAL',
    'CADENA_VALOR',
    'MAYORQUE',
    'MENORQUE',
    'MAYOR_IGUAL',
    'MENOR_IGUAL',
    'EQUIVALE',
    'DIFIERE',
    'O',
    'Y',
    'NO',
    'ABRE_RPN',
    'CIERRA_RPN'
]

t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_ENTRE = r'\/'
t_PARIZ = r'\('
t_PARDE = r'\)'
t_IGUAL = r'\='
t_PUNTO = r'\.'
t_COMA = r'\,'
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_MAYOR_IGUAL = r'\>\='
t_MENOR_IGUAL = r'\<\='
t_EQUIVALE = r'\=\='
t_DIFIERE = r'\!\='
t_O = r'\|\|'
t_Y = r'\&\&'
t_NO = r'\!'
t_ABRE_RPN = r'\['
t_CIERRA_RPN = r'\]'

t_ignore = ' \t'

reserved = {
   'Imprimir' : 'IMPRIMIR',
   'Leer' : 'LEER',
   'INICIO' : 'INICIO',
   'FIN' : 'FIN',
   'entero': 'ENTERO',
   'real': 'REAL',
   'cadena': 'CADENA',
   'booleano': 'BOOLEANO',
   'mientras': 'MIENTRAS',
   'cuando': 'CUANDO',
   'sino': 'SINO',
   'listo': 'LISTO',
   'Cierto': 'CIERTO',
   'Falso': 'FALSO',
   'entonces': 'ENTONCES'
}

tokens = tokens + list(reserved.values())

digito = r'(\d)'
letra = r'([_A-Za-z])'
identificador = r'(' + letra + r'(' + digito + r'|' + letra + r')*)'

#IDENTIFICADORES
@TOKEN(identificador)
def t_IDENTIF(t):
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

@TOKEN(r'(' + digito + r'(' + digito + r'|' + letra + r')*'+letra+r'(' + digito + r'|' + letra + r')*)')
def t_IDENTIF_ILEGAL(t):
    raise SyntaxError("Identificador inválido: Línea {}".format(t.lineno+1))

# NUMEROS (CON DECIMALES)
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    return t

# CADENAS VALOR
def t_CADENA_VALOR(t):
    r'\".[^"]*\"'
    return t

# PARA LLEVAR LA CUENTA DEL NUMERO DE LINEA
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter ilegal {}".format(t.value))
    t.lexer.skip(1)
    
def t_eof(t):
    return None

lexer = lex.lex()

def main():
    inputFile = input("File path: ")
    with open(inputFile, "r") as file:
        lexer.input(file.read())

        while True:
            tok = lexer.token()
            if not tok: break
            print(tok)

if __name__=="__main__":
    main()