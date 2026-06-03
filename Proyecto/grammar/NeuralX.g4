grammar NeuralX;

// ─────────────────────────────────────────────
//  REGLA DE INICIO
// ─────────────────────────────────────────────

prog: instruccion+ EOF ;

// ─────────────────────────────────────────────
//  INSTRUCCIONES
// ─────────────────────────────────────────────

instruccion
    : declaracionVar
    | declaracionFuncion
    | retorno
    | instruccionML
    | instruccionMatrix
    | instruccionPlot
    | instruccionRed
    | instruccionIO
    | condicional
    | cicloFor
    | cicloWhile
    | expresion
    ;

// ─────────────────────────────────────────────
//  VARIABLES
// ─────────────────────────────────────────────

declaracionVar
    : VAR IDENTIFICADOR ASIGNACION expresion ;

// ─────────────────────────────────────────────
//  FUNCIONES Y RECURSIVIDAD
// ─────────────────────────────────────────────

declaracionFuncion
    : FUNCION IDENTIFICADOR '(' parametros? ')' '{' instruccion+ '}' ;

parametros
    : IDENTIFICADOR (',' IDENTIFICADOR)* ;

llamadaFuncion
    : IDENTIFICADOR '(' argumentos? ')' ;

argumentos
    : expresion (',' expresion)* ;

retorno
    : RETORNAR expresion ;

// ─────────────────────────────────────────────
//  EXPRESIONES CON PRECEDENCIA
// ─────────────────────────────────────────────

