import sys
import ply.lex as lex
#from graphviz import Digraph
from collections import defaultdict

tokens = (

    #<?PHP, ?>
    'OPENTAG',
    'CLOSETAG',

    #Palabras reservadas
    '__HALT_COMPILER',
    'ABSTRACT',
    'AND',
    'ARRAY',
    'AS',
    'BREAK',
    'CALLABLE',
    'CASE',
    'CATCH',
    'CLASS',
    'CLONE',
    'CONST',
    'CONTINUE',
    'DECLARE',
    'DEFAULT',
    'DIE',
    'DO',
    'ECHO',
    'ELSE',
    'ELSEIF',
    'EMPTY',
    'ENDDECLARE',
    'ENDFOR',
    'ENDFOREACH',
    'ENDIF',
    'ENDSWITCH',
    'ENDWHILE',
    'EVAL',
    'EXIT',
    'EXTENDS',
    'CLOSETAGAL',
    'FOR',
    'FOREACH',
    'FUNCTION',
    'GLOBAL',
    'GOTO',
    'IF',
    'IMPLEMENTS',
    'INCLUDE',
    'INCLUDE_ONCE',
    'INSTANCEOF',
    'INSTEADOF',
    'INTERFACE',
    'ISSET',
    'LIST',
    'NAMESPACE',
    'NEW',
    'OR',
    'PRINT',
    'PRIVATE',
    'PROTECTED',
    'PUBLIC',
    'REQUIRE',
    'REQUIRE_ONCE',
    'RETURN',
    'STATIC',
    'SWITCH',
    'THROW',
    'TRAIT',
    'TRY',
    'UNSET',
    'USE',
    'VAR',
    'WHILE',
    'XOR',

    #Valores booleanos
    'TRUE',
    'FALSE',

    #Simbolos
    'PLUS',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'TIMESTIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMI',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'QUOTES',
    'APOSTROPHE',
    'DOT_DOT',

    #Otros
    'COMMENTS',
    'COMMENTS_C99',
    'ID',
    'IDVAR',
    'NUM',
    'STRING',
    'VOID',
)

t_ignore = " \t"
#Simbolos-------------------------------------------------------------
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUAL     = r'='
t_DISTINT   = r'!'
t_LESS      = r'<'
t_GREATER   = r'>'
t_SEMI      = r';'
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBLOCK    = r'{'
t_RBLOCK    = r'}'
t_COLON     = r':'
t_AMPERSANT = r'\&'
t_HASHTAG   = r'\#'
t_DOT       = r'\.'
t_QUOTES    = r'\"'
t_APOSTROPHE = r'\''


def t_VOID(t):
    r'VOID|void'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    #print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

#<?PHP, ?>
def t_OPENTAG(t):
    r'(<\?(php)?)'
    return t

def t_CLOSETAG(t):
    r'\?>'
    return t


#Palabras reservadas-------------------------------------------------------------
def t___HALT_COMPILER(t):
    r'__halt_compiler'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_AND(t):
    r'and|AND|\&\&'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CALLABLE(t):
    r'callable'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CLONE(t):
    r'clone'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DIE(t):
    r'die'
    return t

def t_DO(t):
    r'do'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_ENDDECLARE(t):
    r'enddeclare'
    return t

def t_ENDFOR(t):
    r'endfor'
    return t

def t_ENDFOREACH(t):
    r'endforeach'
    return t

def t_ENDIF(t):
    r'endif'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_ENDWHILE(t):
    r'endwhile'
    return t

def t_EVAL(t):
    r'eval'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_CLOSETAGAL(t):
    r'CLOSETAGal'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INCLUDE_ONCE(t):
    r'include_once'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_INSTEADOF(t):
    r'insteadof'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_ISSET(t):
    r'isset'
    return t

def t_LIST(t):
    r'list'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_NEW(t):
    r'new'
    return t

def t_OR(t):
    r'or|\|\||OR'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_TRAIT(t):
    r'trait'
    return t

def t_TRY(t):
    r'try'
    return t

def t_UNSET(t):
    r'unset'
    return t

def t_USE(t):
    r'use'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_XOR(t):
    r'xor'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

#Simbolos-------------------------------------------------------------

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_MINUSMINUS(t):
    r'--'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_TIMESTIMES(t):
    r'\*\*'
    return t

