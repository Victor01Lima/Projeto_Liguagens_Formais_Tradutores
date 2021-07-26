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
   ''' initializedIdentifierList : ID EQUAL expression '(' ID EQUAL expression '''

### Metodo FunctionSignature ###
def p_functionSignature (p): #duvida aqui
    ''' functionSignature : type ?  ID formalParameterPart'''

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
    '''formalParameterList : OPEN_PARENTHESES normalFormalParameters ','?  CLOSE_PARENTHESES  '''

### Metodo normalFormalParameters ###
def p_normalFormalParameters(p): ###DUVIDA
    '''normalFormalParameters :normalFormalParameter OPEN_PARENTHESES COMMA normalFormalParameter CLOSE_PARENTHESES  '''

### Metodo normalFormalParameter ###
def p_normalFormalParameter(p):
    '''normalFormalParameter : type ID '''

### Metodo body ###
def p_body_statements(p):
    '''body : OPEN_KEYS statements CLOSE_KEYS'''

def p_body__(p):
    '''body :  OPEN_KEYS CLOSE_KEYS'''

### Metodo statements ###
def p_statements_statements_statement(p):
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
    '''localVariableDeclaration : type ID (EQUAL expression)? ( COMMA ID ( EQUAL expression)?)* POINT_COMMA'''

### Metodo forStatement ###
def p_forStatement_statement(p):
    '''forStatement : FOR OPEN_PARENTHESES  forLoopParts CLOSE_PARENTHESES statement'''

def p_forStatement_body(p):
    '''forStatement : FOR OPEN_PARENTHESES forLoopParts CLOSE_PARENTHESES body '''

### metodo forLoopParts ###
def p_forLoopParts_localVariableDeclaration(p):
    '''forLoopparts : localVariableDeclaration POINT_COMMA expression? POINT_COMMA expressionList? '''

def p_forLoopParts_expression(p):
    '''forLoopparts : expression POINT_COMMA expression? POINT_COMMA expressionList? '''

def p_forLoopParts_type(p):
    '''forLoopParts ; type? ID IN expression'''

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
    '''ifStatement : IF OPEN_PARENTHESES expression CLOSE_PARENTHESES statement ELSE statement? '''

def p_ifStatement_body_else_body(p):
    '''ifStatement : IF OPEN_PARENTHESES expression CLOSE_PARENTHESES body ELSE body? '''

def p_ifStatement_statement_else_body(p):
    ''' ifStatement : IF OPEN_PARENTHESES expression CLOSE_PARENTHESES body ELSE statement ?'''

### Metodo breakStatement ###
def p_breakStatement(p):
    '''breakStatement : BREAK POINT_COMMA '''

### Metodo continueStatement ###
def p_continueStatement(p):
    ''' continueStatement : CONTINUE POINT_COMMA '''

### Metodo returnStatement ###
def p_returnStatement(p):
    ''' RETURN expression? POINT_COMMA '''

### Metodo expressionStatement ###
def p_expressionStatement(p):
    '''returnStatement : expressionStatement : expression? POINT_COMMA '''

### Metodo expression ###
def p_expression_expression_operator_expression(p):
    ''' expression : expression operator expression'''

def p_expression_unaryop_expression(p):
    ''' expression : unaryop expression '''

def p_expression_expression_plus_plus(p):
    ''' expression : expression PLUS_PLUS '''

def p_expression_expression_minus_minus(p):
    '''expression : expression MINUS_MINUS '''

def p_expression_call(p): ##duvida
    ''' expression : call '''

def p_expression_literal(p):
    '''expression : literal '''

def p_expression_primary(p):
    '''expression : primary '''

### metodo operator ###

def p_operator_equal(p):
    ''' operator : EQUAL'''
def p_operator_multiplication_division(p):
    ''' operator : MULTIPLICATION_DIVISION'''
def p_operator_division_equal(p):
    ''' operator : DIVIDE_EQUAL'''
def p_operator_plus_equal(p):
    '''operator : PLUS_EQUAL'''
def p_operator_minus_equal(p):
    '''operator : MINUS_EQUAL '''
def p_operator_or (p):
    ''' operator : OR'''
def p_operator_and(p):
    ''' operator : AND '''
def p_operator_equal_equal(p):
    '''operator : EQUAL_EQUAL '''

def p_operator_diferent(p):
    '''operator :  DIFFERENT'''
def p_operator_less_than(p):
    ''' operator : LESS_THAN '''
def p_operator_greater_than(p):
    '''operator : GREATER_THAN '''
def p_operator_greater_than_or_equal_to(p):
    ''' operator : GREATER_THAN_OR_EQUAL_TO '''
def p_operator_less_than_or_equal_to(p):
    ''' operator : LESS_THAN_OR_EQUAL_TO'''
def p_operator_logic_or(p):
    '''operator : LOGIC_OR '''
def p_operator_logic_and(p):
    '''operator : LOGIC_AND'''
def p_operator_shift_left(p):
    '''operator : SHIFT_LEFT'''
def p_operator_shift_right(p):
    '''operator : SHIFT_RIGHT'''
def p_operator_plus(p):
    ''' operator : PLUS'''
def p_operator_minus(p):
    ''' operator : MINUS'''
def p_operator_mult(p):
    '''operator : MULT'''
def p_operator_divide(p):
    ''' operator : DIVIDE'''
def p_operator_percentage(p):
    '''operator : PERCENTAGE'''

### metodo primary ###
def p_primary_call(p):
    ''' primary : call '''

def p_primary_literal(p):
    ''' primary : literal '''
def p_primary_ID(p):
    ''' primary : ID '''
def p_primary_expression(p):
    ''' primary :   OPEN_PARENTHESES expression CLOSE_PARENTHESES '''


### metodo literal ### Duvida++
def p_literal_booleanLiteral(p):
    ''' literal : booleanLiteral '''

def p_literal_numericLiteral(p):
    '''  literal : numericLiteral '''

def p_literal_stringLiteral(p):
    ''' literal : stringLiteral '''
parser = yacc.yacc()


parser.parse()