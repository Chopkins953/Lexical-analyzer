import ply.lex as lex
# List of token names
tokens = (
   'COMMENT',
   'SYMBOL',
   'KEYWORD',
   'INTEGERCONSTANT',
   'STRINGCONSTANT',
   'BOOLEANCONSTANT',
   'IDENTITFIER',
)
 
# Regular expression rules for tokens
t_ignore_COMMENT = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
t_SYMBOL   = r'(\(|\)|\[|\]|{|}|,|;|=|\.|\+|-|\*|&|\||~|<|>)'
t_INTEGERCONSTANT  = r'[0-9]+'
t_STRINGCONSTANT  = r'".*"'
t_BOOLEANCONSTANT  = r'true|false'

def t_KEYWORD(t):
     r'(class|constructor|method|function|int|boolean|char|void|var|static|field|let|do|if|else|while|return|null|this)'
     return t

# if the identifier matches the booleans set type to boolean constant
def t_IDENTITFIER(t):
     r'(_|[a-z]|[A-Z])(_|[a-z]|[A-Z])*'
     if t.value == "true" or t.value == "false":
          t.type = 'BOOLEANCONSTANT'  
     return t
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t \n'
 
# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

#test data
#data = ' /**THIRD \n*COMMENT TEST */ this is another test of the tokenizer while true "String constant test" asfd 1234.0987 *- +- + /*SECOND COMMENT TEST*/// commemt test + _/ -*/+*/\n'

print('Please enter file path: ')
file_path = input();

file = open(file_path,'r')

# Give the lexer some input
lexer.input(file.read())
 
# Tokenize
print('<tokens>\n')
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print('<'+tok.type+'>', tok.value,'</'+ tok.type+ '>') 
print('\n</tokens>\n')

input()
