NeuralX Language 

Learning, desarrollado con ANTLR4 y Python. 
Este proyecto fue realizado con fines académicos para poder entender y practicar con la construcción de los lenguajes. 

## 1. Estructura del proyecto 
Neuralx
1.	Nueralx.g4 
2.	NeutralXVisitorImpl.py 
3.	main.py 
4.	README
## 1.1 Descripción de cada documento 
NeuralX.g4 
Este archivo contiene la gramática en donde se define las reglas léxicas y sintácticas. 
NeuralXVisitorImpl.py 
Este archivo implementa la lógica del lenguaje usando Visitor. 
main.py 
Este es el archivo principal que ejecuta el parser y el Visitor. 
README
Escrito con la explicación del proyecto.
## 2. Lógica del lenguaje
NeutralX fue diseñado para interpretar instrucciones relacionadas con operación de Deep Learning en donde se divide en: 

## 2.1 Léxico 
Aquí se definen: 
•	Palabras reservadas 
•	Identificadores 
•	Numeros 
•	Simbolos
Ejemplo: 
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
## 2.2 Sintaxis 
Se define las reglas del lenguaje. 
Ejemplo:
program
: statement+ ;

statement
: assign
| print
;

assign
: ID '=' NUM ;

print
: 'print' ID ;

Esto indica que el lenguaje permite:

- Asignar valores
- Imprimir valores
## 2.3 Visitor 
Aquí de define la lógica de ejecución. 
Ejemplo: 
•	Guardar variables
•	Imprimir resultados 
•	Ejecutar instrucciones 
Ejemplo:
Usar un diccionario para almacenar valores. 
self.memory = {}

Cuando se asigna:

x = 5

Se guarda:

memory["x"] = 5

Cuando se imprime:

print x

Se busca en memoria y se muestra.
## 2.4 Programa principal (main) 
Este archivo: 
•	Lee el código fuente
•	Ejecuta el lexer 
•	Ejecuta el parser 
•	Ejecuta el visitor
Input → Lexer → Parser → Tree → Visitor → Resultado
## 3 Compilación por consola
•	Primero se genera el parser usando ANTLR.
•	En la terminal, dentro de la carpeta del proyecto antlr4 -Dlanguage=Python3 NeuralX.g4
•	Esto genera: 
NeuralXLexer.py 
NeuralXParser.py 
NeuralXVisitor.py
## 4 Ejecutar el programa
Ejecutar Python3 main.py, ejecutando el intérprete del lenguaje. 
## 5. USO 
Ejemplo: 
x = 10 
y = 100 
print x 
print y 
Salida esperada: 
10 
20 
## 6. Explicación del funcionamiento 
Este proceso simula el funcionamiento del compilador.
•	El código se lee desde consola o archivo. 
•	ANTLR analiza la gramática. 
•	Se genera el árbol sintáctico. 
•	El visitor recorre el árbol. 
•	Se ejecutan las instrucciones. 
## 7. Conceptos 
•	ANTLR4
•	Parser 
•	Lexer
•	Visitor 
•	Árbol sintáctico 
•	Deep Learning 
## 8. Autor 
Proyecto académico 
Construcción de DLS (Lenguaje de dominio especifico para realizar proceso de Deep Learning) 
Autores: 
Gabriela Delgado, Sergio Morales, Samuel Ramírez, Luisa Bautista