def t_DOT_DOT(t):
    r'::'
    return t


#Otros

def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1

def t_IDVAR(t):
    r'\$\w+(\d\w)*'
    return t

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(\w\d)*'
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t


def test(data, lexer):
    lexer.input(data)
    nivel=0
    while True:
        tok = lexer.token()
        if not tok:
            break
        nivel = grafo(tok, nivel)
        #print (tok.value)

pilapila=[]
lexer = lex.lex()


def grafo(token, nivel):
    n=nivel
    if token.value=="if":
        pilapila.append([nivel,"if"])
        nivel+=1
    if token.value=="else":
        pilapila.append([nivel,"else"])
        nivel+=1
    if token.value=="}":
        nivel-=1
    if token.value=="while" or token.value=="for":
        pilapila.append([nivel,"while"])
        nivel+=1
    return nivel

def nodos():
    numero=1
    nombres=[]
    for elemento in pilapila:
        if elemento[1]=="if":
            nombres.append("if"+str(numero)+str(elemento[0]))
            nombres.append("Final-f"+str(numero+2)+str(elemento[0]))
            nombres.append("Contenido-fc"+str(numero+1)+str(elemento[0]+1))
            numero+=3
        if elemento[1]=="else":
            nombres.append("else"+str(numero)+str(elemento[0]))
            nombres.append("Contenido-els"+str(numero+1)+str(elemento[0]+1))
            numero+=2
        if elemento[1]=="while":
            nombres.append("while"+str(numero)+str(elemento[0]))
            nombres.append("Final-wh"+str(numero+2)+str(elemento[0]))
            nombres.append("Contenido-whc"+str(numero+1)+str(elemento[0]+1))
            numero+=3
    return nombres

def buscarif(lista, nivel, destino):
    origen="0"
    for nodo in lista:
        if (nodo.find("Final")>=0 or nodo.find("Contenido-")>=0) and nodo[-1]==nivel:
            origen=nodo
    return origen+" -> "+destino

def buscarelse(lista, nivel, destino):
    origen="0"
    for nodo in lista:
        if nodo.find("if")>=0 and nodo[-1]==nivel:
            origen=nodo
    return origen+" -> "+destino

def buscarcif(lista, nivel, destino):
    origen="0"
    for nodo in lista:
        if nodo.find("if")>=0 and nodo[-1]==str(int(nivel)-1):
            origen=nodo
    return origen+" -> "+destino

def buscarcelse(lista, nivel, destino):
    origen="0"
    for nodo in lista:
        if nodo.find("else")>=0 and nodo[-1]==str(int(nivel)-1):
            origen=nodo
    return origen+" -> "+destino

def buscarcwh(lista, nivel, destino):
    origen="0"
    for nodo in lista:
        if nodo.find("while")>=0 and nodo[-1]==str(int(nivel)-1):
            origen=nodo
    return origen+" -> "+destino

def buscarfwh(lista, nivel, destino):
    origen="0"
    for nodo in lista:
        if nodo.find("while")>=0 and nodo[-1]==nivel:
            origen=nodo
    return origen+" -> "+destino

def buscarfifi(lista, nivel, destino):
    origen="0"
    t=1
    for nodo in lista:
        if nodo[-1]>nivel:
            if str(int(nivel)+1)==nodo[-1] and (nodo.find("Final")>=0 or t==1):
                origen=nodo
                if nodo.find("Final")>=0:
                    t=0
        else:
            break
    return origen+" -> "+destino

def buscarfife(lista, nivel, destino):
    origen="0"
    t=1
    s=1
    for nodo in lista:
        #print(destino, nodo)
        if nodo[-1]>nivel and t==0 and (s==1 or nodo.find("Final")>=0):
            if str(int(nivel)+1)==nodo[-1]:
                origen=nodo
            if nodo.find("Final")>=0:
                s=0
        if nodo[-1]==nivel and t==0:
            break
        if nodo[-1]==nivel and nodo.find("else")>=0:
            t=0
        if t!=0 and nodo[-1]==nivel:
            break

    if origen!="0":
        return origen+" -> "+destino
    else:
        return ""