expresion
    // ── Aritmética ──────────────────────────────────────────
    : expresion POTENCIA expresion                             #Potencia
    | expresion MULT expresion                                 #Multiplicacion
    | expresion DIV expresion                                  #Division
    | expresion SUMA expresion                                 #Suma
    | expresion RESTA expresion                                #Resta
    | expresion MODULO expresion                               #ModuloOp
    | RESTA expresion                                          #Negacion
    // ── Trigonometría ────────────────────────────────────────
    | SEN       '(' expresion ')'                              #Seno
    | COS       '(' expresion ')'                              #Coseno
    | TAN       '(' expresion ')'                              #Tangente
    | ASEN      '(' expresion ')'                              #ArcSeno
    | ACOS      '(' expresion ')'                              #ArcCoseno
    | ATAN      '(' expresion ')'                              #ArcTangente
    // ── Matemática general ───────────────────────────────────
    | LOG       '(' expresion ')'                              #Logaritmo
    | LOG10     '(' expresion ')'                              #Logaritmo10
    | RAIZ      '(' expresion ')'                              #RaizCuad
    | ABS       '(' expresion ')'                              #ValorAbsoluto
    | PISO      '(' expresion ')'                              #Piso
    | TECHO     '(' expresion ')'                              #Techo
    | REDONDEAR '(' expresion ')'                              #Redondear
    // ── Matrices ─────────────────────────────────────────────
    | TRANSPONER '(' expresion ')'                             #TransponerExpr
    | INVERTIR   '(' expresion ')'                             #InvertirExpr
    | DET        '(' expresion ')'                             #DetExpr
    | NORMA      '(' expresion ')'                             #NormaExpr
    | FORMA      '(' expresion ')'                             #FormaExpr
    | IDENTIDAD  '(' expresion ')'                             #IdentidadExpr
    | ZEROS      '(' expresion ',' expresion ')'               #CerosExpr
    // ── Estructuras de datos ─────────────────────────────────
    | LISTA_T    '(' ')'                                       #CrearLista
    | ARREGLO_T  '(' expresion ',' expresion ')'               #CrearArreglo
    | AGREGAR    '(' expresion ',' expresion ')'               #AgregarExpr
    | ELIMINAR   '(' expresion ',' expresion ')'               #EliminarExpr
    | OBTENER    '(' expresion ',' expresion ')'               #ObtenerExpr
    | LONGITUD   '(' expresion ')'                             #LongitudExpr
    | ORDENAR    '(' expresion ')'                             #OrdenarExpr
    | CONTIENE   '(' expresion ',' expresion ')'               #ContieneExpr
    | INDICE     '(' expresion ',' expresion ')'               #IndiceExpr
    | INVERTIR_L '(' expresion ')'                             #InvertirListaExpr
    // ── Archivos ─────────────────────────────────────────────
    | LEER_TODO    '(' expresion ')'                           #LeerTodoExpr
    | LEER_LINEA   '(' expresion ')'                           #LeerLineaExpr
    | LEER_CSV     '(' CADENA ')'                              #LeerCSVExpr
    | ESCRIBIR_CSV '(' CADENA ',' expresion ')'                #EscribirCSVExpr
    | EXISTE       '(' CADENA ')'                              #ExisteExpr
    | LINEAS       '(' expresion ')'                           #LineasExpr
    | COLUMNAS_CSV '(' expresion ')'                           #ColumnasCSVExpr
    | FILA_CSV     '(' expresion ',' expresion ')'             #FilaCSVExpr
    // ── Modelos ML ───────────────────────────────────────────
    | REGRESION_LINEAL '(' ')'                                 #CrearRegLineal
    | REGRESION_LOG    '(' ')'                                 #CrearRegLog
    | ENTRENAR_MOD '(' expresion ',' expresion ',' expresion ')' #EntrenarMod
    | PREDECIR_MOD '(' expresion ',' expresion ')'             #PredecirMod
    | EVALUAR      '(' expresion ',' expresion ',' expresion ')' #EvaluarMod
    | INTERCEPTO   '(' expresion ')'                           #InterceptoExpr
    | PRECISION    '(' expresion ')'                           #PrecisionExpr
    | ERROR_MOD    '(' expresion ')'                           #ErrorModExpr
    | COEFICIENTES '(' expresion ')'                           #CoeficientesExpr
    // ── MLP ──────────────────────────────────────────────────
    | MLP_T      '(' ')'                                       #CrearMLP
    | CAPA_DENSA '(' expresion ',' expresion ',' CADENA ')'    #AgregarCapa
    | COMPILAR   '(' expresion ',' expresion ',' expresion ',' CADENA ')' #CompilarMLP
    | PERDIDA    '(' expresion ')'                             #PerdidaExpr
    | HISTORIA   '(' expresion ')'                             #HistoriaExpr
    // ── RNA / Agrupamiento ────────────────────────────────────
    | KMEANS     '(' expresion ')'                             #CrearKMeans
    | DBSCAN_T   '(' expresion ',' expresion ')'               #CrearDBSCAN
    | RNA_CLAS   '(' ')'                                       #CrearRNAClas
    | RNA_PRED   '(' ')'                                       #CrearRNAPred
    | CENTROIDES '(' expresion ')'                             #CentroidesExpr
    | ETIQUETAS  '(' expresion ')'                             #EtiquetasExpr
    | INERCIA    '(' expresion ')'                             #InerciaExpr
    // ── ML legado ────────────────────────────────────────────
    | AJUSTAR    '(' expresion ',' expresion ')'               #AjustarExpr
    | CLASIFICAR '(' expresion ',' expresion ')'               #ClasificarExpr
    | PREDECIR   '(' expresion ',' expresion ')'               #PredecirExpr
    // ── Base ─────────────────────────────────────────────────
    | '(' expresion ')'                                        #Parentesis
    | llamadaFuncion                                           #LlamadaExpr
    | NUMERO                                                   #Numero
    | CADENA                                                   #CadenaExpr
    | VERDADERO                                                #Verdadero
    | FALSO                                                    #Falso
    | IDENTIFICADOR                                            #Variable
    | lista                                                    #ListaExpr
    | declaracionMatriz                                        #MatrizExpr
    ;

// ─────────────────────────────────────────────
//  LISTAS Y MATRICES
// ─────────────────────────────────────────────

lista : '[' (expresion (',' expresion)*)? ']' ;

declaracionMatriz
    : MAT '[' '[' listaNumeros ']' (',' '[' listaNumeros ']')* ']' ;

listaNumeros
    : NUMERO (',' NUMERO)* ;

// ─────────────────────────────────────────────
//  CONDICIONALES
// ─────────────────────────────────────────────

condicional
    : SI '(' condicion ')' '{' instruccion+ '}'
      (SINO SI '(' condicion ')' '{' instruccion+ '}')*
      (SINO '{' instruccion+ '}')? ;

condicion
    : expresion MAYOR expresion                                #CondMayor
    | expresion MENOR expresion                                #CondMenor
    | expresion IGUAL expresion                                #CondIgual
    | expresion DIFERENTE expresion                            #CondDiferente
    | expresion MAYORIGUAL expresion                           #CondMayorIgual
    | expresion MENORIGUAL expresion                           #CondMenorIgual
    | condicion Y condicion                                    #CondY
    | condicion O condicion                                    #CondO
    | NO condicion                                             #CondNo
    ;

