#Lexer -- Análisis léxico de un pseudocódigo en español

import sys
import re

def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens
  
RESERVED = 'RESERVED'
INT = 'INT'
ID = 'ID'

token_exprs = [
      (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
      
    (r'inicio', RESERVED),
    (r'fin', RESERVED),
    (r'Proceso', RESERVED),
    (r'FinProceso', RESERVED),
    (r'Escribir',RESERVED),
    (r'Leer',RESERVED ),
    (r'\ +', RESERVED),
    (r'- ', RESERVED),
    (r'\ *', RESERVED),
    (r'/', RESERVED),
    (r'<=', RESERVED),
    (r'<', RESERVED),
    (r'> =', RESERVED),
    (r'>', RESERVED),
    (r'=', RESERVED),
    (r'! =', RESERVED),
    (r'Mod', RESERVED),
    (r'Desde', RESERVED),
    (r'Hasta', RESERVED),
    (r'repetir',RESERVED),
    (r'finDesde',RESERVED),
    (r'Imprimir',RESERVED),
    (r';', RESERVED),



   (r'[0-9] +', INT),
    (r'[A-Za-z] [A-Za-z0-9 _] *', ID),
]

def imp_lex (personajes):
    return lexer.lex (caracteres, token_exprs)

import sys
from imp_lexer import *


#PRUEBA

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = imp_lex(characters)
    for token in tokens:
        print (token)
    
