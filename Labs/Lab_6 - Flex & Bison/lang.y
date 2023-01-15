%{
#include <stdio.h>
#include <stdlib.h>
#define YYDEBUG 1

%}

%token IN
%token OUT
%token INT
%token STRING
%token CHARACTER
%token IF
%token ELIF
%token WHILE
%token ELSE

%token ASSIGN
%token EQ
%token LT
%token LTE
%token GT
%token GTE
%token NE
%token AND
%token OR
%token NOT

%token IDENTIFIER
%token CONSTANT

%left '+' '-' '*' '/'

%token ADD 
%token SUB
%token DIV 
%token MOD 
%token MUL 

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET 
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET 


%token SEMI_COLON
%token COLON

%start program
%error-verbose

%%

program : block
		;
block : OPEN_CURLY_BRACKET stmt_list CLOSED_CURLY_BRACKET
		;
stmt_list : stmt | stmt stmt_list 
			   ;
stmt : simple_stmt | struct_stmt
		  ;	  
simple_stmt : decl_stmt SEMI_COLON | io_stmt SEMI_COLON | assign_stmt SEMI_COLON
				 ;
decl_stmt : IDENTIFIER COLON type
			;		
type : simple_type
	;
simple_type : INT | STRING | CHARACTER
			;
io_stmt : IN IDENTIFIER | OUT IDENTIFIER | OUT CONSTANT 
		;
assign_stmt : IDENTIFIER ASSIGN expression
				;
expression : expression ADD term | expression SUB term | term
		   ;
term : term MUL factor | term DIV factor | term MOD factor | factor
	 ;
factor : OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | IDENTIFIER | CONSTANT
	   ;
struct_stmt : if_stmt | while_stmt
		;
if_stmt : IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET block| IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET block ELSE block | IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET block elif_block ELSE block
		;
logic_op: AND | OR
		;
elif_block : ELIF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET block | ELIF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET block elif_block
		;
condition : expression relation expression | expression relation expression logic_op condition
		  ;
relation : EQ | NE | LT | LTE | GT | GTE
		 ;
while_stmt : WHILE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET block
		   ;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}

