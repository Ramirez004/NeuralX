grammar NeuralX;

// Regla de inicio
prog: instruccion+ EOF ;

instruccion
    : declaracionVar
    | instruccionML
    | instruccionMatrix
    | instruccionPlot
    | instruccionRed
    | instruccionIO
    | importacion
    | condicional
    | cicloFor
    | cicloWhile
    | expresion
    ;

// Variables
declaracionVar
    : VAR IDENTIFICADOR ASIGNACION expresion ;

// Importaciones
importacion
    : IMPORT modulo ;

modulo
    : 'NeuralX.Math'
    | 'NeuralX.Matrix'
    | 'NeuralX.Plot'
    | 'NeuralX.ML'
    | 'NeuralX.Net'
    | 'NeuralX.IO'
    ;

// Expresiones — ML incluido para poder hacer var modelo = ajustar(x, y)
expresion
    : expresion POTENCIA expresion                         #Potencia
    | expresion MULT expresion                             #Multiplicacion
    | expresion DIV expresion                              #Division
    | expresion SUMA expresion                             #Suma
    | expresion RESTA expresion                            #Resta
    | expresion MODULO expresion                           #ModuloOp
    | SEN '(' expresion ')'                                #Seno
    | COS '(' expresion ')'                                #Coseno
    | TAN '(' expresion ')'                                #Tangente
    | '(' expresion ')'                                    #Parentesis
    | TRANSPONER '(' expresion ')'                         #TransponerExpr
    | INVERTIR '(' expresion ')'                           #InvertirExpr
    | AJUSTAR '(' expresion ',' expresion ')'              #AjustarExpr
    | CLASIFICAR '(' expresion ',' expresion ')'           #ClasificarExpr
    | PREDECIR '(' expresion ',' expresion ')'             #PredecirExpr
    | COEFICIENTES '(' expresion ')'                       #CoeficientesExpr
    | NUMERO                                               #Numero
    | IDENTIFICADOR                                        #Variable
    | lista                                                #ListaExpr
    | declaracionMatriz                                    #MatrizExpr
    ;

// Listas
lista : '[' (expresion (',' expresion)*)? ']' ;

// Matrices
declaracionMatriz
    : MAT '[' '[' listaNumeros ']' (',' '[' listaNumeros ']')* ']' ;

listaNumeros
    : NUMERO (',' NUMERO)* ;

// Condicionales
condicional
    : SI '(' condicion ')' '{' instruccion+ '}'
      (SINO '{' instruccion+ '}')? ;

condicion
    : expresion MAYOR expresion
    | expresion MENOR expresion
    | expresion IGUAL expresion
    ;

// Ciclos
cicloFor
    : REPITE IDENTIFICADOR EN '[' NUMERO '..' NUMERO ']' '{' instruccion+ '}' ;

cicloWhile
    : MIENTRAS '(' condicion ')' '{' instruccion+ '}' ;

// ML — como instruccion standalone (sin asignacion)
instruccionML
    : AJUSTAR '(' expresion ',' expresion ')'
    | CLASIFICAR '(' expresion ',' expresion ')'
    | PREDECIR '(' expresion ',' expresion ')'
    | COEFICIENTES '(' expresion ')'
    ;

// Matrices — como instruccion standalone
instruccionMatrix
    : TRANSPONER '(' expresion ')'
    | INVERTIR '(' expresion ')'
    ;

// Plot
instruccionPlot
    : GRAFICAR '(' expresion ',' expresion ')'
    | DISPERSAR '(' expresion ',' expresion ')'
    | TITULO '(' CADENA ')'
    | EJEX '(' CADENA ')'
    | EJEY '(' CADENA ')'
    | MOSTRAR '(' ')'
    ;

// Redes
instruccionRed
    : RED '(' CAPAS '=' '[' listaNumeros ']' ')'
    | PERCEPTRON '(' CAPAS '=' '[' listaNumeros ']' ')'
    | ENTRENAR '(' expresion ',' expresion ',' expresion ')'
    ;

// IO
instruccionIO
    : ABRIR '(' CADENA ')'
    | GUARDAR '(' CADENA ',' expresion ')'
    | MOSTRAR '(' expresion ')'
    ;

// --- TOKENS ---
VAR          : 'var' ;
IMPORT       : 'import' ;
SI           : 'si' ;
SINO         : 'sino' ;
REPITE       : 'repite' ;
EN           : 'en' ;
MIENTRAS     : 'mientras' ;
MAT          : 'mat' ;
TRANSPONER   : 'transponer' ;
INVERTIR     : 'invertir' ;
AJUSTAR      : 'ajustar' ;
CLASIFICAR   : 'clasificar' ;
PREDECIR     : 'predecir' ;
COEFICIENTES : 'coeficientes' ;
GRAFICAR     : 'graficar' ;
DISPERSAR    : 'dispersar' ;
TITULO       : 'titulo' ;
EJEX         : 'ejeX' ;
EJEY         : 'ejeY' ;
MOSTRAR      : 'mostrar' ;
RED          : 'red' ;
PERCEPTRON   : 'perceptron' ;
ENTRENAR     : 'entrenar' ;
CAPAS        : 'capas' ;
ABRIR        : 'abrir' ;
GUARDAR      : 'guardar' ;
SEN          : 'sen' ;
COS          : 'cos' ;
TAN          : 'tan' ;

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

NUMERO       : [0-9]+ ('.' [0-9]+)? ;
CADENA       : '"' (~'"')* '"' ;
IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]* ;
WS           : [ \t\r\n]+ -> skip ;
