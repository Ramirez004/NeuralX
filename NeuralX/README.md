# NeuralX — DSL para Deep Learning

Lenguaje de dominio específico implementado con ANTLRv4 y Python usando el patrón Visitor.

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `NeuralX.g4` | Gramática del lenguaje — define tokens y reglas sintácticas |
| `NeuralXVisitorImpl.py` | Visitor — interpreta el AST y ejecuta cada operación |
| `main.py` | Punto de entrada — conecta Lexer, Parser y Visitor |
| `pruebas.nx` | Archivo de pruebas escrito en NeuralX |

Archivos generados automáticamente por ANTLR (no editar):

| Archivo | Descripción |
|---|---|
| `NeuralXLexer.py` | Convierte el texto en tokens |
| `NeuralXParser.py` | Construye el árbol de sintaxis (AST) |
| `NeuralXVisitor.py` | Clase base del Visitor |
| `NeuralXListener.py` | No se usa en este proyecto |

---

## Requisitos

- Python 3.8+
- Java 11+ (requerido por ANTLR)

---

## Instalación

**Paso 1 — Crear y activar el entorno virtual**
```bash
python3 -m venv neuralx-env
source neuralx-env/bin/activate
```

**Paso 2 — Instalar dependencias**
```bash
pip install antlr4-python3-runtime==4.13.1
pip install numpy matplotlib scikit-learn
pip install antlr4-tools
```

---

## Generar el parser

Este paso convierte `NeuralX.g4` en los archivos Python que necesita el proyecto.
Solo se ejecuta una vez, o cada vez que se modifique el `.g4`.

```bash
antlr4 -Dlanguage=Python3 -visitor NeuralX.g4
```

Archivos que genera:
```
NeuralXLexer.py
NeuralXParser.py
NeuralXVisitor.py
NeuralXListener.py
```

---

## Ejecutar

**Modo REPL — escribir código línea por línea**
```bash
python main.py
```

Ejemplo:
```
NeuralX> var x = 5 + 3
NeuralX> mostrar(x)
8.0
NeuralX> salir
```

**Modo archivo — ejecutar un archivo .nx**
```bash
python main.py pruebas.nx
```

---

## Archivos de entrada

`main.py` acepta archivos `.nx` — archivos de texto plano con código NeuralX.

Ejemplo de archivo `.nx`:
```
var x = 10
var y = 3
var resultado = x * y
mostrar(resultado)
```

---

## Cada vez que abran una terminal nueva

```bash
source neuralx-env/bin/activate
cd NeuralX
python main.py
```

---

## Documentación del código

### NeuralX.g4

Define la gramática completa del lenguaje NeuralX.

- `prog` — regla de inicio, contiene todas las instrucciones
- `instruccion` — cualquier instrucción válida del lenguaje
- `declaracionVar` — declara una variable: `var x = expresion`
- `expresion` — operaciones aritméticas con precedencia correcta
- `lista` — lista de valores: `[1, 2, 3]`
- `declaracionMatriz` — matriz: `mat[[1,2],[3,4]]`
- `condicional` — bloque `si / sino`
- `cicloFor` — ciclo `repite i en [0..n]`
- `cicloWhile` — ciclo `mientras`
- `instruccionML` — operaciones de machine learning
- `instruccionPlot` — operaciones de graficación
- `instruccionRed` — redes neuronales
- `instruccionIO` — lectura y escritura de archivos

---

### NeuralXVisitorImpl.py

Implementa el patrón Visitor sobre el AST generado por ANTLR.
Cada método `visit` corresponde a una regla del `.g4`.

**tabla** — diccionario Python que almacena las variables declaradas con `var`.

| Método | Qué hace |
|---|---|
| `visitDeclaracionVar` | Guarda la variable en la tabla de símbolos |
| `visitVariable` | Busca la variable en la tabla, error si no existe |
| `visitSuma` | Evalúa `a + b` |
| `visitResta` | Evalúa `a - b` |
| `visitMultiplicacion` | Evalúa `a * b`, usa matmul si son matrices |
| `visitDivision` | Evalúa `a / b`, error si divisor es 0 |
| `visitPotencia` | Evalúa `a ^ b` |
| `visitModuloOp` | Evalúa `a mod b` |
| `visitSeno` | Evalúa `sen(x)` con math.sin |
| `visitCoseno` | Evalúa `cos(x)` con math.cos |
| `visitTangente` | Evalúa `tan(x)` con math.tan |
| `visitNumero` | Convierte el texto "10" al número 10.0 |
| `visitParentesis` | Evalúa la expresión dentro del paréntesis |
| `visitListaExpr` | Construye una lista Python |
| `visitMatrizExpr` | Construye un numpy array |
| `visitTransponerExpr` | Transpone una matriz con numpy |
| `visitInvertirExpr` | Invierte una matriz con numpy |
| `visitAjustarExpr` | Entrena un modelo de regresión lineal con scikit-learn |
| `visitClasificarExpr` | Entrena un modelo de regresión logística con scikit-learn |
| `visitPredecirExpr` | Predice valores con un modelo entrenado |
| `visitCoeficientesExpr` | Retorna pendiente e intercepto del modelo |
| `visitInstruccionPlot` | Grafica con matplotlib |
| `visitInstruccionRed` | Crea y entrena redes neuronales con keras/scikit-learn |
| `visitInstruccionIO` | Lee y escribe archivos |
| `visitCondicional` | Ejecuta bloque si/sino |
| `visitCondicion` | Evalúa comparación >, <, == |
| `visitCicloFor` | Ejecuta ciclo repite |
| `visitCicloWhile` | Ejecuta ciclo mientras |
| `visitImportacion` | Registra el módulo importado |

---

### main.py

Punto de entrada del programa.

**ErrorNeuralX** — manejador de errores de sintaxis. Captura errores de ANTLR y los muestra en español con línea y columna exacta.

**ejecutar(codigo, visitor)** — recibe un string de código NeuralX, lo procesa con el Lexer y Parser, y lo ejecuta con el Visitor.

**modo_archivo(ruta, visitor)** — lee un archivo `.nx` y lo ejecuta completo.

**modo_repl(visitor)** — inicia el loop interactivo. Detecta bloques `{ }` y espera a que estén completos antes de ejecutar.

## Autor 
Proyecto académico 
Construcción de DLS (Lenguaje de dominio especifico para realizar proceso de Deep Learning) 
Autores: 
Gabriela Delgado, Sergio Morales, Samuel Ramírez, Luisa Bautista
