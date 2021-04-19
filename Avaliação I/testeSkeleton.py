import sys

def inicio():
    print("""
    ---------------------------------------
             Teoria Grafos
    ---------------------------------------
        Esse programa cria grafos simples
        Sem laços ou arestas paralelas
    ---------------------------------------
        Digite o número equivalente 
        a opção desejada
    ---------------------------------------
    """)
    buffer = 4
    while((int(buffer)!=1) and (int(buffer)!=2) and (int(buffer)!=3)):
        print("""Suas arestas são valoradas?
        (1) SIM
        (2) NÃO
        (3) SAIR
        """)
        buffer = input("Opção: ")
        if buffer.strip().isdigit():
            if((int(buffer)!=1) and (int(buffer)!=2) and (int(buffer)!=3)):
                print("Opção inválida\n")
            else:
                pass
                #print("ok")
        else:
            print("Opção inválida\n")
            buffer = 4
    if int(buffer)==3:
        finalizar()
        return
    global valorado
    valorado = buffer
    buffer =4

    while((int(buffer)!=1) and (int(buffer)!=2) and (int(buffer)!=3)):
        print("""Suas arestas são direcionadas?
        (1) SIM
        (2) NÃO
        (3) SAIR
        """)
        buffer = input("Opção: ")
        if buffer.strip().isdigit():
            if((int(buffer)!=1) and (int(buffer)!=2) and (int(buffer)!=3)):
                print("Opção inválida\n")
            else:
                pass
                #print("ok")
        else:
            print("Opção inválida\n")
            buffer = 4
    if int(buffer)==3:
        finalizar()
        return
    global direcionado
    direcionado = buffer
    menu()
    return

def menu():

    while(True):
        print("""
        ---------------------------------------
                Teoria Grafos
        ---------------------------------------
        O que deseja fazer?
        1) Criar Vertice
        2) Criar Aresta
        3) Mostrar Informações do Grafo
        4) Mostrar Informações de Um Vértice
        5) Checar Adjacencia de Dois Vertices
        6) Sair    
        """)
        buffer = input("Opção: ")
        if buffer.strip().isdigit():
            switchMenu(int(buffer))
        else:
            print("Opção Inválida")


    return

def switchMenu(x):
    if(x==1):
        criarVertice()
    elif(x==2):
        criarAresta()
    elif(x==3):
        informacoesGrafo()
    elif(x==4):
        informacoesVertice()
    elif(x==5):
        adjacenciaCheck()
    elif(x==6):
        finalizar()
    else:
        print("Opção Inválida\n")

def criarVertice():
    print("criando Vertice")
    return

def criarAresta():
    print("criando Aresta")
    return

def informacoesGrafo():
    mostrarGrafo()
    ordemGrafo()
    tamanhoGrafo()
    return

def informacoesVertice():
    listaDeVerticesAdjacentes()
    grauDoVertice()
    return

def adjacenciaCheck():
    print("pedindo os dois vertices")
    print("dizendo se são adjacentes")
    return

def mostrarGrafo():
    print("mostrando Grafo")
    return

def listaDeVerticesAdjacentes():
    print("mostrando lista de vertices adjacentes")
    return

def grauDoVertice():
    print("pedindo vertice")
    print("mostrando grau do vertice")
    return

def ordemGrafo():
    print("mostrando ordem do grafo")
    return

def tamanhoGrafo():
    print("mostrando tamanho do Grafo")
    return

def finalizar():
    print("Adeus! o//")
    sys.exit()

    return
valorado = 0
direcionado = 0
sair = False
inicio()