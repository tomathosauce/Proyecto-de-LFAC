#@title Importar librerias
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG

#@title Subconjunto de lenguaje (solo expresiones)
grammar_subset = CFG.fromstring("""
expression -> expression "MAS" expression | expression "MENOS" expression | expression "POR" expression | expression "ENTRE" expression | expression "MAYORQUE" expression | expression "MENORQUE" expression | expression "MAYOR_IGUAL" expression | expression "MENOR_IGUAL" expression | expression "EQUIVALE" expression | expression "DIFIERE" expression | expression "O" expression | expression "Y" expression | "PARIZ" expression "PARDE" | "NO" expression | "ABRE_RPN" special_expression "CIERRA_RPN" | "IDENTIF" | "NUMERO" | boolean_value
boolean_value -> "CIERTO" | "FALSO"
special_expression -> special_expression special_expression "MAS" | special_expression special_expression "MENOS" | special_expression special_expression "POR" | special_expression special_expression "ENTRE" | special_expression special_expression "MAYORQUE" | special_expression special_expression "MENORQUE" | special_expression special_expression "MAYOR_IGUAL" | special_expression special_expression "MENOR_IGUAL" | special_expression special_expression "EQUIVALE" | special_expression special_expression "DIFIERE" | special_expression special_expression "O" | special_expression special_expression "Y" | "NO" special_expression | "IDENTIF" | "NUMERO" | boolean_value
""")

grammar_subset_result = generate(grammar_subset, depth=5)

gsrl = list(grammar_subset_result)

with open('grammar_subset_result.txt2', 'w') as f:
  for item in gsrl:
    f.write("{}\n".format(" ".join(item)))