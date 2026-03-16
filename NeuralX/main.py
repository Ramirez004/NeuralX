import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from NeuralXLexer import NeuralXLexer
from NeuralXParser import NeuralXParser
from NeuralXVisitorImpl import NeuralXVisitorImpl


# ─────────────────────────────────────────────
#  MANEJADOR DE ERRORES EN ESPAÑOL
# ─────────────────────────────────────────────

class ErrorNeuralX(ErrorListener):
    def __init__(self):
        super().__init__()
        self.hay_errores = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hay_errores = True
        simbolo = offendingSymbol.text if offendingSymbol else "desconocido"
        print(f"[NeuralX] Error de sintaxis en línea {line}, columna {column}: símbolo inesperado '{simbolo}'")


# ─────────────────────────────────────────────
#  FUNCIÓN PRINCIPAL DE EJECUCIÓN
# ─────────────────────────────────────────────

def ejecutar(codigo, visitor):
    input_stream = InputStream(codigo)

    lexer = NeuralXLexer(input_stream)
    lexer.removeErrorListeners()
    error_listener = ErrorNeuralX()
    lexer.addErrorListener(error_listener)

    tokens = CommonTokenStream(lexer)

    parser = NeuralXParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.prog()

    # Si hubo error de sintaxis, no continuar
    if error_listener.hay_errores:
        return

    try:
        visitor.visit(tree)
    except ZeroDivisionError as e:
        print(e)
    except NameError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except ImportError as e:
        print(e)
    except Exception as e:
        print(f"[NeuralX] Error en ejecución: {e}")


# ─────────────────────────────────────────────
#  MODO ARCHIVO — python main.py archivo.nx
# ─────────────────────────────────────────────

def modo_archivo(ruta, visitor):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            codigo = f.read()
        print(f"[NeuralX] Ejecutando archivo: {ruta}")
        print("-" * 40)
        ejecutar(codigo, visitor)
    except FileNotFoundError:
        print(f"[NeuralX] Error: no se encontró el archivo '{ruta}'")
        sys.exit(1)


# ─────────────────────────────────────────────
#  MODO REPL — python main.py
# ─────────────────────────────────────────────

def modo_repl(visitor):
    print("=" * 45)
    print("  NeuralX — DSL para Deep Learning")
    print("  Escribe código NeuralX y presiona Enter.")
    print("  Escribe 'salir' para terminar.")
    print("=" * 45)

    buffer = []

    while True:
        try:
            prompt = "... " if buffer else "NeuralX> "
            linea = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("\n[NeuralX] Sesión terminada.")
            break

        if linea.strip() == "salir":
            print("[NeuralX] ¡Hasta luego!")
            break

        if linea.strip() == "":
            if buffer:
                codigo = "\n".join(buffer)
                buffer = []
                ejecutar(codigo, visitor)
            continue

        buffer.append(linea)

        # Ejecutar si las llaves están balanceadas (bloques si/mientras/repite)
        codigo_actual = "\n".join(buffer)
        if codigo_actual.count("{") == codigo_actual.count("}"):
            ejecutar(codigo_actual, visitor)
            buffer = []


# ─────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    # El visitor se crea una vez — las variables persisten en el REPL
    visitor = NeuralXVisitorImpl()

    if len(sys.argv) > 1:
        modo_archivo(sys.argv[1], visitor)
    else:
        modo_repl(visitor)
