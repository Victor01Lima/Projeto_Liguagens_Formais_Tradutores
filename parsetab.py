
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND AS ASSERT ASYNC AWAIT BOOL BREAK CASE CATCH CLASS CLOSE_KEYS CLOSE_PARENTHESES COMMA CONST CONTINUE COVARIANT DEFAULT DEFERRED DIFFERENT DIVIDE DIVIDEINT DIVIDE_EQUAL DO DOUBLE DYNAMIC ELSE ENUM EQUAL EQUAL_EQUAL EXPORT EXPRESS EXTENDS EXTENSION EXTERNAL FACTORY FALSE FINAL FINALLY FLOAT FOR FUNCTION GET GREATER_THAN GREATER_THAN_OR_EQUAL_TO HIDE IF IMPLEMENTS IMPORT IN INT INTERFACE INVERT IS LESS_THAN LESS_THAN_OR_EQUAL_TO LIBRARY LIST LOGIC_AND LOGIC_OR MAP MINUS MINUS_EQUAL MINUS_MINUS MIXIN MULT MULTIPLICATION_DIVISION NEW NULL NUM ON OPEN_KEYS OPEN_PARENTHESES OPERATOR OR PART PERCENTAGE PLUS PLUS_EQUAL PLUS_PLUS POINT_COMMA POINT_V RETHROW RETURN SET SHIFT_LEFT SHIFT_RIGHT SHOW STATIC STRING STRING_LITERAL SUPER SWITCH SYNC THIS THROW TRUE TRY TYPEDEF UNARY_BITWASE_COMPLEMENT VAR VOID WHILE WITH XOR YIELDtopLevelDeclaration : PLUS topLevelDeclaration : IF'
    
_lr_action_items = {'PLUS':([0,],[2,]),'IF':([0,],[3,]),'$end':([1,2,3,],[0,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'topLevelDeclaration':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> topLevelDeclaration","S'",1,None,None,None),
  ('topLevelDeclaration -> PLUS','topLevelDeclaration',1,'p_topLevelDeclaration_functionSignature','analisador_sintatico_copy.py',9),
  ('topLevelDeclaration -> IF','topLevelDeclaration',1,'p_topLevelDeclaration_type_initializedIdentifierList_POINT_V','analisador_sintatico_copy.py',12),
]