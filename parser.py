import ply.lex as lex
import ply.yacc as yacc

from song import Song
from song import Note

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


def p_song(p):
    'song : song note'
    p[1].appendNote(Note(p[2], octave=4, duration="1/4"))
    p[0] = p[1]


def p_song_note(p):
    'song : note'
    song = Song(tempo=100)
    song.appendNote(Note(p[1], octave=4, duration="1/4"))
    p[0] = song


def p_note(p):
    'note : PITCH'
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

## TEST LEXER

data = 'C D E F G A B C'

lexer.input(data)

for tok in lexer:
    print(tok)


## TEST PARSER

result = parser.parse(data)
result.play()
