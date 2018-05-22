import ply.lex as lex

tokens = [ 'NUMBER', 'MAYOROIGUAL', 'MENOROIGUAL', 'PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' , 'MAYOR', 'MENOR', 'DIFERENTE', 'PARA', 'EN', 'HAGA', 'SI', 'NAME', 'EQUIVALE','SINO', 'MIENTRAS', 'ABRIRLLAVE', 'CERRARLLAVE']



t_ignore = ' \t\n'

t_PLUS = r'\+'

t_MINUS = r'-'

t_TIMES = r'\*'

t_DIVIDE = r'/'

t_EQUALS = r'\='

t_MAYOR= r'>'

t_MAYOROIGUAL = r'>='

t_MENOROIGUAL = r'<='

t_MENOR= r'<'

t_DIFERENTE= r'!='

t_EQUIVALE= r'=='

t_ABRIRLLAVE= r'\('

t_CERRARLLAVE= r'\)'

#t_PARA = r'for'



t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)   
    return t

def t_PARA(t): 
    r'for\b'
    return t

def t_SI(t): 
    r'if\b'
    return t

def t_SINO(t): 
    r'else\b'
    return t


def t_HAGA(t): 
    r'do\b'
    return t

def t_EN(t): 
    r'in\b'
    return t

def t_MIENTRAS(t): 
    r'while\b'
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

#f=open('prueba.txt','r')
#print f.readline()

#lex.input("if x >= 3 do x = 2*3")

#lex.input("x = 3 - 44 + 5 * 6 > < != == for in if do while ")

#lex.input(f.readline())

def start ():
    f=open('algo.txt','r')
    lista= f.readlines()
    print lista
    for i in range(len(lista)):
	lex.input(lista[i])

	while True:
            tok = lex.token()
	    if not tok: break
	    print str(tok.value) + " - " + str(tok.type)


start()
