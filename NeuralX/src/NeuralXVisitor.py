# Generated from grammar/NeuralX.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NeuralXParser import NeuralXParser
else:
    from NeuralXParser import NeuralXParser

# This class defines a complete generic visitor for a parse tree produced by NeuralXParser.

class NeuralXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NeuralXParser#prog.
    def visitProg(self, ctx:NeuralXParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#instruccion.
    def visitInstruccion(self, ctx:NeuralXParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#declaracionVar.
    def visitDeclaracionVar(self, ctx:NeuralXParser.DeclaracionVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#declaracionFuncion.
    def visitDeclaracionFuncion(self, ctx:NeuralXParser.DeclaracionFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#parametros.
    def visitParametros(self, ctx:NeuralXParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:NeuralXParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#argumentos.
    def visitArgumentos(self, ctx:NeuralXParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#retorno.
    def visitRetorno(self, ctx:NeuralXParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#EliminarExpr.
    def visitEliminarExpr(self, ctx:NeuralXParser.EliminarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ColumnasCSVExpr.
    def visitColumnasCSVExpr(self, ctx:NeuralXParser.ColumnasCSVExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Numero.
    def visitNumero(self, ctx:NeuralXParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#LeerTodoExpr.
    def visitLeerTodoExpr(self, ctx:NeuralXParser.LeerTodoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#HistoriaExpr.
    def visitHistoriaExpr(self, ctx:NeuralXParser.HistoriaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ArcCoseno.
    def visitArcCoseno(self, ctx:NeuralXParser.ArcCosenoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#EvaluarMod.
    def visitEvaluarMod(self, ctx:NeuralXParser.EvaluarModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Falso.
    def visitFalso(self, ctx:NeuralXParser.FalsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CerosExpr.
    def visitCerosExpr(self, ctx:NeuralXParser.CerosExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#DetExpr.
    def visitDetExpr(self, ctx:NeuralXParser.DetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CentroidesExpr.
    def visitCentroidesExpr(self, ctx:NeuralXParser.CentroidesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Negacion.
    def visitNegacion(self, ctx:NeuralXParser.NegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Piso.
    def visitPiso(self, ctx:NeuralXParser.PisoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearMLP.
    def visitCrearMLP(self, ctx:NeuralXParser.CrearMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#InterceptoExpr.
    def visitInterceptoExpr(self, ctx:NeuralXParser.InterceptoExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Seno.
    def visitSeno(self, ctx:NeuralXParser.SenoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#RaizCuad.
    def visitRaizCuad(self, ctx:NeuralXParser.RaizCuadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#PredecirExpr.
    def visitPredecirExpr(self, ctx:NeuralXParser.PredecirExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CadenaExpr.
    def visitCadenaExpr(self, ctx:NeuralXParser.CadenaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearDBSCAN.
    def visitCrearDBSCAN(self, ctx:NeuralXParser.CrearDBSCANContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#AjustarExpr.
    def visitAjustarExpr(self, ctx:NeuralXParser.AjustarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#IdentidadExpr.
    def visitIdentidadExpr(self, ctx:NeuralXParser.IdentidadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#PrecisionExpr.
    def visitPrecisionExpr(self, ctx:NeuralXParser.PrecisionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#EtiquetasExpr.
    def visitEtiquetasExpr(self, ctx:NeuralXParser.EtiquetasExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#InvertirListaExpr.
    def visitInvertirListaExpr(self, ctx:NeuralXParser.InvertirListaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ErrorModExpr.
    def visitErrorModExpr(self, ctx:NeuralXParser.ErrorModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearKMeans.
    def visitCrearKMeans(self, ctx:NeuralXParser.CrearKMeansContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#AgregarExpr.
    def visitAgregarExpr(self, ctx:NeuralXParser.AgregarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearRNAClas.
    def visitCrearRNAClas(self, ctx:NeuralXParser.CrearRNAClasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#LineasExpr.
    def visitLineasExpr(self, ctx:NeuralXParser.LineasExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ClasificarExpr.
    def visitClasificarExpr(self, ctx:NeuralXParser.ClasificarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#EntrenarMod.
    def visitEntrenarMod(self, ctx:NeuralXParser.EntrenarModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Suma.
    def visitSuma(self, ctx:NeuralXParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ObtenerExpr.
    def visitObtenerExpr(self, ctx:NeuralXParser.ObtenerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Techo.
    def visitTecho(self, ctx:NeuralXParser.TechoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Coseno.
    def visitCoseno(self, ctx:NeuralXParser.CosenoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ValorAbsoluto.
    def visitValorAbsoluto(self, ctx:NeuralXParser.ValorAbsolutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#PredecirMod.
    def visitPredecirMod(self, ctx:NeuralXParser.PredecirModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CoeficientesExpr.
    def visitCoeficientesExpr(self, ctx:NeuralXParser.CoeficientesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Verdadero.
    def visitVerdadero(self, ctx:NeuralXParser.VerdaderoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#TransponerExpr.
    def visitTransponerExpr(self, ctx:NeuralXParser.TransponerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Potencia.
    def visitPotencia(self, ctx:NeuralXParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#PerdidaExpr.
    def visitPerdidaExpr(self, ctx:NeuralXParser.PerdidaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#InvertirExpr.
    def visitInvertirExpr(self, ctx:NeuralXParser.InvertirExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ModuloOp.
    def visitModuloOp(self, ctx:NeuralXParser.ModuloOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Variable.
    def visitVariable(self, ctx:NeuralXParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#OrdenarExpr.
    def visitOrdenarExpr(self, ctx:NeuralXParser.OrdenarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearRegLog.
    def visitCrearRegLog(self, ctx:NeuralXParser.CrearRegLogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#FormaExpr.
    def visitFormaExpr(self, ctx:NeuralXParser.FormaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ExisteExpr.
    def visitExisteExpr(self, ctx:NeuralXParser.ExisteExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#LeerLineaExpr.
    def visitLeerLineaExpr(self, ctx:NeuralXParser.LeerLineaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearRegLineal.
    def visitCrearRegLineal(self, ctx:NeuralXParser.CrearRegLinealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Multiplicacion.
    def visitMultiplicacion(self, ctx:NeuralXParser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Tangente.
    def visitTangente(self, ctx:NeuralXParser.TangenteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#LeerCSVExpr.
    def visitLeerCSVExpr(self, ctx:NeuralXParser.LeerCSVExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#AgregarCapa.
    def visitAgregarCapa(self, ctx:NeuralXParser.AgregarCapaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#EscribirCSVExpr.
    def visitEscribirCSVExpr(self, ctx:NeuralXParser.EscribirCSVExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Redondear.
    def visitRedondear(self, ctx:NeuralXParser.RedondearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Division.
    def visitDivision(self, ctx:NeuralXParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#IndiceExpr.
    def visitIndiceExpr(self, ctx:NeuralXParser.IndiceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#LongitudExpr.
    def visitLongitudExpr(self, ctx:NeuralXParser.LongitudExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Resta.
    def visitResta(self, ctx:NeuralXParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#NormaExpr.
    def visitNormaExpr(self, ctx:NeuralXParser.NormaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Logaritmo10.
    def visitLogaritmo10(self, ctx:NeuralXParser.Logaritmo10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#MatrizExpr.
    def visitMatrizExpr(self, ctx:NeuralXParser.MatrizExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Parentesis.
    def visitParentesis(self, ctx:NeuralXParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#InerciaExpr.
    def visitInerciaExpr(self, ctx:NeuralXParser.InerciaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearArreglo.
    def visitCrearArreglo(self, ctx:NeuralXParser.CrearArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearRNAPred.
    def visitCrearRNAPred(self, ctx:NeuralXParser.CrearRNAPredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#LlamadaExpr.
    def visitLlamadaExpr(self, ctx:NeuralXParser.LlamadaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#Logaritmo.
    def visitLogaritmo(self, ctx:NeuralXParser.LogaritmoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CompilarMLP.
    def visitCompilarMLP(self, ctx:NeuralXParser.CompilarMLPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ArcSeno.
    def visitArcSeno(self, ctx:NeuralXParser.ArcSenoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CrearLista.
    def visitCrearLista(self, ctx:NeuralXParser.CrearListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ContieneExpr.
    def visitContieneExpr(self, ctx:NeuralXParser.ContieneExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ArcTangente.
    def visitArcTangente(self, ctx:NeuralXParser.ArcTangenteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#FilaCSVExpr.
    def visitFilaCSVExpr(self, ctx:NeuralXParser.FilaCSVExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ListaExpr.
    def visitListaExpr(self, ctx:NeuralXParser.ListaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#lista.
    def visitLista(self, ctx:NeuralXParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#declaracionMatriz.
    def visitDeclaracionMatriz(self, ctx:NeuralXParser.DeclaracionMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#listaNumeros.
    def visitListaNumeros(self, ctx:NeuralXParser.ListaNumerosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#condicional.
    def visitCondicional(self, ctx:NeuralXParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondIgual.
    def visitCondIgual(self, ctx:NeuralXParser.CondIgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondY.
    def visitCondY(self, ctx:NeuralXParser.CondYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondMayorIgual.
    def visitCondMayorIgual(self, ctx:NeuralXParser.CondMayorIgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondNo.
    def visitCondNo(self, ctx:NeuralXParser.CondNoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondO.
    def visitCondO(self, ctx:NeuralXParser.CondOContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondMenorIgual.
    def visitCondMenorIgual(self, ctx:NeuralXParser.CondMenorIgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondDiferente.
    def visitCondDiferente(self, ctx:NeuralXParser.CondDiferenteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondMenor.
    def visitCondMenor(self, ctx:NeuralXParser.CondMenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#CondMayor.
    def visitCondMayor(self, ctx:NeuralXParser.CondMayorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ForRango.
    def visitForRango(self, ctx:NeuralXParser.ForRangoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#ForLista.
    def visitForLista(self, ctx:NeuralXParser.ForListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#cicloWhile.
    def visitCicloWhile(self, ctx:NeuralXParser.CicloWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#instruccionML.
    def visitInstruccionML(self, ctx:NeuralXParser.InstruccionMLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#instruccionMatrix.
    def visitInstruccionMatrix(self, ctx:NeuralXParser.InstruccionMatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#instruccionPlot.
    def visitInstruccionPlot(self, ctx:NeuralXParser.InstruccionPlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#instruccionRed.
    def visitInstruccionRed(self, ctx:NeuralXParser.InstruccionRedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuralXParser#instruccionIO.
    def visitInstruccionIO(self, ctx:NeuralXParser.InstruccionIOContext):
        return self.visitChildren(ctx)



del NeuralXParser