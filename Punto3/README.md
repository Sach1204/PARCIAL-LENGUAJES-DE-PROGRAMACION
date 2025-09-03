**PUNTO 3**

Escriba un programa en C que implemente una calculadora que pueda sacar raíz cuadrada de números reales. Use flex y Bison. La entrada debe ser por un archivo de texto y la 
salida debe ser por consola.


**Codigo para la Calculador en Lex (Calc.l)**
```lex
%{
#include "calc.tab.h"
%}

%%

[0-9]+(\.[0-9]+)?    { yylval.f = atof(yytext); return NUM; }
"sqrt"               { return SQRT; }
\n                   { return EOL; }
[ \t]                ;   /* ignorar espacios */
.                    { return yytext[0]; }

%%



```
**Codigo para la Calculador en Bison (Calc.y)**
```bison
%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
%}

%union {
    double f;
}

%token <f> NUM
%token SQRT
%token EOL
%type <f> expr

%%

input:
    /* vacío */
    | input line
    ;

line:
    expr EOL   { printf("Resultado: %f\n", $1); }
    ;

expr:
    NUM                 { $$ = $1; }
    | SQRT expr         { $$ = sqrt($2); }
    | expr '+' expr     { $$ = $1 + $3; }
    | expr '-' expr     { $$ = $1 - $3; }
    | expr '*' expr     { $$ = $1 * $3; }
    | expr '/' expr     { 
                            if ($3 == 0) { 
                                printf("Error: División por cero\n"); 
                                $$ = 0; 
                            } else { 
                                $$ = $1 / $3; 
                            }
                        }
    | '(' expr ')'      { $$ = $2; }
    ;

%%

int main(void) {
    return yyparse();
}

int yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}


```
**TXT que recibe los datos para hacer la operacion(entrada.txt)**
```txt
2+3
10-4
6*7
8/2
sqrt 9
sqrt 25
(5+3)*2


```
**Como se compila y se ve desde terminal los resultados**
<img width="1856" height="391" alt="image" src="https://github.com/user-attachments/assets/65bdfb32-2dfe-4c9e-b511-27d64a2693a4" />


