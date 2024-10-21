ops = ['+', '-']


def indentation(level):
    return '    ' * level


def add_context_to_exp(ast: tuple):
    l = ['binary_expression']

    if ast[0] == 'binary_expression':
        sym = ast[1]
        l.append(sym)
        if sym == '*':
            if type(ast[2]) == tuple:
                l.append(list(ast[2]) + [sym])
            else:
                l.append(ast[2])

            if type(ast[3]) == tuple:
                l.append(list(ast[3]) + [sym])
            else:
                l.append(ast[3])

            return tuple(l)
    return ast


def translate_ast_to_python(ast, level=0):
    if ast[0] == 'program':
        return 'def main():' + ''.join(list(filter(lambda x: x != '', [translate_ast_to_python(x, level + 1) for x in ast[1]])))
    elif ast[0] == 'declare':
        return ''
    elif ast[0] == 'print':
        return "\n" + indentation(level) + f'print({", ".join([translate_ast_to_python(x) for x in ast[1]])})'
    elif ast[0] == 'read':
        return f'\n{indentation(level)}'+f'\n{indentation(level)}'.join([f'{x} = input()' for x in ast[1]])
    elif ast[0] == 'assign':
        return "\n" + indentation(level) + f'{translate_ast_to_python(ast[1])} = {translate_ast_to_python(ast[2])}'
    elif ast[0] == 'binary_expression':
        if ast[1] == '*':
            ast_context = add_context_to_exp(ast)
        else:
            ast_context = ast

        exp1 = translate_ast_to_python(ast_context[2])
        exp2 = translate_ast_to_python(ast_context[3])
        sym = ast_context[1]

        if sym == '||':
            sym = 'or'
        if sym == '&&':
            sym = 'and'

        if sym in ops and len(ast_context) == 5 and ast_context[4] == '*':
            exp = f'({exp1} {sym} {exp2})'
        else:
            exp = f'{exp1} {sym} {exp2}'

        return exp
    elif ast[0] == 'if':
        return "\n" + indentation(level) + 'if ' + translate_ast_to_python(ast[1]) + ':' \
               + ''.join([translate_ast_to_python(x, level + 1)
                         for x in ast[2]])
    elif ast[0] == 'if-else':
        return "\n" + indentation(level) + 'if ' + translate_ast_to_python(ast[1]) + ':' \
               + ''.join([translate_ast_to_python(x, level + 1)
                         for x in ast[2]]) + '\n' + indentation(level) + 'else:' + ''.join([translate_ast_to_python(x, level + 1)
                                                                                            for x in ast[3]])
    elif ast[0] == 'while':
        return "\n" + indentation(level) + 'while ' + translate_ast_to_python(ast[1]) + ':' \
               + ''.join([translate_ast_to_python(x, level + 1)
                         for x in ast[2]])
    elif ast[0] == 'negated':
        return "not " + translate_ast_to_python(ast[1])

    if type(ast) == str or type(ast) == int or type(ast) == float:
        if type(ast) == str:
            if ast == 'Falso':
                return 'False'
            elif ast == 'Cierto':
                return 'True'

        return ast

    return ''
