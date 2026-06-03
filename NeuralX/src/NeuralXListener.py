# Generated from grammar/NeuralX.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NeuralXParser import NeuralXParser
else:
    from NeuralXParser import NeuralXParser

# This class defines a complete listener for a parse tree produced by NeuralXParser.
class NeuralXListener(ParseTreeListener):

    # Enter a parse tree produced by NeuralXParser#prog.
    def enterProg(self, ctx:NeuralXParser.ProgContext):
        pass

    # Exit a parse tree produced by NeuralXParser#prog.
    def exitProg(self, ctx:NeuralXParser.ProgContext):
        pass


    # Enter a parse tree produced by NeuralXParser#instruccion.
    def enterInstruccion(self, ctx:NeuralXParser.InstruccionContext):
        pass

    # Exit a parse tree produced by NeuralXParser#instruccion.
    def exitInstruccion(self, ctx:NeuralXParser.InstruccionContext):
        pass


    # Enter a parse tree produced by NeuralXParser#declaracionVar.
    def enterDeclaracionVar(self, ctx:NeuralXParser.DeclaracionVarContext):
        pass

    # Exit a parse tree produced by NeuralXParser#declaracionVar.
    def exitDeclaracionVar(self, ctx:NeuralXParser.DeclaracionVarContext):
        pass


    # Enter a parse tree produced by NeuralXParser#declaracionFuncion.
    def enterDeclaracionFuncion(self, ctx:NeuralXParser.DeclaracionFuncionContext):
        pass

    # Exit a parse tree produced by NeuralXParser#declaracionFuncion.
    def exitDeclaracionFuncion(self, ctx:NeuralXParser.DeclaracionFuncionContext):
        pass


    # Enter a parse tree produced by NeuralXParser#parametros.
    def enterParametros(self, ctx:NeuralXParser.ParametrosContext):
        pass

    # Exit a parse tree produced by NeuralXParser#parametros.
    def exitParametros(self, ctx:NeuralXParser.ParametrosContext):
        pass


    # Enter a parse tree produced by NeuralXParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:NeuralXParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by NeuralXParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:NeuralXParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by NeuralXParser#argumentos.
    def enterArgumentos(self, ctx:NeuralXParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by NeuralXParser#argumentos.
    def exitArgumentos(self, ctx:NeuralXParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by NeuralXParser#retorno.
    def enterRetorno(self, ctx:NeuralXParser.RetornoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#retorno.
    def exitRetorno(self, ctx:NeuralXParser.RetornoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#EliminarExpr.
    def enterEliminarExpr(self, ctx:NeuralXParser.EliminarExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#EliminarExpr.
    def exitEliminarExpr(self, ctx:NeuralXParser.EliminarExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ColumnasCSVExpr.
    def enterColumnasCSVExpr(self, ctx:NeuralXParser.ColumnasCSVExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ColumnasCSVExpr.
    def exitColumnasCSVExpr(self, ctx:NeuralXParser.ColumnasCSVExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Numero.
    def enterNumero(self, ctx:NeuralXParser.NumeroContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Numero.
    def exitNumero(self, ctx:NeuralXParser.NumeroContext):
        pass


    # Enter a parse tree produced by NeuralXParser#LeerTodoExpr.
    def enterLeerTodoExpr(self, ctx:NeuralXParser.LeerTodoExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#LeerTodoExpr.
    def exitLeerTodoExpr(self, ctx:NeuralXParser.LeerTodoExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#HistoriaExpr.
    def enterHistoriaExpr(self, ctx:NeuralXParser.HistoriaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#HistoriaExpr.
    def exitHistoriaExpr(self, ctx:NeuralXParser.HistoriaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ArcCoseno.
    def enterArcCoseno(self, ctx:NeuralXParser.ArcCosenoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ArcCoseno.
    def exitArcCoseno(self, ctx:NeuralXParser.ArcCosenoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#EvaluarMod.
    def enterEvaluarMod(self, ctx:NeuralXParser.EvaluarModContext):
        pass

    # Exit a parse tree produced by NeuralXParser#EvaluarMod.
    def exitEvaluarMod(self, ctx:NeuralXParser.EvaluarModContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Falso.
    def enterFalso(self, ctx:NeuralXParser.FalsoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Falso.
    def exitFalso(self, ctx:NeuralXParser.FalsoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CerosExpr.
    def enterCerosExpr(self, ctx:NeuralXParser.CerosExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CerosExpr.
    def exitCerosExpr(self, ctx:NeuralXParser.CerosExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#DetExpr.
    def enterDetExpr(self, ctx:NeuralXParser.DetExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#DetExpr.
    def exitDetExpr(self, ctx:NeuralXParser.DetExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CentroidesExpr.
    def enterCentroidesExpr(self, ctx:NeuralXParser.CentroidesExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CentroidesExpr.
    def exitCentroidesExpr(self, ctx:NeuralXParser.CentroidesExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Negacion.
    def enterNegacion(self, ctx:NeuralXParser.NegacionContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Negacion.
    def exitNegacion(self, ctx:NeuralXParser.NegacionContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Piso.
    def enterPiso(self, ctx:NeuralXParser.PisoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Piso.
    def exitPiso(self, ctx:NeuralXParser.PisoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearMLP.
    def enterCrearMLP(self, ctx:NeuralXParser.CrearMLPContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearMLP.
    def exitCrearMLP(self, ctx:NeuralXParser.CrearMLPContext):
        pass


    # Enter a parse tree produced by NeuralXParser#InterceptoExpr.
    def enterInterceptoExpr(self, ctx:NeuralXParser.InterceptoExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#InterceptoExpr.
    def exitInterceptoExpr(self, ctx:NeuralXParser.InterceptoExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Seno.
    def enterSeno(self, ctx:NeuralXParser.SenoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Seno.
    def exitSeno(self, ctx:NeuralXParser.SenoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#RaizCuad.
    def enterRaizCuad(self, ctx:NeuralXParser.RaizCuadContext):
        pass

    # Exit a parse tree produced by NeuralXParser#RaizCuad.
    def exitRaizCuad(self, ctx:NeuralXParser.RaizCuadContext):
        pass


    # Enter a parse tree produced by NeuralXParser#PredecirExpr.
    def enterPredecirExpr(self, ctx:NeuralXParser.PredecirExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#PredecirExpr.
    def exitPredecirExpr(self, ctx:NeuralXParser.PredecirExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CadenaExpr.
    def enterCadenaExpr(self, ctx:NeuralXParser.CadenaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CadenaExpr.
    def exitCadenaExpr(self, ctx:NeuralXParser.CadenaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearDBSCAN.
    def enterCrearDBSCAN(self, ctx:NeuralXParser.CrearDBSCANContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearDBSCAN.
    def exitCrearDBSCAN(self, ctx:NeuralXParser.CrearDBSCANContext):
        pass


    # Enter a parse tree produced by NeuralXParser#AjustarExpr.
    def enterAjustarExpr(self, ctx:NeuralXParser.AjustarExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#AjustarExpr.
    def exitAjustarExpr(self, ctx:NeuralXParser.AjustarExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#IdentidadExpr.
    def enterIdentidadExpr(self, ctx:NeuralXParser.IdentidadExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#IdentidadExpr.
    def exitIdentidadExpr(self, ctx:NeuralXParser.IdentidadExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#PrecisionExpr.
    def enterPrecisionExpr(self, ctx:NeuralXParser.PrecisionExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#PrecisionExpr.
    def exitPrecisionExpr(self, ctx:NeuralXParser.PrecisionExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#EtiquetasExpr.
    def enterEtiquetasExpr(self, ctx:NeuralXParser.EtiquetasExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#EtiquetasExpr.
    def exitEtiquetasExpr(self, ctx:NeuralXParser.EtiquetasExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#InvertirListaExpr.
    def enterInvertirListaExpr(self, ctx:NeuralXParser.InvertirListaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#InvertirListaExpr.
    def exitInvertirListaExpr(self, ctx:NeuralXParser.InvertirListaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ErrorModExpr.
    def enterErrorModExpr(self, ctx:NeuralXParser.ErrorModExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ErrorModExpr.
    def exitErrorModExpr(self, ctx:NeuralXParser.ErrorModExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearKMeans.
    def enterCrearKMeans(self, ctx:NeuralXParser.CrearKMeansContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearKMeans.
    def exitCrearKMeans(self, ctx:NeuralXParser.CrearKMeansContext):
        pass


    # Enter a parse tree produced by NeuralXParser#AgregarExpr.
    def enterAgregarExpr(self, ctx:NeuralXParser.AgregarExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#AgregarExpr.
    def exitAgregarExpr(self, ctx:NeuralXParser.AgregarExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearRNAClas.
    def enterCrearRNAClas(self, ctx:NeuralXParser.CrearRNAClasContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearRNAClas.
    def exitCrearRNAClas(self, ctx:NeuralXParser.CrearRNAClasContext):
        pass


    # Enter a parse tree produced by NeuralXParser#LineasExpr.
    def enterLineasExpr(self, ctx:NeuralXParser.LineasExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#LineasExpr.
    def exitLineasExpr(self, ctx:NeuralXParser.LineasExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ClasificarExpr.
    def enterClasificarExpr(self, ctx:NeuralXParser.ClasificarExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ClasificarExpr.
    def exitClasificarExpr(self, ctx:NeuralXParser.ClasificarExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#EntrenarMod.
    def enterEntrenarMod(self, ctx:NeuralXParser.EntrenarModContext):
        pass

    # Exit a parse tree produced by NeuralXParser#EntrenarMod.
    def exitEntrenarMod(self, ctx:NeuralXParser.EntrenarModContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Suma.
    def enterSuma(self, ctx:NeuralXParser.SumaContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Suma.
    def exitSuma(self, ctx:NeuralXParser.SumaContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ObtenerExpr.
    def enterObtenerExpr(self, ctx:NeuralXParser.ObtenerExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ObtenerExpr.
    def exitObtenerExpr(self, ctx:NeuralXParser.ObtenerExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Techo.
    def enterTecho(self, ctx:NeuralXParser.TechoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Techo.
    def exitTecho(self, ctx:NeuralXParser.TechoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Coseno.
    def enterCoseno(self, ctx:NeuralXParser.CosenoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Coseno.
    def exitCoseno(self, ctx:NeuralXParser.CosenoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ValorAbsoluto.
    def enterValorAbsoluto(self, ctx:NeuralXParser.ValorAbsolutoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ValorAbsoluto.
    def exitValorAbsoluto(self, ctx:NeuralXParser.ValorAbsolutoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#PredecirMod.
    def enterPredecirMod(self, ctx:NeuralXParser.PredecirModContext):
        pass

    # Exit a parse tree produced by NeuralXParser#PredecirMod.
    def exitPredecirMod(self, ctx:NeuralXParser.PredecirModContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CoeficientesExpr.
    def enterCoeficientesExpr(self, ctx:NeuralXParser.CoeficientesExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CoeficientesExpr.
    def exitCoeficientesExpr(self, ctx:NeuralXParser.CoeficientesExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Verdadero.
    def enterVerdadero(self, ctx:NeuralXParser.VerdaderoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Verdadero.
    def exitVerdadero(self, ctx:NeuralXParser.VerdaderoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#TransponerExpr.
    def enterTransponerExpr(self, ctx:NeuralXParser.TransponerExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#TransponerExpr.
    def exitTransponerExpr(self, ctx:NeuralXParser.TransponerExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Potencia.
    def enterPotencia(self, ctx:NeuralXParser.PotenciaContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Potencia.
    def exitPotencia(self, ctx:NeuralXParser.PotenciaContext):
        pass


    # Enter a parse tree produced by NeuralXParser#PerdidaExpr.
    def enterPerdidaExpr(self, ctx:NeuralXParser.PerdidaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#PerdidaExpr.
    def exitPerdidaExpr(self, ctx:NeuralXParser.PerdidaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#InvertirExpr.
    def enterInvertirExpr(self, ctx:NeuralXParser.InvertirExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#InvertirExpr.
    def exitInvertirExpr(self, ctx:NeuralXParser.InvertirExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ModuloOp.
    def enterModuloOp(self, ctx:NeuralXParser.ModuloOpContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ModuloOp.
    def exitModuloOp(self, ctx:NeuralXParser.ModuloOpContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Variable.
    def enterVariable(self, ctx:NeuralXParser.VariableContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Variable.
    def exitVariable(self, ctx:NeuralXParser.VariableContext):
        pass


    # Enter a parse tree produced by NeuralXParser#OrdenarExpr.
    def enterOrdenarExpr(self, ctx:NeuralXParser.OrdenarExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#OrdenarExpr.
    def exitOrdenarExpr(self, ctx:NeuralXParser.OrdenarExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearRegLog.
    def enterCrearRegLog(self, ctx:NeuralXParser.CrearRegLogContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearRegLog.
    def exitCrearRegLog(self, ctx:NeuralXParser.CrearRegLogContext):
        pass


    # Enter a parse tree produced by NeuralXParser#FormaExpr.
    def enterFormaExpr(self, ctx:NeuralXParser.FormaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#FormaExpr.
    def exitFormaExpr(self, ctx:NeuralXParser.FormaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ExisteExpr.
    def enterExisteExpr(self, ctx:NeuralXParser.ExisteExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ExisteExpr.
    def exitExisteExpr(self, ctx:NeuralXParser.ExisteExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#LeerLineaExpr.
    def enterLeerLineaExpr(self, ctx:NeuralXParser.LeerLineaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#LeerLineaExpr.
    def exitLeerLineaExpr(self, ctx:NeuralXParser.LeerLineaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearRegLineal.
    def enterCrearRegLineal(self, ctx:NeuralXParser.CrearRegLinealContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearRegLineal.
    def exitCrearRegLineal(self, ctx:NeuralXParser.CrearRegLinealContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Multiplicacion.
    def enterMultiplicacion(self, ctx:NeuralXParser.MultiplicacionContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Multiplicacion.
    def exitMultiplicacion(self, ctx:NeuralXParser.MultiplicacionContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Tangente.
    def enterTangente(self, ctx:NeuralXParser.TangenteContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Tangente.
    def exitTangente(self, ctx:NeuralXParser.TangenteContext):
        pass


    # Enter a parse tree produced by NeuralXParser#LeerCSVExpr.
    def enterLeerCSVExpr(self, ctx:NeuralXParser.LeerCSVExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#LeerCSVExpr.
    def exitLeerCSVExpr(self, ctx:NeuralXParser.LeerCSVExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#AgregarCapa.
    def enterAgregarCapa(self, ctx:NeuralXParser.AgregarCapaContext):
        pass

    # Exit a parse tree produced by NeuralXParser#AgregarCapa.
    def exitAgregarCapa(self, ctx:NeuralXParser.AgregarCapaContext):
        pass


    # Enter a parse tree produced by NeuralXParser#EscribirCSVExpr.
    def enterEscribirCSVExpr(self, ctx:NeuralXParser.EscribirCSVExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#EscribirCSVExpr.
    def exitEscribirCSVExpr(self, ctx:NeuralXParser.EscribirCSVExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Redondear.
    def enterRedondear(self, ctx:NeuralXParser.RedondearContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Redondear.
    def exitRedondear(self, ctx:NeuralXParser.RedondearContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Division.
    def enterDivision(self, ctx:NeuralXParser.DivisionContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Division.
    def exitDivision(self, ctx:NeuralXParser.DivisionContext):
        pass


    # Enter a parse tree produced by NeuralXParser#IndiceExpr.
    def enterIndiceExpr(self, ctx:NeuralXParser.IndiceExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#IndiceExpr.
    def exitIndiceExpr(self, ctx:NeuralXParser.IndiceExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#LongitudExpr.
    def enterLongitudExpr(self, ctx:NeuralXParser.LongitudExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#LongitudExpr.
    def exitLongitudExpr(self, ctx:NeuralXParser.LongitudExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Resta.
    def enterResta(self, ctx:NeuralXParser.RestaContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Resta.
    def exitResta(self, ctx:NeuralXParser.RestaContext):
        pass


    # Enter a parse tree produced by NeuralXParser#NormaExpr.
    def enterNormaExpr(self, ctx:NeuralXParser.NormaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#NormaExpr.
    def exitNormaExpr(self, ctx:NeuralXParser.NormaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Logaritmo10.
    def enterLogaritmo10(self, ctx:NeuralXParser.Logaritmo10Context):
        pass

    # Exit a parse tree produced by NeuralXParser#Logaritmo10.
    def exitLogaritmo10(self, ctx:NeuralXParser.Logaritmo10Context):
        pass


    # Enter a parse tree produced by NeuralXParser#MatrizExpr.
    def enterMatrizExpr(self, ctx:NeuralXParser.MatrizExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#MatrizExpr.
    def exitMatrizExpr(self, ctx:NeuralXParser.MatrizExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Parentesis.
    def enterParentesis(self, ctx:NeuralXParser.ParentesisContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Parentesis.
    def exitParentesis(self, ctx:NeuralXParser.ParentesisContext):
        pass


    # Enter a parse tree produced by NeuralXParser#InerciaExpr.
    def enterInerciaExpr(self, ctx:NeuralXParser.InerciaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#InerciaExpr.
    def exitInerciaExpr(self, ctx:NeuralXParser.InerciaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearArreglo.
    def enterCrearArreglo(self, ctx:NeuralXParser.CrearArregloContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearArreglo.
    def exitCrearArreglo(self, ctx:NeuralXParser.CrearArregloContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearRNAPred.
    def enterCrearRNAPred(self, ctx:NeuralXParser.CrearRNAPredContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearRNAPred.
    def exitCrearRNAPred(self, ctx:NeuralXParser.CrearRNAPredContext):
        pass


    # Enter a parse tree produced by NeuralXParser#LlamadaExpr.
    def enterLlamadaExpr(self, ctx:NeuralXParser.LlamadaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#LlamadaExpr.
    def exitLlamadaExpr(self, ctx:NeuralXParser.LlamadaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#Logaritmo.
    def enterLogaritmo(self, ctx:NeuralXParser.LogaritmoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#Logaritmo.
    def exitLogaritmo(self, ctx:NeuralXParser.LogaritmoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CompilarMLP.
    def enterCompilarMLP(self, ctx:NeuralXParser.CompilarMLPContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CompilarMLP.
    def exitCompilarMLP(self, ctx:NeuralXParser.CompilarMLPContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ArcSeno.
    def enterArcSeno(self, ctx:NeuralXParser.ArcSenoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ArcSeno.
    def exitArcSeno(self, ctx:NeuralXParser.ArcSenoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CrearLista.
    def enterCrearLista(self, ctx:NeuralXParser.CrearListaContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CrearLista.
    def exitCrearLista(self, ctx:NeuralXParser.CrearListaContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ContieneExpr.
    def enterContieneExpr(self, ctx:NeuralXParser.ContieneExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ContieneExpr.
    def exitContieneExpr(self, ctx:NeuralXParser.ContieneExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ArcTangente.
    def enterArcTangente(self, ctx:NeuralXParser.ArcTangenteContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ArcTangente.
    def exitArcTangente(self, ctx:NeuralXParser.ArcTangenteContext):
        pass


    # Enter a parse tree produced by NeuralXParser#FilaCSVExpr.
    def enterFilaCSVExpr(self, ctx:NeuralXParser.FilaCSVExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#FilaCSVExpr.
    def exitFilaCSVExpr(self, ctx:NeuralXParser.FilaCSVExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ListaExpr.
    def enterListaExpr(self, ctx:NeuralXParser.ListaExprContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ListaExpr.
    def exitListaExpr(self, ctx:NeuralXParser.ListaExprContext):
        pass


    # Enter a parse tree produced by NeuralXParser#lista.
    def enterLista(self, ctx:NeuralXParser.ListaContext):
        pass

    # Exit a parse tree produced by NeuralXParser#lista.
    def exitLista(self, ctx:NeuralXParser.ListaContext):
        pass


    # Enter a parse tree produced by NeuralXParser#declaracionMatriz.
    def enterDeclaracionMatriz(self, ctx:NeuralXParser.DeclaracionMatrizContext):
        pass

    # Exit a parse tree produced by NeuralXParser#declaracionMatriz.
    def exitDeclaracionMatriz(self, ctx:NeuralXParser.DeclaracionMatrizContext):
        pass


    # Enter a parse tree produced by NeuralXParser#listaNumeros.
    def enterListaNumeros(self, ctx:NeuralXParser.ListaNumerosContext):
        pass

    # Exit a parse tree produced by NeuralXParser#listaNumeros.
    def exitListaNumeros(self, ctx:NeuralXParser.ListaNumerosContext):
        pass


    # Enter a parse tree produced by NeuralXParser#condicional.
    def enterCondicional(self, ctx:NeuralXParser.CondicionalContext):
        pass

    # Exit a parse tree produced by NeuralXParser#condicional.
    def exitCondicional(self, ctx:NeuralXParser.CondicionalContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondIgual.
    def enterCondIgual(self, ctx:NeuralXParser.CondIgualContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondIgual.
    def exitCondIgual(self, ctx:NeuralXParser.CondIgualContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondY.
    def enterCondY(self, ctx:NeuralXParser.CondYContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondY.
    def exitCondY(self, ctx:NeuralXParser.CondYContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondMayorIgual.
    def enterCondMayorIgual(self, ctx:NeuralXParser.CondMayorIgualContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondMayorIgual.
    def exitCondMayorIgual(self, ctx:NeuralXParser.CondMayorIgualContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondNo.
    def enterCondNo(self, ctx:NeuralXParser.CondNoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondNo.
    def exitCondNo(self, ctx:NeuralXParser.CondNoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondO.
    def enterCondO(self, ctx:NeuralXParser.CondOContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondO.
    def exitCondO(self, ctx:NeuralXParser.CondOContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondMenorIgual.
    def enterCondMenorIgual(self, ctx:NeuralXParser.CondMenorIgualContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondMenorIgual.
    def exitCondMenorIgual(self, ctx:NeuralXParser.CondMenorIgualContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondDiferente.
    def enterCondDiferente(self, ctx:NeuralXParser.CondDiferenteContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondDiferente.
    def exitCondDiferente(self, ctx:NeuralXParser.CondDiferenteContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondMenor.
    def enterCondMenor(self, ctx:NeuralXParser.CondMenorContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondMenor.
    def exitCondMenor(self, ctx:NeuralXParser.CondMenorContext):
        pass


    # Enter a parse tree produced by NeuralXParser#CondMayor.
    def enterCondMayor(self, ctx:NeuralXParser.CondMayorContext):
        pass

    # Exit a parse tree produced by NeuralXParser#CondMayor.
    def exitCondMayor(self, ctx:NeuralXParser.CondMayorContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ForRango.
    def enterForRango(self, ctx:NeuralXParser.ForRangoContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ForRango.
    def exitForRango(self, ctx:NeuralXParser.ForRangoContext):
        pass


    # Enter a parse tree produced by NeuralXParser#ForLista.
    def enterForLista(self, ctx:NeuralXParser.ForListaContext):
        pass

    # Exit a parse tree produced by NeuralXParser#ForLista.
    def exitForLista(self, ctx:NeuralXParser.ForListaContext):
        pass


    # Enter a parse tree produced by NeuralXParser#cicloWhile.
    def enterCicloWhile(self, ctx:NeuralXParser.CicloWhileContext):
        pass

    # Exit a parse tree produced by NeuralXParser#cicloWhile.
    def exitCicloWhile(self, ctx:NeuralXParser.CicloWhileContext):
        pass


    # Enter a parse tree produced by NeuralXParser#instruccionML.
    def enterInstruccionML(self, ctx:NeuralXParser.InstruccionMLContext):
        pass

    # Exit a parse tree produced by NeuralXParser#instruccionML.
    def exitInstruccionML(self, ctx:NeuralXParser.InstruccionMLContext):
        pass


    # Enter a parse tree produced by NeuralXParser#instruccionMatrix.
    def enterInstruccionMatrix(self, ctx:NeuralXParser.InstruccionMatrixContext):
        pass

    # Exit a parse tree produced by NeuralXParser#instruccionMatrix.
    def exitInstruccionMatrix(self, ctx:NeuralXParser.InstruccionMatrixContext):
        pass


    # Enter a parse tree produced by NeuralXParser#instruccionPlot.
    def enterInstruccionPlot(self, ctx:NeuralXParser.InstruccionPlotContext):
        pass

    # Exit a parse tree produced by NeuralXParser#instruccionPlot.
    def exitInstruccionPlot(self, ctx:NeuralXParser.InstruccionPlotContext):
        pass


    # Enter a parse tree produced by NeuralXParser#instruccionRed.
    def enterInstruccionRed(self, ctx:NeuralXParser.InstruccionRedContext):
        pass

    # Exit a parse tree produced by NeuralXParser#instruccionRed.
    def exitInstruccionRed(self, ctx:NeuralXParser.InstruccionRedContext):
        pass


    # Enter a parse tree produced by NeuralXParser#instruccionIO.
    def enterInstruccionIO(self, ctx:NeuralXParser.InstruccionIOContext):
        pass

    # Exit a parse tree produced by NeuralXParser#instruccionIO.
    def exitInstruccionIO(self, ctx:NeuralXParser.InstruccionIOContext):
        pass



del NeuralXParser