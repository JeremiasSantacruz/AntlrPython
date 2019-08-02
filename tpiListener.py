# Generated from tpi.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tpiParser import tpiParser
else:
    from tpiParser import tpiParser

# This class defines a complete listener for a parse tree produced by tpiParser.
class tpiListener(ParseTreeListener):

    # Enter a parse tree produced by tpiParser#start.
    def enterStart(self, ctx:tpiParser.StartContext):
        global noVar
        global var 
        var = []
        noVar = []
        pass

    # Exit a parse tree produced by tpiParser#start.
    def exitStart(self, ctx:tpiParser.StartContext):
        pass


    # Enter a parse tree produced by tpiParser#programa.
    def enterPrograma(self, ctx:tpiParser.ProgramaContext):
        pass

    # Exit a parse tree produced by tpiParser#programa.
    def exitPrograma(self, ctx:tpiParser.ProgramaContext):
        print ("="*60)
        print ("Variables usadas: ", end=' ')
        for i in var:
            print (i +", ", end=' ')
        print ("\nConstante usadas: ", end=' ')
        for i in noVar:
            print(i+ ", ", end=' ')
        pass


    # Enter a parse tree produced by tpiParser#ambiente.
    def enterAmbiente(self, ctx:tpiParser.AmbienteContext):
        pass

    # Exit a parse tree produced by tpiParser#ambiente.
    def exitAmbiente(self, ctx:tpiParser.AmbienteContext):
        pass


    # Enter a parse tree produced by tpiParser#lineaambiente.
    def enterLineaambiente(self, ctx:tpiParser.LineaambienteContext):
        pass

    # Exit a parse tree produced by tpiParser#lineaambiente.
    def exitLineaambiente(self, ctx:tpiParser.LineaambienteContext):
        pass


    # Enter a parse tree produced by tpiParser#variable.
    def enterVariable(self, ctx:tpiParser.VariableContext):
        var.append(ctx.IDENTIFICADOR().getText())
        pass

    # Exit a parse tree produced by tpiParser#variable.
    def exitVariable(self, ctx:tpiParser.VariableContext):
        pass


    # Enter a parse tree produced by tpiParser#constante.
    def enterConstante(self, ctx:tpiParser.ConstanteContext):
        noVar.append(ctx.IDENTIFICADOR().getText())
        pass

    # Exit a parse tree produced by tpiParser#constante.
    def exitConstante(self, ctx:tpiParser.ConstanteContext):
        pass


    # Enter a parse tree produced by tpiParser#proceso.
    def enterProceso(self, ctx:tpiParser.ProcesoContext):
        pass

    # Exit a parse tree produced by tpiParser#proceso.
    def exitProceso(self, ctx:tpiParser.ProcesoContext):
        pass


    # Enter a parse tree produced by tpiParser#lineacod.
    def enterLineacod(self, ctx:tpiParser.LineacodContext):
        pass

    # Exit a parse tree produced by tpiParser#lineacod.
    def exitLineacod(self, ctx:tpiParser.LineacodContext):
        pass


    # Enter a parse tree produced by tpiParser#asignacion.
    def enterAsignacion(self, ctx:tpiParser.AsignacionContext):
        if ctx.IDENTIFICADOR().getText() not in var :
            if ctx.IDENTIFICADOR().getText() in noVar:
                print ("%s es una constante. <%s, %s>" %(ctx.IDENTIFICADOR().getText(), ctx.start.line, ctx.start.column)) 
            else: 
                print("%s no declarada. <%s, %s>" %(ctx.IDENTIFICADOR().getText(), ctx.start.line, ctx.start.column))
        pass

    # Exit a parse tree produced by tpiParser#asignacion.
    def exitAsignacion(self, ctx:tpiParser.AsignacionContext):
        pass


    # Enter a parse tree produced by tpiParser#asignacioninc.
    def enterAsignacioninc(self, ctx:tpiParser.AsignacionincContext):
        pass

    # Exit a parse tree produced by tpiParser#asignacioninc.
    def exitAsignacioninc(self, ctx:tpiParser.AsignacionincContext):
        pass


    # Enter a parse tree produced by tpiParser#sentencias.
    def enterSentencias(self, ctx:tpiParser.SentenciasContext):
        pass

    # Exit a parse tree produced by tpiParser#sentencias.
    def exitSentencias(self, ctx:tpiParser.SentenciasContext):
        pass


    # Enter a parse tree produced by tpiParser#condicional.
    def enterCondicional(self, ctx:tpiParser.CondicionalContext):
        pass

    # Exit a parse tree produced by tpiParser#condicional.
    def exitCondicional(self, ctx:tpiParser.CondicionalContext):
        pass


    # Enter a parse tree produced by tpiParser#iterativas.
    def enterIterativas(self, ctx:tpiParser.IterativasContext):
        pass

    # Exit a parse tree produced by tpiParser#iterativas.
    def exitIterativas(self, ctx:tpiParser.IterativasContext):
        pass


    # Enter a parse tree produced by tpiParser#lineasegun.
    def enterLineasegun(self, ctx:tpiParser.LineasegunContext):
        pass

    # Exit a parse tree produced by tpiParser#lineasegun.
    def exitLineasegun(self, ctx:tpiParser.LineasegunContext):
        pass


    # Enter a parse tree produced by tpiParser#funcion.
    def enterFuncion(self, ctx:tpiParser.FuncionContext):
        pass

    # Exit a parse tree produced by tpiParser#funcion.
    def exitFuncion(self, ctx:tpiParser.FuncionContext):
        pass


    # Enter a parse tree produced by tpiParser#arg.
    def enterArg(self, ctx:tpiParser.ArgContext):
        pass

    # Exit a parse tree produced by tpiParser#arg.
    def exitArg(self, ctx:tpiParser.ArgContext):
        pass


    # Enter a parse tree produced by tpiParser#expresion.
    def enterExpresion(self, ctx:tpiParser.ExpresionContext):
        pass

    # Exit a parse tree produced by tpiParser#expresion.
    def exitExpresion(self, ctx:tpiParser.ExpresionContext):
        pass


    # Enter a parse tree produced by tpiParser#siexpresion.
    def enterSiexpresion(self, ctx:tpiParser.SiexpresionContext):
        pass

    # Exit a parse tree produced by tpiParser#siexpresion.
    def exitSiexpresion(self, ctx:tpiParser.SiexpresionContext):
        pass


    # Enter a parse tree produced by tpiParser#factor.
    def enterFactor(self, ctx:tpiParser.FactorContext):
        pass

    # Exit a parse tree produced by tpiParser#factor.
    def exitFactor(self, ctx:tpiParser.FactorContext):
        pass


    # Enter a parse tree produced by tpiParser#termino.
    def enterTermino(self, ctx:tpiParser.TerminoContext):
        pass

    # Exit a parse tree produced by tpiParser#termino.
    def exitTermino(self, ctx:tpiParser.TerminoContext):
        pass


    # Enter a parse tree produced by tpiParser#hoja.
    def enterHoja(self, ctx:tpiParser.HojaContext):
        pass

    # Exit a parse tree produced by tpiParser#hoja.
    def exitHoja(self, ctx:tpiParser.HojaContext):
        pass


    # Enter a parse tree produced by tpiParser#dato.
    def enterDato(self, ctx:tpiParser.DatoContext):
        pass

    # Exit a parse tree produced by tpiParser#dato.
    def exitDato(self, ctx:tpiParser.DatoContext):
        pass


    # Enter a parse tree produced by tpiParser#operadorrelacional.
    def enterOperadorrelacional(self, ctx:tpiParser.OperadorrelacionalContext):
        pass

    # Exit a parse tree produced by tpiParser#operadorrelacional.
    def exitOperadorrelacional(self, ctx:tpiParser.OperadorrelacionalContext):
        pass


    # Enter a parse tree produced by tpiParser#addoperador.
    def enterAddoperador(self, ctx:tpiParser.AddoperadorContext):
        pass

    # Exit a parse tree produced by tpiParser#addoperador.
    def exitAddoperador(self, ctx:tpiParser.AddoperadorContext):
        pass


    # Enter a parse tree produced by tpiParser#multioperador.
    def enterMultioperador(self, ctx:tpiParser.MultioperadorContext):
        pass

    # Exit a parse tree produced by tpiParser#multioperador.
    def exitMultioperador(self, ctx:tpiParser.MultioperadorContext):
        pass


    # Enter a parse tree produced by tpiParser#numero.
    def enterNumero(self, ctx:tpiParser.NumeroContext):
        pass

    # Exit a parse tree produced by tpiParser#numero.
    def exitNumero(self, ctx:tpiParser.NumeroContext):
        pass


