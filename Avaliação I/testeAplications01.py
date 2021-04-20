import sys
class Aresta:
    
    def __init__(self,v1,v2,value,name):
        self.vertice1 = v1
        self.vertice2 =v2
        self.value = value
        self.nome = name

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
    valorado = int(buffer)
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
    direcionado = int(buffer)
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
            print("""Opção Inválida,
            digite um numero entre as opções""")


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
        print("""Opção Inválida,
        digite um numero entre as opções""")

def criarVertice():
    print("""Criando Vértice
    Vértices atuais: """)
    for j in range(0,len(listaVertices),1):
        print(listaVertices[j])
    print("Digite um novo nome de vertice: ")
    vertice = ""
    while(vertice==""):
        vertice = input()
    global listaVertice
    if(vertice in listaVertices):
        print("Vértice já existe")
    else:
        listaVertices.append(vertice)
    return

def criarAresta():
    while(True):
        print("""Você irá escolher dois vertices
        para criar a aresta""")
        listaDeVerticesAdjacentes()
        buffer1 = input("Digite o vertice de partida: ")
        if (buffer1 in listaVertices):
            break
        else:
            print("""Nome Inadequado
            Digite o nome de um vértice""")
    while(True):
        listaDeVerticesAdjacentes()
        buffer2 = input("Digite o vertice de chegada: ")
        if(buffer1 != buffer2):
            if (buffer2 in listaVertices):
                break
            else:
                print("""Nome Inadequado
                Digite o nome de um vértice""")
        else:
            print("Vértices devem ser diferentes")
    for j in range (0,len(listaArestas),1):
        print("Checando se vertices ligadas")
        if(direcionado==1):
            if((listaArestas[j].vertice1 == buffer1) and (listaArestas[j].vertice2 == buffer2)):
                print("aresta já existe")
                return
        elif(((listaArestas[j].vertice1 == buffer1) and (listaArestas[j].vertice2 == buffer2))or ((listaArestas.vertice2[j] == buffer1) and (listaArestas[j].vertice1 == buffer2))):
            print("aresta já existe")
    print("""Escolha um nome novo para a aresta
    Arestas atuais: """)
    bufferName = ""
    for j in range (0,len(listaArestas),1):
        print(listaArestas[j].nome)
    print("Digite um novo nome de aresta")
    while(bufferName==""):
        bufferName = input()
        for j in range (0,len(listaArestas),1):
            if (bufferName == listaArestas[j].nome):
                print("Aresta com esse nome ja existe")
                buffer = ""
    if(valorado == 1):
        while(True):
            print("Escolha um valor para a aresta: ")
            bufferValue = input()
            if bufferValue.strip().isdigit():
                if(float(bufferValue)>0):
                    break
                else:
                    print("""Valor da aresta inválido
                    Valor deve ser maior que zero""")
            else:
                print("""Opção Inválida,
                digite um numero para o valor""")
    else:
        bufferValue = -1
    listaArestas.append(Aresta(buffer1,buffer2,int(bufferValue),bufferName))
    print("""Aresta Criada""")
    print("nome: ",listaArestas[0].nome ,"\nv1: ", listaArestas[0].vertice1 ,"\nv2", listaArestas[0].vertice2 ,"value", listaArestas[0].value)



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
    for j in range(0,len(listaVertices),1):
        print(listaVertices[j]+" ")
    print("mostrando lista de vertices")
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
listaVertices = []
listaArestas = []
sair = False
inicio()