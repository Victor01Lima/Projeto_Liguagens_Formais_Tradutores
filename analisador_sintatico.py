import ply.lex as lex
from analisador_lexico import tokens
import ply.yacc as yacc

### Metodo topLevelDeclaration ###    
def p_topLevelDeclaration_functionSignature(p):
    '''topLevelDeclaration : functionSignature body'''

def p_topLevelDeclaration_type_initializedIdentifierList_POINT_V(p):
    '''topLevelDeclaration : type initializedIdentifierList POINT_V'''

def p_topLevelDeclaration_functionSignature_body_topLevelDeclaration(p):
    ''' topLevelDeclaration : functionSignature body topLevelDeclaration'''

def p_topLevelDeclaration_type_initializedIdentifierList_POINT_V_topLevelDeclaration(p):
    '''topLevelDeclaration : type initializedIdentifierList  POINT_V  topLevelDeclaration'''

### Metodo initializedIdentifierList ###
def p_initializedIdentifierList(p): #duvida aqui
   ''' initializedIdentifierList : ID EQUAL expression p_initializedIdentifierList_estrela 
'''

def p_initializedIdentifierList_estrela(p):
    ''' p_initializedIdentifierList_estrela : COMMA ID EQUAL expression
                            | COMMA ID EQUAL expression  p_initializedIdentifierList_estrela
    '''
### Metodo FunctionSignature ###
def p_functionSignature (p):
    ''' functionSignature : type ID formalParameterPart
                        | ID formalParameterPart
    '''

### Metodo type ###
def p_type_VOID(p):
    ''' type : VOID'''
def p_type_STRING(p):
    '''type : STRING'''
def p_type_BOOL(p):
    '''type : BOOL'''
def p_type_INT(p):
    '''type : INT'''
def p_type_FLOAT(p):
    '''type : FLOAT'''
def p_type_VAR(p):
    '''type : VAR'''

### Metodo formalParameterPart ###
def p_formalParameterPart(p):
    '''formalParameterPart  :  formalParameterList '''

### Metodo formalParameterList ###
def p_formalParameterList_void_(p):
    '''formalParameterList : OPEN_PARENTHESES CLOSE_PARENTHESES '''

### Metodo formalParameterList ###
def p_formalParameterList_normalFormal_Parameters(p):
    '''formalParameterList : OPEN_PARENTHESES normalFormalParameters COMMA  CLOSE_PARENTHESES  
                            |    OPEN_PARENTHESES normalFormalParameters  CLOSE_PARENTHESES 
'''

### Metodo normalFormalParameters ###
def p_normalFormalParameters(p): 
    '''normalFormalParameters : normalFormalParameter  p_normalFormalParameters_estrela'''
def p_normalFormalParameters_estrela(p):
    ''' 
        p_normalFormalParameters_estrela : COMMA normalFormalParameter
                                 | COMMA normalFormalParameter p_normalFormalParameters_estrela
    '''
### Metodo normalFormalParameter ###
def p_normalFormalParameter(p):
    '''normalFormalParameter : type ID '''

### Metodo body ###
def p_body_statements(p):
    '''body : OPEN_KEYS statements CLOSE_KEYS'''

def p_body__(p):
    '''body :  OPEN_KEYS CLOSE_KEYS'''

### Metodo statements ###
def p_statements_statements_statement(p):  ## resolver recurssão
    '''statements : statements statement '''

def p_statements_statement(p):
    '''statements : statement '''

### Metodo statement ###
def p_statement_body(p):
    ''' statement : body '''

def p_statement_localVariableDeclaration(p):
    '''statement : localVariableDeclaration '''

def p_statement_forStatement(p):
    ''' statement : forStatement '''

def p_statement_whileStatement(p):
    '''statement : whileStatement '''

def p_statement_ifStatement(p):
    ''' statement : ifStatement '''

def p_statement_breakStatement(p):
    ''' statement : breakStatement'''

def p_statement_continueStatement(p):
    ''' statement : continueStatement'''

def p_statement_returnStatement(p):
    ''' statement : returnStatement'''

def p_statement_expressionStatement(p):
    ''' statement : expressionStatement'''

### Metodo localVariableDeclaration ###
def p_localVariableDeclaration(p): #duvida
    '''localVariableDeclaration : type ID EQUAL expression expression_one_equal POINT_COMMA
                                | type ID  expression_one_equal POINT_COMMA 
                                | type ID EQUAL expression  COMMA ID  POINT_COMMA
                                | type ID  COMMA ID  POINT_COMMA
    '''

def p_expression_one_equal(p):
   ''' expression_one_equal : COMMA ID  EQUAL expression 
                            | COMMA ID
                            | COMMA ID  EQUAL expression expression_one_equal
                            | COMMA ID expression_one_equal'''
    
### Metodo forStatement ###
def p_forStatement_statement(p):
    '''forStatement : FOR OPEN_PARENTHESES  forLoopParts CLOSE_PARENTHESES statement'''

def p_forStatement_body(p):
    '''forStatement : FOR OPEN_PARENTHESES forLoopParts CLOSE_PARENTHESES body '''

### metodo forLoopParts ###
def p_forLoopParts_localVariableDeclaration(p):
    '''forLoopparts : localVariableDeclaration POINT_COMMA expression POINT_COMMA expressionList
                    | localVariableDeclaration POINT_COMMA POINT_COMMA expressionList
                    | localVariableDeclaration POINT_COMMA expression POINT_COMMA
                    | localVariableDeclaration POINT_COMMA POINT_COMMA
    '''

