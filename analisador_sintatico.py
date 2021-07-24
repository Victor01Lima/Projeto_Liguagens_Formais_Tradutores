import ply.lex as lex
from analisador_lexico import tokens
import ply.yacc as yacc



### Metodo topLevelDeclaration ###
def p_start (p):
    '''topLevelDeclaration : functionSignature body
                         | type initializedIdentifierList POINT_V
                         | functionSignature body topLevelDeclaration   
                         | type initializedIdentifierList  POINT_V  topLevelDeclaration '''


def p_topLevelDeclaration_functionSignature(p):
    '''topLevelDeclaration : functionSignature body

    '''
##Implementar todos os metodos
###  ###

parser = yacc.yacc()


parser.parse()