// ─────────────────────────────────────────────
//  CICLOS
// ─────────────────────────────────────────────

cicloFor
    : REPITE IDENTIFICADOR EN '[' NUMERO '..' NUMERO ']' '{' instruccion+ '}'  #ForRango
    | REPITE IDENTIFICADOR EN expresion '{' instruccion+ '}'                    #ForLista
    ;

cicloWhile
    : MIENTRAS '(' condicion ')' '{' instruccion+ '}' ;

// ─────────────────────────────────────────────
//  MÓDULOS COMO SENTENCIAS
// ─────────────────────────────────────────────

instruccionML
    : AJUSTAR      '(' expresion ',' expresion ')'
    | CLASIFICAR   '(' expresion ',' expresion ')'
    | PREDECIR     '(' expresion ',' expresion ')'
    | COEFICIENTES '(' expresion ')'
    ;

instruccionMatrix
    : TRANSPONER '(' expresion ')'
    | INVERTIR   '(' expresion ')'
    ;

instruccionPlot
    : GRAFICAR   '(' expresion ',' expresion ')'
    | GRAFICAR   '(' expresion ',' expresion ',' CADENA ')'
    | DISPERSAR  '(' expresion ',' expresion ')'
    | DISPERSAR  '(' expresion ',' expresion ',' CADENA ')'
    | BARRAS     '(' expresion ',' expresion ')'
    | HISTOGRAMA '(' expresion ',' expresion ')'
    | TITULO     '(' CADENA ')'
    | EJEX       '(' CADENA ')'
    | EJEY       '(' CADENA ')'
    | ETIQUETA_P '(' CADENA ')'
    | LEYENDA    '(' ')'
    | CUADRICULA '(' ')'
    | RANGO_X    '(' expresion ',' expresion ')'
    | RANGO_Y    '(' expresion ',' expresion ')'
    | LIMPIAR    '(' ')'
    | GUARDAR_G  '(' CADENA ')'
    | MOSTRAR_P  '(' ')'
    ;

instruccionRed
    : RED        '(' CAPAS '=' '[' listaNumeros ']' ')'
    | PERCEPTRON '(' CAPAS '=' '[' listaNumeros ']' ')'
    | ENTRENAR   '(' expresion ',' expresion ',' expresion ')'
    ;

instruccionIO
    : ABRIR    '(' CADENA ',' CADENA ')'
    | CERRAR   '(' expresion ')'
    | ESCRIBIR '(' expresion ',' expresion ')'
    | GUARDAR  '(' CADENA ',' expresion ')'
    | MOSTRAR  '(' expresion ')'
    ;

// ─────────────────────────────────────────────
//  TOKENS — KEYWORDS CORE
// ─────────────────────────────────────────────

VAR          : 'var' ;
FUNCION      : 'funcion' ;
RETORNAR     : 'retornar' ;
SI           : 'si' ;
SINO         : 'sino' ;
REPITE       : 'repite' ;
EN           : 'en' ;
MIENTRAS     : 'mientras' ;
VERDADERO    : 'verdadero' ;
FALSO        : 'falso' ;
Y            : 'AND' ;
O            : 'OR' ;
NO           : 'NOT' ;
MAT          : 'mat' ;

// ─────────────────────────────────────────────
//  TOKENS — ARITMÉTICA
// ─────────────────────────────────────────────

SEN          : 'sen' ;
COS          : 'cos' ;
TAN          : 'tan' ;
ASEN         : 'asen' ;
ACOS         : 'acos' ;
ATAN         : 'atan' ;
LOG          : 'log' ;
LOG10        : 'log10' ;
RAIZ         : 'raiz' ;
ABS          : 'abs' ;
PISO         : 'piso' ;
TECHO        : 'techo' ;
REDONDEAR    : 'redondear' ;

// ─────────────────────────────────────────────
//  TOKENS — MATRICES
// ─────────────────────────────────────────────

TRANSPONER   : 'transponer' ;
INVERTIR     : 'invertir' ;
DET          : 'det' ;
NORMA        : 'norma' ;
FORMA        : 'forma' ;
IDENTIDAD    : 'identidad' ;
ZEROS        : 'ceros' ;

// ─────────────────────────────────────────────
//  TOKENS — ESTRUCTURAS
// ─────────────────────────────────────────────

LISTA_T      : 'Lista' ;
ARREGLO_T    : 'Arreglo' ;
AGREGAR      : 'agregar' ;
ELIMINAR     : 'eliminar' ;
OBTENER      : 'obtener' ;
LONGITUD     : 'longitud' ;
ORDENAR      : 'ordenar' ;
CONTIENE     : 'contiene' ;
INDICE       : 'indice' ;
INVERTIR_L   : 'invertirLista' ;