def p_forLoopParts_expression(p):
    '''forLoopparts : expression POINT_COMMA expression POINT_COMMA expressionList
                    | expression POINT_COMMA POINT_COMMA expressionList
                    | expression POINT_COMMA expression POINT_COMMA
                    | expression POINT_COMMA POINT_COMMA
    '''

def p_forLoopParts_type(p):
    '''forLoopParts : type ID IN expression
                    | ID IN expression
    '''

### Metodo expressionList ###
def p_expressionList_expression(p):
    '''expressionList : expression '''

def p_expressionList_expressionList(p):
    '''expressionList : expression COMMA expressionList '''

### Metodo whileStatement ###
def p_whileStatement_statement(p):
    ''' whileStatement :  WHILE OPEN_PARENTHESES expression CLOSE_PARENTHESES statement'''

def p_whileStatement_body(p):
    ''' whileStatement :  WHILE OPEN_PARENTHESES expression CLOSE_PARENTHESES body '''

### Metodo ifStatement ###
def p_ifStatement_statement_else_statement(p):
    '''ifStatement : IF OPEN_PARENTHESES expression CLOSE_PARENTHESES statement ELSE statement 
                    | IF OPEN_PARENTHESES expression CLOSE_PARENTHESES body ELSE body
                    | IF OPEN_PARENTHESES expression CLOSE_PARENTHESES statement ELSE body
                    | IF OPEN_PARENTHESES expression CLOSE_PARENTHESES statement 
                    | IF OPEN_PARENTHESES expression CLOSE_PARENTHESES body 
                    | IF OPEN_PARENTHESES expression CLOSE_PARENTHESES body ELSE statement
    '''

#def p_ifStatement_body_else_body(p):
#    '''ifStatement : IF OPEN_PARENTHESES expression CLOSE_PARENTHESES body ELSE body 
#                    | IF OPEN_PARENTHESES expression CLOSE_PARENTHESES body ELSE
#    '''

### Metodo breakStatement ###
def p_breakStatement(p):
    '''breakStatement : BREAK POINT_COMMA '''

### Metodo continueStatement ###
def p_continueStatement(p):
    ''' continueStatement : CONTINUE POINT_COMMA '''

### Metodo returnStatement ###
def p_returnStatement(p):
    '''expressionStatement : RETURN expression POINT_COMMA 
                        | RETURN POINT_COMMA
    '''

def p_expressionStatement(p):
    '''returnStatement : expression POINT_COMMA 
                        | POINT_COMMA
    '''

def p_expression(p):
    '''
        expression : expression EQUAL expression_0
                    | expression PLUS_EQUAL expression_0
                    | expression MINUS_EQUAL expression_0
                    | expression MULTIPLICATION_DIVISION expression_0
                    | expression DIVIDE_EQUAL expression_0
                    | expression_0
    '''

def p_expression_0(p):
    '''
        expression_0 : expression_0 OR expression_1
                    | expression_1
    ''' 

def p_expression_1(p):
    '''
        expression_1 : expression_1 AND expression_2
                    | expression_2
    '''

def p_expression_2(p):
    '''
        expression_2 :  expression_2 EQUAL_EQUAL expression_3
                    | expression_2 DIFFERENT expression_3
                    | expression_3
    '''

def p_expression_3(p):
    '''
        expression_3 :  expression_3 EQUAL_EQUAL expression_4
                    | expression_3 DIFFERENT expression_4
                    | expression_4
    '''

def p_expression_4(p):
    '''
        expression_4 : expression_4 LESS_THAN expression_5
                    | expression_4 GREATER_THAN expression_5
                    | expression_4 LESS_THAN_OR_EQUAL_TO expression_5
                    | expression_4 GREATER_THAN_OR_EQUAL_TO expression_5
                    | expression_5
    '''   

def p_expression_5(p):
    ''' 
        expression_5 :  expression_5 LOGIC_OR expression_6
                    | expression_6
    '''

def p_expression_6(p):
    ''' 
        expression_6 :  expression_6 LOGIC_AND expression_7
                    | expression_7
    '''

def p_expression_7(p):
    ''' 
        expression_7 :  expression_7 SHIFT_LEFT expression_8
                    | expression_7 SHIFT_RIGHT expression_8
                    | expression_8
    '''

def p_expression_8(p):
    '''
       expression_8 : expression_8 PLUS expression_9
                    | expression_8 MINUS expression_9
                    | expression_9
    '''

def p_expression_9(p):
    '''
        expression_9 : expression_9 MULT expression_10
                    | expression_9 PERCENTAGE expression_10
                    | expression_9 DIVIDE expression_10
                    | expression_10
    '''

def p_expression_10(p):
    '''
        expression_10 : MINUS expression_10
                    | PLUS_PLUS expression_10
                    | MINUS_MINUS expression_10
                    | INVERT expression_10
                    | expression_11
    '''

def p_expression_11(p):
    '''
        expression_11 : expression_11 MINUS_MINUS
                    | expression_11 PLUS_PLUS
                    | expression_11 OPEN_CONCHETE expression_11 CLOSE_CONCHETE
                    | OPEN_PARENTHESES expression CLOSE_PARENTHESES
                    | expression_12
    '''

def p_expression_12(p): #fazer metodo number_literal # fazer metodo boolean
    '''
        expression_12 : ID 
                    | STRING_LITERAL 
                    | NUMBER  
                    | BOOL
                    | ID OPEN_PARENTHESES normalFormalParameter CLOSE_PARENTHESES 
    '''

parser = yacc.yacc()

parser.parse()