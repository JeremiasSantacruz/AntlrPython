grammar tpi;
 /*========
  * Parser
  =========*/

/* PROGRAMA GENERAL        */

start                
	: programa NEWLINE? EOF
	;

programa             
	: ACCION IDENTIFICADOR ES NEWLINE ambiente proceso FINACCION 
	;

/* Definiciones del ambiente, se podria agregar soporte a otros tipos de datos*/
ambiente            
	: AMBIENTE NEWLINE+ lineaambiente? 
	;

lineaambiente       
	: variable
	| constante
	;

variable
	: IDENTIFICADOR  ':' TIPODEDATO NEWLINE+ lineaambiente? 
	;

constante
	:  IDENTIFICADOR '='  termino NEWLINE+ lineaambiente? 
	;

/* Comienzo de las lineas del programa*/
proceso               
	: PROCESO NEWLINE+ lineacod?
	;
/* Clasificamos las lineas en 4 grandes categorias*/
lineacod             
	: asignacion NEWLINE+ lineacod? 
	| funcion NEWLINE+ lineacod? 
	| sentencias NEWLINE+ lineacod?
	| asignacioninc NEWLINE+ lineacod?
	;

asignacion            
	: IDENTIFICADOR ASIGNACION expresion 
	;

asignacioninc 
	: IDENTIFICADOR ASGINACIONINC expresion
	;


sentencias          
	: condicional
	| iterativas
	;

condicional
	:SI expresion ENTONCES NEWLINE lineacod (SINO NEWLINE lineacod)? FINSI
	|SEGUN IDENTIFICADOR HACER NEWLINE lineasegun DEFECTO NEWLINE lineacod FINSEGUN
	;

iterativas
	: REPETIR NEWLINE lineacod HASTAQUE expresion
	| PARA asignacion HASTA termino ',' termino HACER NEWLINE lineacod FINPARA
	| MIENTRAS expresion HACER NEWLINE lineacod FINMIENTRAS
	;

lineasegun 
	: hoja ':' lineacod NEWLINE lineasegun 
	| hoja ':' lineacod 
	;
/*Se popdria agregar otras funciones  definidas por el usuario
 con IDENTIFICADORES */
funcion               
	: LEER PAR arg IPAR 
	| ESCRIBIR PAR arg IPAR
	;
/*Deberia ser una simple expresion wn vez de dato???*/
arg      
	: dato ','arg 
	| dato
	;

expresion
	: PAR expresion IPAR
	| siexpresion (operadorrelacional expresion)?
	;

siexpresion
	: factor (addoperador siexpresion)?
	;

factor
	: termino (multioperador factor)?;

termino               
	: ( MAS | MENOS )? hoja
	;

hoja
   : dato
   | PAR expresion IPAR
   | NOTL factor
   | BOOL
   ;

dato
	: numero
	| IDENTIFICADOR
	| TXT
	| BOOL
	;

operadorrelacional
    : IGUAL
   | DESIGUAL
   | MENORA
   | MAYORA
   | MENOROI
   | MAYOROI
   ;

addoperador
   : MAS
   | MENOS
   | OR
   ;

multioperador
   : MULTI
   | DIVENT
   | DIV
   | MOD
   | AND
   | POT
   ;

numero                
	: MENOS? REAL
	| MENOS? NUMEROENTERO
	;

/* ===============
FRAGMENT
==================*/


fragment A
   : ('a' | 'A')
   ;


fragment B
   : ('b' | 'B')
   ;


fragment C
   : ('c' | 'C')
   ;


fragment D
   : ('d' | 'D')
   ;


fragment E
   : ('e' | 'E')
   ;


fragment F
   : ('f' | 'F')
   ;


fragment G
   : ('g' | 'G')
   ;


fragment H
   : ('h' | 'H')
   ;


fragment I
   : ('i' | 'I')
   ;


fragment J
   : ('j' | 'J')
   ;