// ─────────────────────────────────────────────
//  TOKENS — PLOT
// ─────────────────────────────────────────────

GRAFICAR     : 'graficar' ;
DISPERSAR    : 'dispersar' ;
BARRAS       : 'barras' ;
HISTOGRAMA   : 'histograma' ;
TITULO       : 'titulo' ;
EJEX         : 'ejeX' ;
EJEY         : 'ejeY' ;
ETIQUETA_P   : 'etiqueta' ;
LEYENDA      : 'leyenda' ;
CUADRICULA   : 'cuadricula' ;
RANGO_X      : 'rangoX' ;
RANGO_Y      : 'rangoY' ;
LIMPIAR      : 'limpiar' ;
GUARDAR_G    : 'guardarGrafica' ;
MOSTRAR_P    : 'mostrarGrafica' ;

// ─────────────────────────────────────────────
//  TOKENS — IO
// ─────────────────────────────────────────────

ABRIR        : 'abrir' ;
GUARDAR      : 'guardar' ;
CERRAR       : 'cerrar' ;
ESCRIBIR     : 'escribir' ;
LEER_TODO    : 'leerTodo' ;
LEER_LINEA   : 'leerLinea' ;
LEER_CSV     : 'leerCSV' ;
ESCRIBIR_CSV : 'escribirCSV' ;
EXISTE       : 'existe' ;
LINEAS       : 'lineas' ;
COLUMNAS_CSV : 'columnasCSV' ;
FILA_CSV     : 'filaCSV' ;
MOSTRAR      : 'mostrar' ;

// ─────────────────────────────────────────────
//  TOKENS — ML / REGRESIÓN
// ─────────────────────────────────────────────

REGRESION_LINEAL : 'regresionLineal' ;
REGRESION_LOG    : 'regresionLogistica' ;
ENTRENAR_MOD     : 'entrenarModelo' ;
PREDECIR_MOD     : 'predecirModelo' ;
EVALUAR          : 'evaluar' ;
COEFICIENTES     : 'coeficientes' ;
INTERCEPTO       : 'intercepto' ;
PRECISION        : 'precision' ;
ERROR_MOD        : 'errorModelo' ;
AJUSTAR          : 'ajustar' ;
CLASIFICAR       : 'clasificar' ;
PREDECIR         : 'predecir' ;

// ─────────────────────────────────────────────
//  TOKENS — MLP
// ─────────────────────────────────────────────

MLP_T        : 'mlp' ;
CAPA_DENSA   : 'capaDensa' ;
COMPILAR     : 'compilar' ;
PERDIDA      : 'perdida' ;
HISTORIA     : 'historia' ;
RED          : 'red' ;
PERCEPTRON   : 'perceptron' ;
ENTRENAR     : 'entrenar' ;
CAPAS        : 'capas' ;

// ─────────────────────────────────────────────
//  TOKENS — RNA / AGRUPAMIENTO
// ─────────────────────────────────────────────

KMEANS       : 'kMeans' ;
DBSCAN_T     : 'dbscan' ;
RNA_CLAS     : 'rnaClas' ;
RNA_PRED     : 'rnaPred' ;
CENTROIDES   : 'centroides' ;
ETIQUETAS    : 'etiquetas' ;
INERCIA      : 'inercia' ;

// ─────────────────────────────────────────────
//  TOKENS — OPERADORES
// ─────────────────────────────────────────────

SUMA         : '+' ;
RESTA        : '-' ;
MULT         : '*' ;
DIV          : '/' ;
POTENCIA     : '^' ;
MODULO       : 'mod' ;
ASIGNACION   : '=' ;
MAYOR        : '>' ;
MENOR        : '<' ;
IGUAL        : '==' ;
DIFERENTE    : '!=' ;
MAYORIGUAL   : '>=' ;
MENORIGUAL   : '<=' ;

// ─────────────────────────────────────────────
//  TOKENS — LITERALES
// ─────────────────────────────────────────────

NUMERO        : [0-9]+ ('.' [0-9]+)? ;
CADENA        : '"' (~'"')* '"' ;
IDENTIFICADOR : [a-zA-Z_][a-zA-Z0-9_]* ;
WS            : [ \t\r\n]+ -> skip ;
COMENTARIO    : '//' ~[\r\n]* -> skip ;
