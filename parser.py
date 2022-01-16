import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'PITCH'
]

t_PITCH = r'[A-G]'

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


def p_expression_song(p):
    'song : song pitch'

def p_expression_note(p):
    'note : PITCH'
    p[0] = p[1]


## TEST

data = 'C D E F G A B C'

lexer.input(data)

for tok in lexer:
    print(tok)