fragment K
   : ('k' | 'K')
   ;


fragment L
   : ('l' | 'L')
   ;


fragment M
   : ('m' | 'M')
   ;


fragment N
   : ('n' | 'N')
   ;


fragment O
   : ('o' | 'O')
   ;


fragment P
   : ('p' | 'P')
   ;


fragment Q
   : ('q' | 'Q')
   ;


fragment R
   : ('r' | 'R')
   ;


fragment S
   : ('s' | 'S')
   ;


fragment T
   : ('t' | 'T')
   ;


fragment U
   : ('u' | 'U')
   ;


fragment V
   : ('v' | 'V')
   ;


fragment W
   : ('w' | 'W')
   ;


fragment X
   : ('x' | 'X')
   ;


fragment Y
   : ('y' | 'Y')
   ;


fragment Z
   : ('z' | 'Z')
   ;




/*=========
  * Lexer
=========*/

/* Palabras reservadas sin destincion de mayusculas */
ACCION         : A C C I O N;
ES             : '_' E S;
FINACCION      : F I N '_' A C C I O N ;
AMBIENTE       : A M B I E N T E;
PROCESO        : P R O C E S O;
TIPODEDATO     : ( C A D E N A  | E N T E R O | R E A L | N U M E R O); 
MIENTRAS       : M I E N T R A S ;
HACER          : H A C E R ':';
FINMIENTRAS    : F I N '_' M I E N T R A S;
HASTAQUE       : H A S T A '_' Q U E ;
REPETIR        : R E P E T I R;
SI             : S I;
ENTONCES       : E N T O N C E S ;
SINO           : S I N O;
FINSI          : F I N '_' S I;
PARA           : P A R A;
HASTA          : H A S T A ':';
FINPARA        : F I N '_' P A R A ;
SEGUN          : S E G U N;
DEFECTO        : D E F E C T O ':';
FINSEGUN       : F I N '_' S E G U N;
CADENA         : C A D E N A ;
ESCRIBIR       : E S C R I B I R   ;
LEER           : L E E R;

/* Operadores y parentesis */
IGUAL          : '=';
DPUNTOS        : ':';
SEMI           : ';';
MENOS          : '-';
MAS            : '+';
OR             : '_'O ;
MULTI          : '*';
DIVENT         : '/';
DIV            : '_' D I V;
MOD            : '_'M O D;
AND            : '_' Y ;
POT            : '**' ;
NOTL           : '_no' ;
PAR            : '(' ;
IPAR           : ')' ;
DESIGUAL       : '<>';
MENORA         : '<';
MAYORA         : '>';
MENOROI        : '<=';
MAYOROI        : '>=';

COMA           : ( '.' | ',' );

/*Definicion de los numeros*/
NUMEROENTERO   : [0-9]+ ;
REAL           : [0-9]+ COMA [0.9]*;

ASIGNACION     : ':=' ;
ASGINACIONINC  : ( '-:=' | '+:= ');

BOOL           : ( 'TRUE' | 'FALSE' );

/*Expresion regular de identificadorses 
  Primera parte nos aseguramos que venga una letra
  Despues solamente tomamos un guion bajo y cualquier convinacion de caracteres*/
IDENTIFICADOR  : [a-zA-Z][a-zA-Z0-9]*('_'[a-zA-Z0-9]+)*;

/* Comenzamos con un " luego decimos que puede venir el conjunto (\")
 o cualquier otro caracter(.)*/
TXT            :  '"' ( '\\"' | . )*? '"' ;                

/*Saltea los espacios en blancos y las nuevas lineas pueden ser ; */
WHITESPACE     :  [ \t\r\n] -> skip ; 
NEWLINE        : ('\r'? '\n' | '\r' | ';')+ ;


/* COMENTARIOS */
COMENTARIO1 : '@' ( . )*? '\n' -> skip;
COMENTARIO2 : '#' (.)*? '#' -> skip;