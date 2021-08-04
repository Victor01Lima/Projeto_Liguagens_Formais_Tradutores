from abc import abstractmethod
from abc import ABCMeta


class AbstractVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visitTopLevelDeclFuncSignConcrete(self, topLevelDeclaration):
        pass

    @abstractmethod
    def visitTopLevelDeclTypeInitIdentifierListPointVConcrete(self, topLevelDeclaration):
        pass
    
    @abstractmethod
    def visitTopLevelDeclFunctSignBodyTopLevelDeclConcrete(self, topLevelDeclaration):
        pass

    @abstractmethod
    def visitTopLevelDeclTypeInitIdentifierListPointvTopLevelDeclConcrete(self, topLevelDeclaration):
        pass

    @abstractmethod
    def visitInitializedIdentifierListConcrete(self, initializedIdentifierList):
        pass

    @abstractmethod
    def visitInitializedIdentifierListEstrelaConcrete(self, p_initializedIdentifierList_estrela):
        pass

    @abstractmethod
    def visitInitializedIdentifierListEstrelaCompoundConcrete(self, p_initializedIdentifierList_estrela):
        pass

    @abstractmethod
    def visitTypeVoid(self, type):
        pass

    @abstractmethod
    def visitTypeString(self, type):
        pass

    @abstractmethod
    def visitTypeBool(self, type):
        pass

    @abstractmethod
    def visitTypeInt(self, type):
        pass

    @abstractmethod
    def visitTypeFloat(self, type):
        pass

    @abstractmethod
    def visitTypeVar(self, type):
        pass


    