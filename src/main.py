#!/usr/bin/env python3
# main.py — Intérprete NeuralX
# Uso:
#   python main.py              → consola interactiva (REPL)
#   python main.py archivo.nx   → ejecutar archivo

import nx_loader
nx_loader.register()
import sys
import os

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from NeuralXLexer    import NeuralXLexer
from NeuralXParser   import NeuralXParser
from neurax_visitor  import Visitor


# ── Manejo de errores de sintaxis ────────────────────────────────────

class ErrorSintaxis(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"  Línea {line}:{column} — {msg}")


# ── Función principal de ejecución ───────────────────────────────────

def ejecutar(codigo: str, visitor: Visitor) -> bool:
    """
    Parsea y ejecuta un bloque de código NeuralX.
    Retorna True si fue exitoso, False si hubo error.
    """
    stream     = InputStream(codigo)
    lexer      = NeuralXLexer(stream)
    tokens     = CommonTokenStream(lexer)
    parser     = NeuralXParser(tokens)

    # Quitar listeners por defecto y agregar el nuestro
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    err = ErrorSintaxis()
    lexer.addErrorListener(err)
    parser.addErrorListener(err)

    tree = parser.prog()

    if err.errores:
        print("[NeuralX] Error de sintaxis:")
        for e in err.errores:
            print(e)
        return False

    try:
        visitor.visit(tree)
        return True
    except RuntimeError as e:
        print(f"[NeuralX Error] {e}")
        return False
    except RecursionError:
        print("[NeuralX Error] Recursión demasiado profunda")
        return False
    except Exception as e:
        print(f"[NeuralX Error inesperado] {type(e).__name__}: {e}")
        return False


# ── Modo archivo ──────────────────────────────────────────────────────

def modo_archivo(ruta: str):
    if not os.path.exists(ruta):
        print(f"[NeuralX] Archivo no encontrado: '{ruta}'")
        sys.exit(1)
    with open(ruta, "r", encoding="utf-8") as f:
        codigo = f.read()
    visitor = Visitor()
    ok = ejecutar(codigo, visitor)
    sys.exit(0 if ok else 1)


# ── REPL — consola interactiva ────────────────────────────────────────

BANNER = """
╔══════════════════════════════════════════════════════╗
║          NeuralX — DSL de Deep Learning              ║
║          Intérprete interactivo v1.0                 ║
╠══════════════════════════════════════════════════════╣
║  Escribe código NeuralX y presiona Enter dos veces   ║
║  Comandos: :salir  :limpiar  :ayuda                  ║
╚══════════════════════════════════════════════════════╝
"""

AYUDA = """
Comandos especiales:
  :salir    → cerrar el intérprete
  :limpiar  → resetear variables y funciones
  :ayuda    → mostrar este mensaje

Tipos disponibles:
  Números       → 42  3.14
  Cadenas       → "hola"
  Booleanos     → verdadero  falso
  Matrices      → mat[[1,2],[3,4]]
  Listas        → Lista()
  Arreglos      → Arreglo(5, 0)

Ejemplos rápidos:
  var x = 2 ^ 10
  mostrar(x)

  var M = mat[[1,2],[3,4]]
  mostrar(transponer(M))

  var modelo = regresionLineal()
  var X = mat[[1],[2],[3]]
  var y = mat[[2,4,6]]
  entrenarModelo(modelo, X, y)
  mostrar(predecirModelo(modelo, mat[[4]]))
"""

def modo_repl():
    print(BANNER)
    visitor  = Visitor()
    buffer   = []

    while True:
        try:
            prompt = "NX> " if not buffer else "... "
            linea  = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("\n[NeuralX] Hasta luego.")
            break

        # Comandos especiales
        if linea.strip() == ":salir":
            print("[NeuralX] Hasta luego.")
            break
        elif linea.strip() == ":limpiar":
            visitor = Visitor()
            buffer  = []
            print("[NeuralX] Entorno reiniciado.")
            continue
        elif linea.strip() == ":ayuda":
            print(AYUDA)
            buffer = []
            continue

        buffer.append(linea)

        # Ejecutar cuando hay una línea en blanco o bloque completo
        codigo = "\n".join(buffer)
        if linea.strip() == "" or _bloque_completo(codigo):
            codigo = codigo.strip()
            if codigo:
                ejecutar(codigo, visitor)
            buffer = []


def _bloque_completo(codigo: str) -> bool:
    """Heurística simple: el código está listo si las llaves están balanceadas
    y no termina en ':' o 'then'."""
    abiertos = codigo.count("{") - codigo.count("}")
    return abiertos <= 0 and codigo.strip() != ""


# ── Punto de entrada ──────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) > 1:
        modo_archivo(sys.argv[1])
    else:
        modo_repl()
