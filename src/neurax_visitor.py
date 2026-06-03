# neurax_visitor.py — Visitor completo de NeuralX
# Implementa todos los visitX para cada regla de la gramática.

import sys
from antlr4 import *

from NeuralXParser  import NeuralXParser
from NeuralXVisitor import NeuralXVisitor as NeuralXVisitorBase

from nx_math       import (_sen, _cos, _tan, _asen, _acos, _atan,
                            _log, _log10, _raiz, _abs, _piso, _techo,
                            _redondear, _potencia, PI, E)
from nx_matrix     import Matriz
from nx_estructuras import Lista, Arreglo
import nx_plot      as plot
from nx_io         import ArchivoTXT, ArchivoCSV, EscritorCSV, existe
from nx_regresion  import RegresionLineal, RegresionLogistica
from nx_perceptron import MLP
from nx_rna        import KMeans, DBSCAN, RNAClasificacion, RNAPrediccion


class Visitor(NeuralXVisitorBase):

    def __init__(self):
        self.entorno  = {}   # variables globales
        self._pila    = []   # pila de entornos para funciones
        self._funcs   = {}   # funciones declaradas
        self._retorno = None # valor de retorno activo

    # ── Utilidades internas ──────────────────────────────────────────

    def _empujar_entorno(self):
        self._pila.append(dict(self.entorno))

    def _sacar_entorno(self):
        self.entorno = self._pila.pop()

    def _obtener_var(self, nombre):
        if nombre in self.entorno:
            return self.entorno[nombre]
        raise RuntimeError(f"Variable '{nombre}' no definida")

    # ── Programa ─────────────────────────────────────────────────────

    def visitProg(self, ctx):
        resultado = None
        for instr in ctx.instruccion():
            resultado = self.visit(instr)
        return resultado

    def visitInstruccion(self, ctx):
        return self.visitChildren(ctx)

    # ── Variables ────────────────────────────────────────────────────

    def visitDeclaracionVar(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        valor  = self.visit(ctx.expresion())
        self.entorno[nombre] = valor
        return valor

    # ── Funciones ────────────────────────────────────────────────────

    def visitDeclaracionFuncion(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        self._funcs[nombre] = ctx
        return None

    def visitLlamadaExpr(self, ctx):
        return self.visitLlamadaFuncion(ctx.llamadaFuncion())

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        if nombre not in self._funcs:
            raise RuntimeError(f"Función '{nombre}' no definida")
        func_ctx = self._funcs[nombre]
        args     = []
        if ctx.argumentos():
            args = [self.visit(e) for e in ctx.argumentos().expresion()]
        params = []
        if func_ctx.parametros():
            params = [p.getText() for p in func_ctx.parametros().IDENTIFICADOR()]
        if len(args) != len(params):
            raise RuntimeError(
                f"Función '{nombre}': se esperaban {len(params)} argumentos, "
                f"se recibieron {len(args)}"
            )
        self._empujar_entorno()
        for p, a in zip(params, args):
            self.entorno[p] = a
        self._retorno = None
        for instr in func_ctx.instruccion():
            self.visit(instr)
            if self._retorno is not None:
                break
        resultado = self._retorno
        self._retorno = None
        self._sacar_entorno()
        return resultado

    def visitRetorno(self, ctx):
        self._retorno = self.visit(ctx.expresion())
        return self._retorno

    # ── Literales ────────────────────────────────────────────────────

    def visitNumero(self, ctx):
        texto = ctx.NUMERO().getText()
        return float(texto) if '.' in texto else int(texto)

    def visitCadenaExpr(self, ctx):
        return ctx.CADENA().getText()[1:-1]   # quitar comillas

    def visitVerdadero(self, ctx):
        return True

    def visitFalso(self, ctx):
        return False

    def visitVariable(self, ctx):
        return self._obtener_var(ctx.IDENTIFICADOR().getText())

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion())

    # ── Aritmética ───────────────────────────────────────────────────

    def visitPotencia(self, ctx):
        base = self.visit(ctx.expresion(0))
        exp  = self.visit(ctx.expresion(1))
        return _potencia(base, exp)

    def visitMultiplicacion(self, ctx):
        a = self.visit(ctx.expresion(0))
        b = self.visit(ctx.expresion(1))
        if isinstance(a, Matriz) and isinstance(b, Matriz):
            return a.multiplicacion(b)
        if isinstance(a, Matriz) and isinstance(b, (int, float)):
            return a.escalar(b)
        if isinstance(a, (int, float)) and isinstance(b, Matriz):
            return b.escalar(a)
        return a * b

    def visitDivision(self, ctx):
        a = self.visit(ctx.expresion(0))
        b = self.visit(ctx.expresion(1))
        if b == 0:
            raise RuntimeError("Error: división sobre 0")
        return a / b

    def visitSuma(self, ctx):
        a = self.visit(ctx.expresion(0))
        b = self.visit(ctx.expresion(1))
        if isinstance(a, Matriz) and isinstance(b, Matriz):
            return a.suma(b)
        return a + b

    def visitResta(self, ctx):
        a = self.visit(ctx.expresion(0))
        b = self.visit(ctx.expresion(1))
        if isinstance(a, Matriz) and isinstance(b, Matriz):
            return a.resta(b)
        return a - b

    def visitModuloOp(self, ctx):
        a = self.visit(ctx.expresion(0))
        b = self.visit(ctx.expresion(1))
        if b == 0:
            raise RuntimeError("Error: módulo sobre 0")
        return a % b

    def visitNegacion(self, ctx):
        return -self.visit(ctx.expresion())

    # ── Trigonometría ────────────────────────────────────────────────

    def visitSeno(self, ctx):       return _sen(self.visit(ctx.expresion()))
    def visitCoseno(self, ctx):     return _cos(self.visit(ctx.expresion()))
    def visitTangente(self, ctx):   return _tan(self.visit(ctx.expresion()))
    def visitArcSeno(self, ctx):    return _asen(self.visit(ctx.expresion()))
    def visitArcCoseno(self, ctx):  return _acos(self.visit(ctx.expresion()))
    def visitArcTangente(self, ctx):return _atan(self.visit(ctx.expresion()))

    # ── Matemática general ───────────────────────────────────────────

    def visitLogaritmo(self, ctx):    return _log(self.visit(ctx.expresion()))
    def visitLogaritmo10(self, ctx):  return _log10(self.visit(ctx.expresion()))
    def visitRaizCuad(self, ctx):     return _raiz(self.visit(ctx.expresion()))
    def visitValorAbsoluto(self, ctx):return _abs(self.visit(ctx.expresion()))
    def visitPiso(self, ctx):         return _piso(self.visit(ctx.expresion()))
    def visitTecho(self, ctx):        return _techo(self.visit(ctx.expresion()))
    def visitRedondear(self, ctx):    return _redondear(self.visit(ctx.expresion()))

    # ── Matrices ─────────────────────────────────────────────────────

    def visitMatrizExpr(self, ctx):
        filas = []
        for ln in ctx.declaracionMatriz().listaNumeros():
            fila = []
            for n in ln.NUMERO():
                t = n.getText()
                fila.append(float(t) if '.' in t else int(t))
            filas.append(fila)
        return Matriz(filas)

    def visitTransponerExpr(self, ctx):
        m = self.visit(ctx.expresion())
        if not isinstance(m, Matriz):
            raise RuntimeError("transponer: se esperaba una matriz")
        return m.transpuesta()

    def visitInvertirExpr(self, ctx):
        m = self.visit(ctx.expresion())
        if not isinstance(m, Matriz):
            raise RuntimeError("invertir: se esperaba una matriz")
        return m.inversa()

    def visitDetExpr(self, ctx):
        m = self.visit(ctx.expresion())
        if not isinstance(m, Matriz):
            raise RuntimeError("det: se esperaba una matriz")
        return m.determinante()

    def visitNormaExpr(self, ctx):
        m = self.visit(ctx.expresion())
        if not isinstance(m, Matriz):
            raise RuntimeError("norma: se esperaba una matriz")
        return m.norma()

    def visitFormaExpr(self, ctx):
        m = self.visit(ctx.expresion())
        if not isinstance(m, Matriz):
            raise RuntimeError("forma: se esperaba una matriz")
        return m.forma()

    def visitIdentidadExpr(self, ctx):
        n = int(self.visit(ctx.expresion()))
        return Matriz.identidad(n)

    def visitCerosExpr(self, ctx):
        f = int(self.visit(ctx.expresion(0)))
        c = int(self.visit(ctx.expresion(1)))
        return Matriz.ceros(f, c)

    def visitInstruccionMatrix(self, ctx):
        if ctx.TRANSPONER():
            m = self.visit(ctx.expresion(0))
            print(m.transpuesta())
        elif ctx.INVERTIR():
            m = self.visit(ctx.expresion(0))
            print(m.inversa())

    # ── Listas y Arreglos ────────────────────────────────────────────

    def visitListaExpr(self, ctx):
        l = Lista()
        for e in ctx.lista().expresion():
            l.agregar(self.visit(e))
        return l

    def visitCrearLista(self, ctx):
        return Lista()

    def visitCrearArreglo(self, ctx):
        tam   = int(self.visit(ctx.expresion(0)))
        valor = self.visit(ctx.expresion(1))
        return Arreglo(tam, valor)

    def visitAgregarExpr(self, ctx):
        col   = self.visit(ctx.expresion(0))
        valor = self.visit(ctx.expresion(1))
        if not isinstance(col, Lista):
            raise RuntimeError("agregar: solo aplica a Lista")
        col.agregar(valor)
        return col

    def visitEliminarExpr(self, ctx):
        col = self.visit(ctx.expresion(0))
        idx = self.visit(ctx.expresion(1))
        if isinstance(col, (Lista, Arreglo)):
            col.eliminar(idx)
        else:
            raise RuntimeError("eliminar: se esperaba Lista o Arreglo")
        return col

    def visitObtenerExpr(self, ctx):
        col = self.visit(ctx.expresion(0))
        idx = self.visit(ctx.expresion(1))
        if isinstance(col, (Lista, Arreglo)):
            return col.obtener(idx)
        raise RuntimeError("obtener: se esperaba Lista o Arreglo")

    def visitLongitudExpr(self, ctx):
        col = self.visit(ctx.expresion())
        if isinstance(col, (Lista, Arreglo)):
            return col.longitud()
        if isinstance(col, list):
            return len(col)
        raise RuntimeError("longitud: tipo no soportado")

    def visitOrdenarExpr(self, ctx):
        col = self.visit(ctx.expresion())
        if isinstance(col, (Lista, Arreglo)):
            return col.ordenar()
        raise RuntimeError("ordenar: se esperaba Lista o Arreglo")

    def visitContieneExpr(self, ctx):
        col   = self.visit(ctx.expresion(0))
        valor = self.visit(ctx.expresion(1))
        if isinstance(col, (Lista, Arreglo)):
            return col.contiene(valor)
        raise RuntimeError("contiene: se esperaba Lista o Arreglo")

    def visitIndiceExpr(self, ctx):
        col   = self.visit(ctx.expresion(0))
        valor = self.visit(ctx.expresion(1))
        if isinstance(col, Lista):
            return col.indice(valor)
        raise RuntimeError("indice: se esperaba Lista")

    def visitInvertirListaExpr(self, ctx):
        col = self.visit(ctx.expresion())
        if isinstance(col, Lista):
            return col.invertir()
        raise RuntimeError("invertirLista: se esperaba Lista")

    # ── Condicionales ────────────────────────────────────────────────

    def visitCondicional(self, ctx):
        condiciones  = ctx.condicion()
        instrucciones = ctx.instruccion()

        # Segmentar instrucciones por bloque usando índice de token.
        # Cada bloque i está entre la condicion[i] y la siguiente
        # condicion[i+1] (o el final si es sino).
        bloques = self._segmentar_bloques_condicional(condiciones, instrucciones)

        ejecutado = False
        for i, cond_ctx in enumerate(condiciones):
            if self.visit(cond_ctx):
                for instr in bloques[i]:
                    self.visit(instr)
                    if self._retorno is not None:
                        return
                ejecutado = True
                break

        if not ejecutado and len(bloques) > len(condiciones):
            for instr in bloques[-1]:
                self.visit(instr)
                if self._retorno is not None:
                    return

    def _segmentar_bloques_condicional(self, condiciones, instrucciones):
        """
        Agrupa instrucciones por bloque usando índice de token.
        Cada instrucción pertenece al bloque cuya condición tiene el
        índice de token más cercano anterior a la instrucción.
        El bloque 'sino' no tiene condición → bloque extra al final.
        """
        if not instrucciones:
            return [[] for _ in range(len(condiciones) + 1)]

        # Índice de inicio de cada condición
        limites_cond = [c.start.tokenIndex for c in condiciones]

        # Asignar cada instrucción al bloque correspondiente
        bloques = [[] for _ in range(len(condiciones) + 1)]

        for instr in instrucciones:
            idx = instr.start.tokenIndex
            # Buscar el bloque cuya condición sea la más cercana anterior
            bloque_asignado = len(condiciones)   # sino por defecto
            for j in range(len(limites_cond) - 1, -1, -1):
                if idx > limites_cond[j]:
                    bloque_asignado = j
                    break
            bloques[bloque_asignado].append(instr)

        return bloques

    # ── Condiciones ──────────────────────────────────────────────────

    def visitCondMayor(self, ctx):
        return self.visit(ctx.expresion(0)) > self.visit(ctx.expresion(1))

    def visitCondMenor(self, ctx):
        return self.visit(ctx.expresion(0)) < self.visit(ctx.expresion(1))

    def visitCondIgual(self, ctx):
        return self.visit(ctx.expresion(0)) == self.visit(ctx.expresion(1))

    def visitCondDiferente(self, ctx):
        return self.visit(ctx.expresion(0)) != self.visit(ctx.expresion(1))

    def visitCondMayorIgual(self, ctx):
        return self.visit(ctx.expresion(0)) >= self.visit(ctx.expresion(1))

    def visitCondMenorIgual(self, ctx):
        return self.visit(ctx.expresion(0)) <= self.visit(ctx.expresion(1))

    def visitCondY(self, ctx):
        return self.visit(ctx.condicion(0)) and self.visit(ctx.condicion(1))

    def visitCondO(self, ctx):
        return self.visit(ctx.condicion(0)) or self.visit(ctx.condicion(1))

    def visitCondNo(self, ctx):
        return not self.visit(ctx.condicion())

    # ── Ciclos ───────────────────────────────────────────────────────

    def visitForRango(self, ctx):
        var   = ctx.IDENTIFICADOR().getText()
        ini   = int(ctx.NUMERO(0).getText())
        fin   = int(ctx.NUMERO(1).getText())
        paso  = 1 if ini <= fin else -1
        i = ini
        while (paso > 0 and i <= fin) or (paso < 0 and i >= fin):
            self.entorno[var] = i
            for instr in ctx.instruccion():
                self.visit(instr)
                if self._retorno is not None:
                    return
            i += paso

    def visitForLista(self, ctx):
        var       = ctx.IDENTIFICADOR().getText()
        coleccion = self.visit(ctx.expresion())
        if isinstance(coleccion, (Lista, Arreglo)):
            elementos = coleccion.a_lista_python()
        elif isinstance(coleccion, list):
            elementos = coleccion
        else:
            raise RuntimeError("repite...en: se esperaba Lista, Arreglo o lista")
        for elem in elementos:
            self.entorno[var] = elem
            for instr in ctx.instruccion():
                self.visit(instr)
                if self._retorno is not None:
                    return

    def visitCicloWhile(self, ctx):
        limite = 100_000
        iters  = 0
        while self.visit(ctx.condicion()):
            for instr in ctx.instruccion():
                self.visit(instr)
                if self._retorno is not None:
                    return
            iters += 1
            if iters >= limite:
                raise RuntimeError("mientras: límite de 100.000 iteraciones alcanzado")

    # ── IO ───────────────────────────────────────────────────────────

    def visitInstruccionIO(self, ctx):
        if ctx.ABRIR():
            ruta  = ctx.CADENA(0).getText()[1:-1]
            modo  = ctx.CADENA(1).getText()[1:-1]
            arch  = ArchivoTXT(ruta, modo)
            # guardar en variable si viene asignado — aquí solo retornamos
            return arch
        elif ctx.CERRAR():
            arch = self.visit(ctx.expresion(0))
            if not isinstance(arch, ArchivoTXT):
                raise RuntimeError("cerrar: se esperaba un archivo abierto")
            arch.cerrar()
        elif ctx.ESCRIBIR():
            arch  = self.visit(ctx.expresion(0))
            texto = self.visit(ctx.expresion(1))
            if not isinstance(arch, ArchivoTXT):
                raise RuntimeError("escribir: se esperaba un archivo abierto")
            arch.escribir(texto)
        elif ctx.GUARDAR():
            ruta  = ctx.CADENA(0).getText()[1:-1]
            valor = self.visit(ctx.expresion(0))
            arch  = ArchivoTXT(ruta, "w")
            arch.escribir(str(valor))
            arch.cerrar()
        elif ctx.MOSTRAR():
            valor = self.visit(ctx.expresion(0))
            print(valor)

    def visitLeerTodoExpr(self, ctx):
        arch = self.visit(ctx.expresion())
        if not isinstance(arch, ArchivoTXT):
            raise RuntimeError("leerTodo: se esperaba un archivo abierto")
        return arch.leer_todo()

    def visitLeerLineaExpr(self, ctx):
        arch = self.visit(ctx.expresion())
        if not isinstance(arch, ArchivoTXT):
            raise RuntimeError("leerLinea: se esperaba un archivo abierto")
        return arch.leer_linea()

    def visitLineasExpr(self, ctx):
        arch = self.visit(ctx.expresion())
        if not isinstance(arch, ArchivoTXT):
            raise RuntimeError("lineas: se esperaba un archivo abierto")
        return arch.lineas()

    def visitLeerCSVExpr(self, ctx):
        ruta = ctx.CADENA().getText()[1:-1]
        return ArchivoCSV(ruta)

    def visitEscribirCSVExpr(self, ctx):
        ruta  = ctx.CADENA().getText()[1:-1]
        datos = self.visit(ctx.expresion())
        esc   = EscritorCSV(ruta)
        if isinstance(datos, Matriz):
            for fila in datos.datos:
                esc.agregar_fila(fila)
        elif isinstance(datos, (Lista, Arreglo)):
            for elem in datos.a_lista_python():
                esc.agregar_fila(
                    elem if isinstance(elem, (Lista, Arreglo))
                    else [elem]
                )
        esc.guardar()
        return True

    def visitExisteExpr(self, ctx):
        return existe(ctx.CADENA().getText()[1:-1])

    def visitColumnasCSVExpr(self, ctx):
        csv = self.visit(ctx.expresion())
        if not isinstance(csv, ArchivoCSV):
            raise RuntimeError("columnasCSV: se esperaba un CSV cargado")
        return csv.columnas()

    def visitFilaCSVExpr(self, ctx):
        csv = self.visit(ctx.expresion(0))
        idx = self.visit(ctx.expresion(1))
        if not isinstance(csv, ArchivoCSV):
            raise RuntimeError("filaCSV: se esperaba un CSV cargado")
        return csv.fila(idx)

    # ── Plot ─────────────────────────────────────────────────────────

    def visitInstruccionPlot(self, ctx):
        if ctx.GRAFICAR():
            xs    = self.visit(ctx.expresion(0))
            ys    = self.visit(ctx.expresion(1))
            color = ctx.CADENA().getText()[1:-1] if ctx.CADENA() else "*"
            plot.graficar(xs, ys, color)
        elif ctx.DISPERSAR():
            xs    = self.visit(ctx.expresion(0))
            ys    = self.visit(ctx.expresion(1))
            color = ctx.CADENA().getText()[1:-1] if ctx.CADENA() else "o"
            plot.dispersar(xs, ys, color)
        elif ctx.BARRAS():
            plot.barras(self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)))
        elif ctx.HISTOGRAMA():
            plot.histograma(self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)))
        elif ctx.TITULO():
            plot.titulo(ctx.CADENA().getText()[1:-1])
        elif ctx.EJEX():
            plot.eje_x(ctx.CADENA().getText()[1:-1])
        elif ctx.EJEY():
            plot.eje_y(ctx.CADENA().getText()[1:-1])
        elif ctx.ETIQUETA_P():
            plot.etiqueta(ctx.CADENA().getText()[1:-1])
        elif ctx.LEYENDA():
            plot.leyenda()
        elif ctx.CUADRICULA():
            plot.cuadricula()
        elif ctx.RANGO_X():
            plot.rango_x(self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)))
        elif ctx.RANGO_Y():
            plot.rango_y(self.visit(ctx.expresion(0)), self.visit(ctx.expresion(1)))
        elif ctx.LIMPIAR():
            plot.limpiar()
        elif ctx.GUARDAR_G():
            plot.guardar_grafica(ctx.CADENA().getText()[1:-1])
        elif ctx.MOSTRAR_P():
            plot.mostrar()

    # ── ML — Regresión ───────────────────────────────────────────────

    def visitCrearRegLineal(self, ctx):
        return RegresionLineal()

    def visitCrearRegLog(self, ctx):
        return RegresionLogistica()

    def visitEntrenarMod(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        X      = self.visit(ctx.expresion(1))
        y      = self.visit(ctx.expresion(2))
        if not hasattr(modelo, "entrenar"):
            raise RuntimeError("entrenarModelo: se esperaba un modelo")
        modelo.entrenar(X, y)
        return modelo

    def visitPredecirMod(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        X      = self.visit(ctx.expresion(1))
        if not hasattr(modelo, "predecir"):
            raise RuntimeError("predecirModelo: modelo no entrenado o inválido")
        return modelo.predecir(X)

    def visitEvaluarMod(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        X      = self.visit(ctx.expresion(1))
        y      = self.visit(ctx.expresion(2))
        if not hasattr(modelo, "evaluar"):
            raise RuntimeError("evaluar: se esperaba un modelo entrenado")
        return modelo.evaluar(X, y)

    def visitInterceptoExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not hasattr(modelo, "intercepto"):
            raise RuntimeError("intercepto: se esperaba un modelo entrenado")
        return modelo.intercepto()

    def visitPrecisionExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not hasattr(modelo, "precision"):
            raise RuntimeError("precision: se esperaba un modelo logístico")
        return modelo.precision

    def visitErrorModExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not hasattr(modelo, "error"):
            raise RuntimeError("errorModelo: se esperaba un modelo entrenado")
        return modelo.error()

    def visitCoeficientesExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not hasattr(modelo, "coeficientes"):
            raise RuntimeError("coeficientes: se esperaba un modelo entrenado")
        return modelo.coeficientes()

    # ── MLP ──────────────────────────────────────────────────────────

    def visitCrearMLP(self, ctx):
        return MLP()

    def visitAgregarCapa(self, ctx):
        modelo     = self.visit(ctx.expresion(0))
        neuronas   = int(self.visit(ctx.expresion(1)))
        activacion = ctx.CADENA().getText()[1:-1]
        if not isinstance(modelo, (MLP, RNAClasificacion, RNAPrediccion)):
            raise RuntimeError("capaDensa: se esperaba mlp(), rnaClas() o rnaPred()")
        modelo.agregar_capa(neuronas, activacion)
        return modelo

    def visitCompilarMLP(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        tasa   = self.visit(ctx.expresion(1))
        epocas = self.visit(ctx.expresion(2))
        tarea  = ctx.CADENA().getText()[1:-1]
        if not hasattr(modelo, "compilar"):
            raise RuntimeError("compilar: se esperaba un modelo")
        modelo.compilar(tasa, epocas, tarea)
        return modelo

    def visitPerdidaExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not hasattr(modelo, "perdida"):
            raise RuntimeError("perdida: se esperaba un modelo entrenado")
        return modelo.perdida()

    def visitHistoriaExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not hasattr(modelo, "historia"):
            raise RuntimeError("historia: se esperaba un modelo entrenado")
        return modelo.historia()

    # ── RNA / Agrupamiento ───────────────────────────────────────────

    def visitCrearKMeans(self, ctx):
        k = self.visit(ctx.expresion())
        return KMeans(k)

    def visitCrearDBSCAN(self, ctx):
        eps = self.visit(ctx.expresion(0))
        mp  = self.visit(ctx.expresion(1))
        return DBSCAN(eps, mp)

    def visitCrearRNAClas(self, ctx):
        return RNAClasificacion()

    def visitCrearRNAPred(self, ctx):
        return RNAPrediccion()

    def visitCentroidesExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not isinstance(modelo, KMeans):
            raise RuntimeError("centroides: se esperaba kMeans entrenado")
        return modelo.centroides()

    def visitEtiquetasExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not hasattr(modelo, "etiquetas"):
            raise RuntimeError("etiquetas: se esperaba modelo de agrupamiento")
        return modelo.etiquetas()

    def visitInerciaExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        if not isinstance(modelo, KMeans):
            raise RuntimeError("inercia: se esperaba kMeans entrenado")
        return modelo.inercia()

    # ── instruccionRed ───────────────────────────────────────────────

    def visitInstruccionRed(self, ctx):
        pass   # compatibilidad con sintaxis legada

    # ── instruccionML legado ─────────────────────────────────────────

    def visitInstruccionML(self, ctx):
        pass

    def visitAjustarExpr(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        X      = self.visit(ctx.expresion(1))
        if hasattr(modelo, "entrenar"):
            modelo.entrenar(X, None)
        return modelo

    def visitClasificarExpr(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        X      = self.visit(ctx.expresion(1))
        if hasattr(modelo, "predecir"):
            return modelo.predecir(X)
        return None

    def visitPredecirExpr(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        X      = self.visit(ctx.expresion(1))
        if hasattr(modelo, "predecir"):
            return modelo.predecir(X)
        return None