def relaciones(nombres):
    relacion=[]
    for i in range(len(nombres)):
        if nombres[i].find("if")>=0:
            relacion.append(buscarif(nombres[0:i], nombres[i][-1],nombres[i]))
        if nombres[i].find("else")>=0:
            relacion.append(buscarelse(nombres[0:i], nombres[i][-1],nombres[i]))
        if nombres[i].find("Contenido-fc")>=0:
            relacion.append(buscarcif(nombres[0:i], nombres[i][-1],nombres[i]))
        if nombres[i].find("Contenido-els")>=0:
            relacion.append(buscarcelse(nombres[0:i], nombres[i][-1],nombres[i]))
        if nombres[i].find("Contenido-whc")>=0:
            relacion.append(buscarcwh(nombres[0:i], nombres[i][-1],nombres[i]))
        if nombres[i].find("Final-wh")>=0:
            relacion.append(buscarfwh(nombres[0:i], nombres[i][-1],nombres[i]))
        if nombres[i].find("Final-f")>=0:
            relacion.append(buscarfifi(nombres[i+1:len(nombres)], nombres[i][-1],nombres[i]))
            re=buscarfife(nombres[i+1:len(nombres)], nombres[i][-1],nombres[i])
            if re!="":
                relacion.append(re)
            else:
                relacion.append(buscarcif(nombres[0:i], str(int(nombres[i][-1])+1),nombres[i]))
        if nombres[i].find("while")>=0:
            relacion.append(buscarif(nombres[0:i], nombres[i+1][-1],nombres[i]))
            relacion.append(buscarfifi(nombres[i+2:len(nombres)], nombres[i][-1],nombres[i]))
    return(relacion)


# Python program to print all paths from a source to destination.
#This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self,vertices):
        #No. of vertices
        self.V= vertices
        self.especiales=[]
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def banderaActiva(self, vertices):
        if vertices.find("while") >= 0:
            return True

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        if self.especiales[u] == 1:
            visited[u] = False
        else:
            visited[u]= True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u ==d:
            print (path)
        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]==False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False


    # Prints all paths from 's' to 'd'
    def printAllPaths(self,s, d):

        # Mark all the vertices as not visited
        visited =[False]*(self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

#This code is contributed by Neelam Yadav

def buscarfinal(nodos):
    final=0
    for m in nodos:
        m = m.replace('f', '')
        m = m.replace('wh', '')
        if m!="0" and m[1]=="0":
            final=int(m[0])
    return final

 #Funcion principal del sistema
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'ejemplo.py'
    f = open(fin, 'r')
    data = f.read()
    test(data, lexer)
    nodosAux=nodos()
    #grafico = Digraph(comment = "Diagrama de flujo")
    '''
    for m in nodosAux:
        m = m.replace('Contenido-', '')
        m = m.replace('Final-', '')
        #print(m)
    for m in nodosAux:
        grafico.node(m)
    '''
    nodos=nodos()
    resultado=relaciones(nodos)

    #print(nodosAux)
    #print(nodos())

    listaRelaciones = []
    listaNodos = ["0"]

    for m in nodos:
        m = m.replace('Contenido-', '')
        m = m.replace('Final-', '')
        listaNodos.append(m)
        #grafico.node(m)

    # Create a graph given in the above diagram
    g = Graph(len(listaNodos))
    g.especiales.append(0)
    for n in nodos:
        if n.find("while") >= 0:
            g.especiales.append(1)
        else:
            g.especiales.append(0)
    print ("Lista banderas: "+str(g.especiales))

    for m in resultado:
        m = m.replace('Contenido-fc', '')
        m = m.replace('Final-f', '')
        m = m.replace('else', '')
        m = m.replace('if', '')
        m = m.replace('Contenido-els', '')
        m = m.replace('while', '')
        m = m.replace('Final-wh', '')
        m = m.replace('Contenido-whc', '')
        listaRelaciones.append(m)
        t = m.split(" -> ")
        g.addEdge(int(t[0][0]), int(t[1][0]))
        print("{} -> {}".format(t[0][0], t[1][0]))
        #grafico.edge(t[0], t[1])

    #print (grafico.source)
    print(len(listaRelaciones), len(listaNodos))
    print ("Complejidad = "+str(len(listaRelaciones)- len(listaNodos) + 2))
    s = 0 ; d = buscarfinal(listaNodos)
    print ("Siguiendo todos los caminos diferentes de %d a %d :" %(s, d))
    g.printAllPaths(s, d)

    #grafico.render('Grafico/flujo.pdf', view=True)