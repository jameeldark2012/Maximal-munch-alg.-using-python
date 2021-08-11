import ply.lex as lex


#Defining tokens names

tokens = ('tokenDO', 'tokenDOUBLE','tokenalphabets')


#Defining regular expressions for tokens

def t_tokenDOUBLE(t):
    r'DOUBLE|double'
    return t

def t_tokenDO(t):
    r'DO|do'
    return t


# This accepts all alphabets
def t_tokenalphabets(t):
    r'[a-zA-Z]'
    return t


lexer = lex.lex()


print("Please enter the input string ")
input_string=input()

input_string=input_string.upper()

print("Matching the following string : "+input_string)

lexer.input(input_string)

for token in lexer:
    print(token.value ,"matches with ",token.type,"at position",token.lexpos)

