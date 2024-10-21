
def indentation(level):
    return '    ' * level


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
        print(ast)
        return "\n" + indentation(level) + f'{translate_ast_to_python(ast[1])} = {translate_ast_to_python(ast[2])}'
    elif ast[0] == 'binary_expression':
        exp1 = translate_ast_to_python(ast[2])
        exp2 = translate_ast_to_python(ast[3])
        sym = ast[1]

        if sym == '||':
            sym = 'or'
        if sym == '&&':
            sym = 'and'

        # if sym == '*':
        #     ops = ['+', '-']
        #     if type(exp1) == tuple and exp1[1] in ops:
        #         exp1 = f'({exp1})'
        #     if type(exp2) == tuple and exp2[1] in ops:
        #         exp2 = f'({exp2})'

        exp = f'{exp1} {sym} {exp2}'

        # print('AST: ', ast)
        # print("result: ", exp)

        return exp
    elif ast[0] == 'if':
        print('if')
        print(ast[2])
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
