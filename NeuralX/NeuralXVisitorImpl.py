import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neural_network import MLPClassifier

# tensorflow es opcional — se carga solo si se usa NeuralX.Net con red()
try:
    from tensorflow import keras
    KERAS_OK = True
except ImportError:
    KERAS_OK = False

from NeuralXVisitor import NeuralXVisitor


class NeuralXVisitorImpl(NeuralXVisitor):

    def __init__(self):
        # Tabla de símbolos: guarda todas las variables declaradas con 'var'
        self.tabla = {}

    # ─────────────────────────────────────────────
    #  VARIABLES
    # ─────────────────────────────────────────────

    def visitDeclaracionVar(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        self.tabla[nombre] = valor
        return valor

    def visitVariable(self, ctx):
        nombre = ctx.IDENTIFICADOR().getText()
        # CORREGIDO: error claro si la variable no fue declarada
        if nombre not in self.tabla:
            raise NameError(f"[NeuralX] Error: variable '{nombre}' no fue declarada.")
        return self.tabla[nombre]

    # ─────────────────────────────────────────────
    #  ARITMÉTICA
    # ─────────────────────────────────────────────

    def visitSuma(self, ctx):
        return self.visit(ctx.expresion(0)) + self.visit(ctx.expresion(1))

    def visitResta(self, ctx):
        return self.visit(ctx.expresion(0)) - self.visit(ctx.expresion(1))

    def visitMultiplicacion(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        if isinstance(izq, np.ndarray) and isinstance(der, np.ndarray):
            return np.matmul(izq, der)
        return izq * der

    def visitDivision(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        # CORREGIDO: manejo explícito de división por cero
        if der == 0:
            raise ZeroDivisionError("[NeuralX] Error: no se puede dividir por cero.")
        return izq / der

    def visitPotencia(self, ctx):
        return self.visit(ctx.expresion(0)) ** self.visit(ctx.expresion(1))

    def visitModuloOp(self, ctx):
        return self.visit(ctx.expresion(0)) % self.visit(ctx.expresion(1))

    def visitSeno(self, ctx):
        return math.sin(self.visit(ctx.expresion()))

    def visitCoseno(self, ctx):
        return math.cos(self.visit(ctx.expresion()))

    def visitTangente(self, ctx):
        return math.tan(self.visit(ctx.expresion()))

    def visitNumero(self, ctx):
        return float(ctx.NUMERO().getText())

    def visitParentesis(self, ctx):
        return self.visit(ctx.expresion(0))

    # ─────────────────────────────────────────────
    #  LISTAS Y MATRICES
    # ─────────────────────────────────────────────

    def visitListaExpr(self, ctx):
        return [self.visit(e) for e in ctx.lista().expresion()]

    def visitMatrizExpr(self, ctx):
        filas = []
        for listaCtx in ctx.declaracionMatriz().listaNumeros():
            fila = [float(n.getText()) for n in listaCtx.NUMERO()]
            filas.append(fila)
        return np.array(filas)

    # ─────────────────────────────────────────────
    #  MATRIX — transponer e invertir como expresión
    # ─────────────────────────────────────────────

    def visitTransponerExpr(self, ctx):
        m = self.visit(ctx.expresion())
        return np.transpose(m)

    def visitInvertirExpr(self, ctx):
        m = self.visit(ctx.expresion())
        return np.linalg.inv(m)

    # ─────────────────────────────────────────────
    #  ML — como expresiones (permiten var modelo = ajustar(x,y))
    # ─────────────────────────────────────────────

    def visitAjustarExpr(self, ctx):
        x = np.array(self.visit(ctx.expresion(0))).reshape(-1, 1)
        y = np.array(self.visit(ctx.expresion(1)))
        modelo = LinearRegression()
        modelo.fit(x, y)
        print(f"[NeuralX] Modelo ajustado — pendiente: {modelo.coef_[0]:.4f}, intercepto: {modelo.intercept_:.4f}")
        return modelo

    def visitClasificarExpr(self, ctx):
        x = np.array(self.visit(ctx.expresion(0))).reshape(-1, 1)
        y = np.array(self.visit(ctx.expresion(1)))
        modelo = LogisticRegression()
        modelo.fit(x, y)
        print("[NeuralX] Modelo logístico ajustado.")
        return modelo

    def visitPredecirExpr(self, ctx):
        modelo = self.visit(ctx.expresion(0))
        x = np.array(self.visit(ctx.expresion(1))).reshape(-1, 1)
        return modelo.predict(x)

    def visitCoeficientesExpr(self, ctx):
        modelo = self.visit(ctx.expresion())
        return {'pendiente': modelo.coef_.tolist(), 'intercepto': modelo.intercept_.tolist()}

    # ML como instrucción standalone (sin asignación)
    def visitInstruccionML(self, ctx):
        if ctx.AJUSTAR():
            x = np.array(self.visit(ctx.expresion(0))).reshape(-1, 1)
            y = np.array(self.visit(ctx.expresion(1)))
            modelo = LinearRegression()
            modelo.fit(x, y)
            return modelo
        elif ctx.CLASIFICAR():
            x = np.array(self.visit(ctx.expresion(0))).reshape(-1, 1)
            y = np.array(self.visit(ctx.expresion(1)))
            modelo = LogisticRegression()
            modelo.fit(x, y)
            return modelo
        elif ctx.PREDECIR():
            modelo = self.visit(ctx.expresion(0))
            x = np.array(self.visit(ctx.expresion(1))).reshape(-1, 1)
            return modelo.predict(x)
        elif ctx.COEFICIENTES():
            modelo = self.visit(ctx.expresion())
            return {'pendiente': modelo.coef_.tolist(), 'intercepto': modelo.intercept_.tolist()}

    # ─────────────────────────────────────────────
    #  PLOT
    # ─────────────────────────────────────────────

    def visitInstruccionPlot(self, ctx):
        if ctx.GRAFICAR():
            x = self.visit(ctx.expresion(0))
            y = self.visit(ctx.expresion(1))
            plt.plot(x, y)
        elif ctx.DISPERSAR():
            x = self.visit(ctx.expresion(0))
            y = self.visit(ctx.expresion(1))
            plt.scatter(x, y)
        elif ctx.TITULO():
            plt.title(ctx.CADENA().getText().strip('"'))
        elif ctx.EJEX():
            plt.xlabel(ctx.CADENA().getText().strip('"'))
        elif ctx.EJEY():
            plt.ylabel(ctx.CADENA().getText().strip('"'))
        elif ctx.MOSTRAR():
            plt.show()

    # ─────────────────────────────────────────────
    #  REDES NEURONALES
    # ─────────────────────────────────────────────

    def visitInstruccionRed(self, ctx):
        capas = [int(n.getText()) for n in ctx.listaNumeros().NUMERO()]
        if ctx.RED():
            if not KERAS_OK:
                raise ImportError("[NeuralX] Error: tensorflow no instalado. Ejecuta: pip install tensorflow")
            modelo = keras.Sequential()
            for c in capas[:-1]:
                modelo.add(keras.layers.Dense(c, activation='relu'))
            modelo.add(keras.layers.Dense(capas[-1]))
            modelo.compile(optimizer='adam', loss='mse')
            print(f"[NeuralX] Red neuronal creada con capas: {capas}")
            return modelo
        elif ctx.PERCEPTRON():
            modelo = MLPClassifier(hidden_layer_sizes=tuple(capas[:-1]), max_iter=1000)
            print(f"[NeuralX] Perceptrón creado con capas ocultas: {capas[:-1]}")
            return modelo
        elif ctx.ENTRENAR():
            modelo = self.visit(ctx.expresion(0))
            x = np.array(self.visit(ctx.expresion(1)))
            y = np.array(self.visit(ctx.expresion(2)))
            if x.ndim == 1:
                x = x.reshape(-1, 1)
            modelo.fit(x, y)
            print("[NeuralX] Entrenamiento completado.")
            return modelo

    # ─────────────────────────────────────────────
    #  IO
    # ─────────────────────────────────────────────

    def visitInstruccionIO(self, ctx):
        if ctx.ABRIR():
            ruta = ctx.CADENA().getText().strip('"')
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                print(f"[NeuralX] Archivo '{ruta}' leído correctamente.")
                return contenido
            except FileNotFoundError:
                raise FileNotFoundError(f"[NeuralX] Error: archivo '{ruta}' no encontrado.")
        elif ctx.GUARDAR():
            ruta = ctx.CADENA().getText().strip('"')
            datos = str(self.visit(ctx.expresion()))
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(datos)
            print(f"[NeuralX] Datos guardados en '{ruta}'.")
        elif ctx.MOSTRAR():
            valor = self.visit(ctx.expresion())
            print(valor)
            return valor

    # ─────────────────────────────────────────────
    #  CONDICIONALES
    # ─────────────────────────────────────────────

    def visitCondicional(self, ctx):
        condicion = self.visit(ctx.condicion())
        instrucciones = ctx.instruccion()
        if ctx.SINO():
            # Separar instrucciones del bloque si y del bloque sino
            sino_pos = ctx.SINO().symbol.tokenIndex
            bloque_si = [i for i in instrucciones if i.start.tokenIndex < sino_pos]
            bloque_sino = [i for i in instrucciones if i.start.tokenIndex > sino_pos]
            if condicion:
                for instr in bloque_si:
                    self.visit(instr)
            else:
                for instr in bloque_sino:
                    self.visit(instr)
        else:
            if condicion:
                for instr in instrucciones:
                    self.visit(instr)

    def visitCondicion(self, ctx):
        izq = self.visit(ctx.expresion(0))
        der = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        if op == '>':
            return izq > der
        elif op == '<':
            return izq < der
        elif op == '==':
            return izq == der

    # ─────────────────────────────────────────────
    #  CICLOS
    # ─────────────────────────────────────────────

    def visitCicloFor(self, ctx):
        variable = ctx.IDENTIFICADOR().getText()
        inicio = int(ctx.NUMERO(0).getText())
        fin = int(ctx.NUMERO(1).getText())
        for i in range(inicio, fin + 1):
            self.tabla[variable] = i
            for instr in ctx.instruccion():
                self.visit(instr)

    def visitCicloWhile(self, ctx):
        while self.visit(ctx.condicion()):
            for instr in ctx.instruccion():
                self.visit(instr)

    # ─────────────────────────────────────────────
    #  IMPORTACIONES
    # ─────────────────────────────────────────────

    def visitImportacion(self, ctx):
        modulo = ctx.modulo().getText()
        print(f"[NeuralX] Módulo importado: {modulo}")
