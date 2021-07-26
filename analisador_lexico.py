# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/

# Author Victor da Luz Lima, Jose Nathanel e Davi de jesus
import ply.lex as lex

# List of token names.   This is always required
tokens = (

    #PALAVRAS RESERVADAS
    'ABSTRACT',
    'AS',
    'ASSERT',
    'ASYNC',
    'AWAIT',
    'BREAK',
    'BOOL',
    'CASE',
    'CATCH',
    'CLASS',
    'CONST',
    'CONTINUE',
    'COVARIANT',
    'DEFAULT',
    'DEFERRED',
    'DO',
    'DOUBLE',
    'DYNAMIC',
    'ELSE',
    'ENUM',
    'EXPORT',
    'EXTENDS',
    'EXTENSION',
    'EXTERNAL',
    'FACTORY',
    'FALSE',
    'FINAL',
    'FLOAT',
    'FINALLY',
    'FOR',
    'FUNCTION',
    'GET',
    'HIDE',
    'IF',
    'IMPLEMENTS',
    'IMPORT',
    'IN',
    'INT',
    'INTERFACE',
    'IS',
    'LIBRARY',
    'LIST',
    'MAP',
    'MIXIN',
    'NEW',
    'NULL',
    'NUM',
    'ON',
    'OPERATOR',
    'PART',
    'RETHROW',
    'RETURN',
    'SET',
    'SHOW',
    'STATIC',
    'STRING',
    'SUPER',
    'SWITCH',
    'SYNC',
    'THIS',
    'THROW',
    'TRUE',
    'TRY',
    'TYPEDEF',
    'VAR',
    'VOID',
    'WHILE',
    'WITH',
    'YIELD',
    'POINT_V',

    #OPERADORES ARITIMETICOS
    'MULTIPLICATION_DIVISION',
    'PLUS_PLUS',
    'PLUS',
    'MINUS',
    'MINUS_MINUS',
    'EXPRESS',
    'MULT',
    'MINUS_EQUAL',
    'DIVIDE',
    'DIVIDE_EQUAL',
    'DIVIDEINT',
    'PERCENTAGE',
    'PLUS_EQUAL',

    # OPERADORES LOGICOS
    'INVERT',
    'LOGIC_AND',
    'LOGIC_OR',
    #OUTROS
    'POINT_COMMA',
    'COMMA',
    'OPEN_PARENTHESES',
    'CLOSE_PARENTHESES',
    'OPEN_KEYS',
    'CLOSE_KEYS',
    # OPERADORES RELACIONAIS
    'EQUAL',
    'EQUAL_EQUAL',
    'DIFFERENT',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_THAN_OR_EQUAL_TO',
    'LESS_THAN_OR_EQUAL_TO',

    #BIT TO BIT
    'AND',
    'OR',
    'XOR',
    'UNARY_BITWASE_COMPLEMENT',
    'SHIFT_LEFT',
    'SHIFT_RIGHT',
)

# Regular expression rules for simple tokens

#PALAVRAS RESERVADAS

t_ABSTRACT = r'abstract'
t_AS = r'as'
t_ASSERT = r'assert'
t_ASYNC = r'async'
t_AWAIT = r'await'
t_BREAK = r'break'
t_BOOL = r'bool'
t_CASE = r'case'
t_CATCH = r'catch'
t_CLASS = r'class'
t_CONST = r'const'
t_CONTINUE = r'continue'
t_COVARIANT = r'covariant'
t_DEFAULT = r'default'
t_DEFERRED = r'deferred'
t_DO = r'do'
t_DOUBLE = r'double'
t_DYNAMIC = r'dynamic'
t_ELSE = r'else'
t_ENUM = r'enum'
t_EXPORT = r'export'
t_EXTENDS = r'extends'
t_EXTENSION = r'extension'
t_EXTERNAL = r'external'
t_FACTORY = r'factory'
t_FLOAT = r'float'
t_FALSE = r'false'
t_FINAL = r'final'
t_FINALLY = r'finally'
t_FOR = r'for'
t_FUNCTION = r'function'
t_GET = r'get'
t_HIDE = r'hide'
t_IF = r'if'
t_INT= r'int'
t_IMPLEMENTS = r'implements'
t_IMPORT = r'import'
t_IN = r'in'
t_INTERFACE = r'interface'
t_IS = r'is'
t_LIBRARY = r'library'
t_LIST = r'List'
t_MIXIN = r'mixin'
t_MAP = r'Map'
t_NEW = r'new'
t_NULL = r'null'
t_NUM = r'num'
t_ON = r'on'
t_OPERATOR = r'operator'
t_PART = r'part'
t_POINT_V =r';'
t_RETHROW = r'rethrow'
t_RETURN = r'return'
t_SET = r'set'
t_SHOW = r'show'
t_STATIC = r'static'
t_STRING = r'String'
t_SUPER = r'super'
t_SWITCH = r'switch'
t_SYNC = r'sync'
t_THIS = r'this'
t_THROW = r'throw'
t_TRUE = r'true'
t_TRY = r'try'
t_TYPEDEF = r'typedef'
t_VAR = r'var'
t_VOID = r'void'
t_WHILE = r'while'
t_WITH = r'with'
t_YIELD = r'yield'

#OPERADORES ARITMETICOS
t_DIVIDE_EQUAL = r'\/\='
t_MULTIPLICATION_DIVISION = r'\*\='
t_PLUS_PLUS = r'\+\+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MINUS_MINUS = r'\-\-'
t_MINUS_EQUAL = r'\-\='
t_EXPRESS = r'-expr'
t_MULT = r'\*'
t_DIVIDE = r'\/'
t_DIVIDEINT = r'\/'
t_PERCENTAGE = r'\%'
t_PLUS_EQUAL =r'\+\='
###OUTROS
t_POINT_COMMA = r'\;'
t_OPEN_KEYS = r'\{'
t_CLOSE_KEYS = r'\}'
t_COMMA = r'\,'
t_OPEN_PARENTHESES = r'\('
t_OPEN_PARENTHESES = r'\)'
# OPERADORES RELACIONAIS
t_EQUAL= r'\='
t_EQUAL_EQUAL = r'\=\='
t_DIFFERENT = r'\!\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_OR_EQUAL_TO = r'\<\='
t_LESS_THAN_OR_EQUAL_TO = r'\>\='

# OPERADORES LOGICOS
t_INVERT = r'\!'  
t_LOGIC_OR = r'\|'
t_LOGIC_AND = r'\&'

#BIT TO BIT
t_AND = r'\&\&'
t_OR = r'\|\|'
t_XOR = r'\^'
t_UNARY_BITWASE_COMPLEMENT = r'\~'
t_SHIFT_LEFT = r'\<\<'
t_SHIFT_RIGHT = r'\>\>'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
 ||
'''

# Give the lexer some input
lexer.input(data)

#while True:
 #   tok = lexer.token()
  ##     break  # No more input
   # print(tok.type, tok.value, tok.lineno, tok.lexpos)
