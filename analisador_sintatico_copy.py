import ply.lex as lex
from analisador_lexico import tokens
import ply.yacc as yacc



### Metodo topLevelDeclaration ###    
def p_topLevelDeclaration_functionSignature(p):
    '''topLevelDeclaration : functionSignature body'''

def p_topLevelDeclaration_type_initializedIdentifierList_POINT_V(p):
    '''topLevelDeclaration : type initializedIdentifierList POINT_V'''




parser = yacc.yacc()


parser.parse()