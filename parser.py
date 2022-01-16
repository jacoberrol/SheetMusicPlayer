import ply.lex as lex
import ply.yacc as yacc

from song import Song
from song import Note

tokens = [
    'WHOLE_DURATION',
    'FRACTIONAL_DURATION',
    'PITCH',
    'OCTAVE'
]

t_WHOLE_DURATION = r'1'
t_FRACTIONAL_DURATION = r'\([1]/[2|4|8|16]\)?'
t_PITCH = r'[A-G][#|b]*'

def t_OCTAVE(t):
    r'[-1-9]'
    t.value = int(t.value)
    return t

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def remove_parens(str):
    return str.replace("(","").replace(")","")

def p_song(p):
    'song : song note'
    p[1].appendNote(p[2])
    p[0] = p[1]


def p_song_note(p):
    'song : note'
    song = Song(tempo=100)
    song.appendNote(p[1])
    p[0] = song


def p_note(p):
    '''note : FRACTIONAL_DURATION PITCH OCTAVE
            | WHOLE_DURATION PITCH OCTAVE'''
    p[0] = Note(p[2], duration=remove_parens(p[1]), octave=p[3])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

## TEST LEXER

data = '(1/4)C3 (1/4)C#3 (1/4)D3 (1/4)Eb3 (1/4)E3 (1/4)F3 (1/4)F#3 (1/4)G3 (1/4)Ab3 (1/4)A3 (1/4)A#3 (1/4)B3 (1/4)B#4'

lexer.input(data)

for tok in lexer:
    print(tok)


## TEST PARSER

result = parser.parse(data)
result.play()
