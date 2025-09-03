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

