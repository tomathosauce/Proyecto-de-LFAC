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
    'CADENA'
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

t_ignore = ' \t\n'

reserved = {
   'Imprimir' : 'IMPRIMIR',
   'Leer' : 'LEER',
   'INICIO' : 'INICIO',
   'FIN' : 'FIN',
   'entero': 'ENTERO',
   'real': 'REAL',
   'cadena': 'CADENA'
}

tokens = tokens + list(reserved.values())

digito = r'(\d)'
letra = r'([_A-Za-z])'
identificador = r'(' + letra + r'(' + digito + r'|' + letra + r')*)'

#IDENTIFICADORES
@TOKEN(identificador)
def t_IDENTIF(t):
    #r'[_A-Za-z]+'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t
# NUMEROS (CON DECIMALES)
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    return t

# CADENAS
def t_CADENA(t):
    r'\".[^"]*\"'
    return t

def t_error(t):
    print("Caracter ilegal {}".format(t.value))
    t.lexer.skip(1)
    
def t_eof(t):
    return None

lexer = lex.lex()

f = open("./pruebas/ejemplo.txt", "r")

lexer.input(f.read())


while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)