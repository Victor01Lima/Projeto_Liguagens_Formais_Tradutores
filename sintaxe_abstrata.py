import ply.lex as lex
from analisador_lexico import *
import ply.yacc as yacc
from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

## topLevelDeclaration ###
class TopLevelDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class TopLevelDeclFuncSignConcrete(TopLevelDeclaration):
    def __init__(self, functionSignature, body):
        self.functionSignature = functionSignature
        self.body = body
    def accept(self, visitor):
        return visitor.visitTopLevelDeclFuncSignConcrete(self)

class TopLevelDeclTypeInitIdentifierListPointVConcrete(TopLevelDeclaration):
    def __init__(self, type, initializedIdentifierList):
        self.type = type
        self.initializedIdentifierList = initializedIdentifierList
    def accept(self, visitor):
        return visitor.visitTopLevelDeclTypeInitIdentifierListPointVConcrete(self)

class TopLevelDeclFunctSignBodyTopLevelDeclConcrete(TopLevelDeclaration):
    def __init__(self, functionSignature, body, topLevelDeclaration):
        self.functionSignature = functionSignature
        self.body = body
        self.topLevelDeclaration = topLevelDeclaration
    def accept(self, visitor):
        return visitor.visitTopLevelDeclFunctSignBodyTopLevelDeclConcrete(self)

class TopLevelDeclTypeInitIdentifierListPointvTopLevelDeclConcrete(TopLevelDeclaration):
    def __init__(self, type, initializedIdentifierList, topLevelDeclaration):
        self.type = type
        self.initializedIdentifierList = initializedIdentifierList
        self.topLevelDeclaration = topLevelDeclaration
    def accept(self, visitor):
        return visitor.visitTopLevelDeclTypeInitIdentifierListPointvTopLevelDeclConcrete(self)


### Metodo initializedIdentifierList ###
class InitializedIdentifierList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class InitializedIdentifierListConcrete(InitializedIdentifierList):
    def __init__(self, type, expression, p_initializedIdentifierList_estrela):
        self.type = type
        self.expression = expression
        self.p_initializedIdentifierList_estrela = p_initializedIdentifierList_estrela
    def accept(self, visitor):
        return visitor.visitInitializedIdentifierListConcrete(self)


class InitializedIdentifierListEstrela(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class InitializedIdentifierListEstrelaSingleConcrete(InitializedIdentifierListEstrela):
    def __init__(self, type, expression):
        self.type = type
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitInitializedIdentifierListEstrelaConcrete(self)


class  InitializedIdentifierListEstrelaCompoundConcrete(InitializedIdentifierListEstrela):
    def __init__(self, type, expression, p_initializedIdentifierList_estrela):
        self.type = type
        self.expression = expression
        self.p_initializedIdentifierList_estrela = p_initializedIdentifierList_estrela
    def accept(self, visitor):
        return visitor.visitInitializedIdentifierListEstrelaCompoundConcrete(self)


### Metodo FunctionSignature ###
class FunctionSignature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FunctionSignatureConcrete(FunctionSignature):
    def __init__(self, type, id, formalParameterList):
        self.type = type
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitFunctionSignatureConcrete(self)

class FunctionSignature2Concrete(FunctionSignature):
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitFunctionSignature2Concrete(self)

### Metodo type ### 
class Type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class TypeVoid():
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitTypeVoid(self)

class TypeString():
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitTypeString(self)

class TypeBool():
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitTypeBool(self)

class TypeInt():
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitTypeInt(self)

class TypeFloat():
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitTypeFloat(self)

class TypeVar():
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitTypeVar(self)