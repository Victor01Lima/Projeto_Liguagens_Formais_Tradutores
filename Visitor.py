
from AbstractVisitor import AbstractVisitor

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):
    
    def visitTopLevelDeclFuncSignConcrete(self, topLevelDeclFuncSignConcrete):
        topLevelDeclFuncSignConcrete.functionSignature.accept(self)
        topLevelDeclFuncSignConcrete.body.accept(self)
    
    def visitTopLevelDeclTypeInitIdentifierListPointVConcrete(self, topLevelDeclTypeInitIdentifierListPointVConcrete):
        
        topLevelDeclTypeInitIdentifierListPointVConcrete.type.accept(self)
        topLevelDeclTypeInitIdentifierListPointVConcrete.initializedIdentifierList.accept(self)
        print(';', end='')

    def visitTopLevelDeclFunctSignBodyTopLevelDeclConcrete(self, topLevelDeclFunctSignBodyTopLevelDeclConcrete):
        topLevelDeclFunctSignBodyTopLevelDeclConcrete.functionSignature.accept(self)
        topLevelDeclFunctSignBodyTopLevelDeclConcrete.body.accept(self)
        topLevelDeclFunctSignBodyTopLevelDeclConcrete.topLevelDeclaration.accept(self)

    def visitTopLevelDeclTypeInitIdentifierListPointvTopLevelDecl(self, topLevelDeclTypeInitIdentifierListPointvTopLevelDecl):
        topLevelDeclTypeInitIdentifierListPointvTopLevelDecl.type.accept(self)
        topLevelDeclTypeInitIdentifierListPointvTopLevelDecl.initializedIdentifierList.accept(self)
        print(';', end='')
        topLevelDeclTypeInitIdentifierListPointvTopLevelDecl.topLevelDeclaration.accept(self)

    def visitInitializedIdentifierListEstrelaConcrete(self, initializedIdentifierListEstrelaConcrete):
        initializedIdentifierListEstrelaConcrete.type.accept(self)
        initializedIdentifierListEstrelaConcrete.expression.accept(self)

    def visitInitializedIdentifierListEstrelaCompoundConcrete(self, initializedIdentifierListEstrelaCompoundConcrete):
        initializedIdentifierListEstrelaCompoundConcrete.type.accept(self)
        initializedIdentifierListEstrelaCompoundConcrete.expression.accept(self)
        initializedIdentifierListEstrelaCompoundConcrete.p_initializedIdentifierList_estrela.accept(self)

    def visitFunctionSignatureConcrete(self, visitFunctionSignatureConcrete):
        visitFunctionSignatureConcrete.type.accept(self)
        visitFunctionSignatureConcrete.id.accept(self)
        visitFunctionSignatureConcrete.formalParameterList.accept(self)


    def visitFunctionSignature2Concrete(self, functionSignature2Concrete):
        functionSignature2Concrete.id.accept(self)
        functionSignature2Concrete.formalParameterList.accept(self)
      