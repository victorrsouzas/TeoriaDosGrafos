import time
import networkx as nx
import matplotlib.pyplot as plt

buffer = 0
d = 1
e = 1
G = nx.DiGraph()  # Direcionado
G2 = nx.Graph()  # Não Direcionado
contaAresta = 0
lista = []
lista2 = []

def menu_Grafos():
    print("""
    -----------------------------
             Teoria Grafos
    -----------------------------
    """)
    time.sleep(1)
    while d == 1:
        print("""
    -----------------------------
      SISTEMA GRAFOS
    -----------------------------
        VOCÊ DESEJA INICIAR UM GRAFO?
        - SIM
        - NÃO
    -----------------------------""")
        a = input("\nOpção: ").upper()
        print("\n")
        if a == "SIM":
            grafos()
        elif a == "NÃO" or a == "NAO":
            break
        else:
            print("\nRESPONDA APENAS SIM OU NÃO")

def menu_Tipo_Grafo():
    print("    ------ADICIONAR GRAFO------")
    print("""
    Escolha a opção do grafo:
    (1) Direcionado
    (2) Não Direcionado
    (3) Sair
    """)

def menu_Tipo():
    print("""
    (1) Valorado
    (2) Não Valorado
    (3) Sair
        """)

def grafos():

    while d == 1:
        menu_Tipo_Grafo()
        try:
            buffer = int(input("Opção: "))
            # FOR DIRECIONADO
            if buffer == 1:
                menu_Tipo()
                peso = int(input("O seu grafo direcionado vai ser:"))
                # FOR DIRECIONADO E VALORADO
                if peso == 1:
                    opcoes(peso, buffer)

                # FOR DIRECIONADO E NÃO VALORADO
                elif peso == 2:
                    opcoes(peso, buffer)

                # SAIR DA OPÇÃO DIRECIONADO: VALORADO OU NÃO VALORADO
                elif peso == 3:
                    grafos()

            # FOR NÃO DIRECIONADO
            elif buffer == 2:
                menu_Tipo()
                peso = int(
                    input("O seu grafo não direcionado vai ser: "))
                # FOR NÃO DIRECIONADO E VALORADO
                if peso == 1:
                    opcoes(peso, buffer)

                # FOR NÃO DIRECIONADO E NÃO VALORADO
                elif peso == 2:
                    opcoes(peso, buffer)
                # SAIR
                elif peso == 3:
                    grafos()
            elif buffer == 3:
                break
        except ValueError:
            print(f"Erro no tipo da entrada {ValueError}")

        break

def menu_Opcoes(peso, buffer):
    global opcao
    if (peso == 1 and buffer == 1) or (peso == 1 and buffer == 2): 
        print("""
        (1) Incluir Vertices e Arestas
        (2) Visualizar o grafo e os dados
        (3) Sair
            """)
        opcao = int(input("Opção: "))
    if (peso == 2 and buffer == 1) or (peso == 2 and buffer == 2):
        print("""
        (1) Incluir Vertices
        (2) Visualizar o grafo e os dados
        (3) Sair
            """)
        opcao = int(input("Opção: "))

def opcoes(peso, buffer):
    global opcao
    global contaAresta
    menu_Opcoes(peso, buffer)
    try:
        # INCLUIR VERTICE
        if opcao == 1:
            if (peso == 1 and buffer == 1) or (peso == 1 and buffer == 2):
                incluir_Vertice_ArestaValorado(peso, buffer)
            if (peso == 2 and buffer == 1) or (peso == 2 and buffer == 2):
                incluir_Vertice_ArestaNValorado(peso, buffer)
            return opcoes(peso, buffer)
        # VISUALIZAR GRAFO E OS DADOS
        elif opcao == 2:
            gerar_Grafo_Lista(lista, peso, buffer)
            vertices = sorted(set(lista2))
            imprimir_GrauVertice(vertices, lista2, peso, buffer)
            if (peso == 1 and buffer == 1) or (peso == 1 and buffer == 2):
                visualizar_DadosGrafosValorados(peso, buffer)
            if (peso == 2 and buffer == 1) or (peso == 2 and buffer == 2):
                visualizar_DadosGrafosNaoValorados(peso, buffer)
            return opcoes(peso, buffer)

        # SAIR
        elif opcao == 3:
            G.clear()
            G2.clear()
            lista.clear()
            lista2.clear()
            contaAresta = 0
            return grafos()

    except ValueError:
        print(f"Erro no tipo da entrada {ValueError}")

def incluir_Vertice_ArestaValorado(op, buff):
    global contaAresta
    global verticeInput1
    global verticeInput2
    global valor
    try:
        while e == 1:

            if op == 1 and buff == 1:
                print("Digite o vertice de saida: ")
                verticeInput1 = input()
                print("Digite o vertice de chegada: ")
                verticeInput2 = input()
            if op == 1 and buff == 2:
                print("Digite o vertice: ")
                verticeInput1 = input()
                print("Digite o vertice: ")
                verticeInput2 = input()
            if ((verticeInput1 != verticeInput2) and (verticeInput2 != None) and (verticeInput1 != None)):
                lista.append(verticeInput1)
                lista2.append(verticeInput1)
                lista.append(verticeInput2)
                lista2.append(verticeInput2)
                if verticeInput2 != "":
                    print(
                        "Digite o peso da aresta: ")
                    valor = int(input())
                    lista.append(valor)
                    contaAresta += 1
                    G.add_node(verticeInput1)
                    G2.add_node(verticeInput1)
                else:
                    valor = 0
                    lista.append(valor)
                    contaAresta += 1
                    G.add_node(verticeInput1)
                    G2.add_node(verticeInput1)
                if verticeInput2 != "":
                    G.add_node(verticeInput2)
                    G2.add_node(verticeInput2)
                    if op == 1 and buff == 1:
                        G.add_edge(verticeInput1, verticeInput2, weight=valor)
                        G2.add_edge(verticeInput1, verticeInput2)
                    if op == 1 and buff == 2:
                        G.add_edge(verticeInput1, verticeInput2)
                        G2.add_edge(verticeInput1, verticeInput2, weight=valor)

            else:
                print("Operação não válida, tente novamente")

            print("\nVocê deseja continuar adicionando vértices? S/N")
            x = input().upper()
            if x == "S":
                continue
            if x == "N":
                break

    except ValueError:
        print(f"Erro no tipo da entrada {ValueError}")

def incluir_Vertice_ArestaNValorado(op, buff):
    global contaAresta
    global verticeInput1
    global verticeInput2
    try:
        while e == 1:
            if op == 2 and buff == 1:
                print("Digite o vertice de saida: ")
                verticeInput1 = input()
                print("Digite o vertice de entrada: ")

            if op == 2 and buff == 2:
                print("Digite o vertice: ")
                verticeInput1 = input()
                print("Digite o vertice: ")
            verticeInput2 = input()
            if ((verticeInput1 != verticeInput2) and (verticeInput2 != None) and (verticeInput1 != None)):
                lista.append(verticeInput1)
                lista2.append(verticeInput1)
                lista.append(verticeInput2)
                lista2.append(verticeInput2)
                contaAresta += 1
                if op == 2 and buff == 1:
                    if verticeInput2 != "":
                        G.add_node(verticeInput1)

                    else:
                        G.add_node(verticeInput1)

                    if verticeInput2 != "":
                        G.add_node(verticeInput2)

                        G.add_edge(verticeInput1,
                                   verticeInput2)
                if op == 2 and buff == 2:
                    if verticeInput2 != "":
                        G2.add_node(verticeInput1)

                    else:
                        G2.add_node(verticeInput1)

                    if verticeInput2 != "":
                        G2.add_node(verticeInput2)

                        G2.add_edge(verticeInput1,
                                    verticeInput2)

            print("\nVocê deseja continuar adicionando vértices? S/N")
            x = input().upper()
            if x == "S":
                continue
            if x == "N":
                break
    except ValueError:
        print(f"Erro no tipo da entrada {ValueError}")

def gerar_Grafo_Lista(grafo, modo, tipo):

    # Direcionado e Valorado
    if modo == 1 and tipo == 1:
        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 3):
            if grafo[j + 1] == "":
                print(f"""

                                    {grafo[j]}
                            """)
                j += 3
            else:
                print(f"""
                                  ({grafo[j+2]})
                                {grafo[j]} ----> {grafo[j+1]}
                                """)
            j += 3
        print("\n")
        print("---------------------------------------------------")
        print("\t\t\tLista de Arestas")
        for j in range(0, len(grafo), 3):
            if grafo[j + 1] == "":
                print(f"""Peso da aresta | Vértice de Saída | Vértice de Chegada
                         {grafo[j]}
            """)
                j += 3
            else:
                print(f"""Peso da aresta | Vértice de Saída | Vértice de Chegada
        ({grafo[j+2]})               {grafo[j]}          {grafo[j+1]}
                """)
            j += 3

        print("---------------------------------------------------")
        print("\n")

    # Direcionado e Não Valorado
    elif modo == 2 and tipo == 1:
        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 2):
            if grafo[j + 1] == "":
                print(f"""

                                    {grafo[j]}
                            """)
                j += 2
            else:
                print(f"""

                                {grafo[j]} ----> {grafo[j+1]}
                                """)
            j += 2
        for j in range(0, len(grafo), 2):
            if grafo[j + 1] == "":
                print(f"""Vértice de Saída | Vértice de Chegada
            {grafo[j]}
                """)
                j += 2
            else:
                print(f"""Vértice de Saída | Vértice de Chegada
            {grafo[j]}                  {grafo[j+1]}
                """)
            j += 2

        print("---------------------------------------------------")
        print("\n")

    # Não Direcionado e Valorado
    elif modo == 1 and tipo == 2:
        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 3):
            if grafo[j + 1] == "":
                print(f"""

                                    {grafo[j]}
                            """)
            else:
                print(f"""
                                ({grafo[j+2]})
                                {grafo[j]} ---- {grafo[j+1]}
                                """)
            j += 3
        print("---------------------------------------------------")
        print("\t\t\tLista de Arestas")
        for j in range(0, len(grafo), 3):
            if grafo[j + 1] == "":
                print(f"""Peso da aresta | Vértice de Saída | Vértice de Chegada
                         {grafo[j]}
            """)
                j += 3
            else:
                print(f"""Peso da aresta |         Vértices
            ({grafo[j+2]})               {grafo[j]}          {grafo[j+1]}
                """)
            j += 3

        print("---------------------------------------------------")
        print("\n")

    # Não Direcionado e Não valorado
    elif modo == 2 and tipo == 2:

        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 2):
            if grafo[j + 1] == "":
                print(f"""

                                    {grafo[j]}
                            """)
                j += 2
            else:
                print(f"""

                                {grafo[j]} ---- {grafo[j+1]}
                                """)
                j += 2
        for j in range(0, len(grafo), 2):
            if grafo[j + 1] == "":
                print(f"""Vértice de Saída | Vértice de Chegada
            {grafo[j]}
                """)
                j += 2
            else:
                print(f"""Vértice de Saída | Vértice de Chegada
                {grafo[j]}                  {grafo[j+1]}
                """)
                j += 2

def imprimir_GrauVertice(vertices, grafo, modo, tipo):

    # Direcionado
    if (modo == 1 or modo == 2) and tipo == 1:

        for j in range(0, len(vertices), 1):
            grauSaida = 0
            grauEntrada = 0
            for i in range(0, len(grafo), 2):
                if vertices[j] == grafo[i]:
                    grauSaida += 1
            for i in range(1, len(grafo), 2):
                if vertices[j] == grafo[i]:
                    grauEntrada += 1
            if vertices[j] != "":
                print("Grau de saída vértice   ",
                      vertices[j], " = ", grauSaida)
                print("Grau de entrada vértice ",
                      vertices[j], " = ", grauEntrada)

    # Não Direcionado
    elif (modo == 1 or modo == 2) and tipo == 2:
        for j in range(0, len(vertices), 1):
            grau = 0
            for i in range(0, len(grafo), 1):
                if vertices[j] == grafo[i]:
                    grau += 1
            if vertices[j] != "":
                print("Grau do vértice ", vertices[j], " = ", grau)

def visualizar_DadosGrafosValorados(op, buff):
    try:
        print(f"\nLista de Vértices: {G.nodes()}")

        print(f"Quantidade de Arestas: {contaAresta}")

        tamanho = len(lista)/3
        print("Tamanho do Grafo = ", tamanho)

        ordem = len(sorted(set(lista2)))
        print("Ordem do Grafo = ", ordem)

        print("\nLista de Adjacências:")
        for j in range(0, len(lista2), 2):
            print(
                f"Vértice destino: {lista2[j]}, Destinos: {lista2[j+1]}")

        # Imprimir Matriz de adjacências
        # Direcionado
        if op == 1 and buff == 1:
            print('\nMatriz de adjacências de GRAFO')
            A = nx.adjacency_matrix(G2)
            print(A.todense())
            print("\n")
        # Não Direcionado
        if op == 1 and buff == 2:
            print('\nMatriz de adjacências de GRAFO')
            A = nx.adjacency_matrix(G)
            print(A.todense())
            print("\n")

        # Questão 9: Verificar se os vertices são adjacentes
        print(
            "Escolha dois vértices para saber se eles são adjacentes")
        print("Vértice 1: ")
        u = input()
        print("Vértice 2: ")
        v = input()
        contador = 0

        for j in range(0, len(lista2), 2):
            if lista2[j] == u:
                if lista2[j+1] == v:
                    contador += 1
            j += 2

        if contador == 1:
            print("São adjacentes")
        elif contador == 0:
            print("Não são adjacentes")

        fig, ax = plt.subplots(figsize=(25,25))
        # Plot do Grafo Direcionado Valorado
        if op == 1 and buff == 1:
            node_size = [2500 for node in G.nodes]
            pos = nx.spring_layout(G)
            labels = nx.get_edge_attributes(G, 'weight')

            nx.draw_networkx_edge_labels(
                G, pos, edge_labels=labels)

            options = {
                'width': 1.0,
                'arrowstyle': '-|>',
                'arrowsize': 12,
            }
            nx.draw_networkx(G, pos, arrows=True,
                             with_labels=True, node_size=node_size, **options)

            plt.show()

        # Plot do Grafo Não Direcionado Valorado
        elif op == 1 and buff == 2:
            pos = nx.spring_layout(G2)
            labels = nx.get_edge_attributes(G2, 'weight')

            nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels)
            nx.draw(G2, pos, with_labels=True)

            plt.show()

    except IndexError:
        print(f"Erro no tipo da entrada {IndexError}")

def visualizar_DadosGrafosNaoValorados(op, buff):
    try:
        if op == 2 and buff == 1:
            print(f"\nLista de Vértices: {G.nodes()}")
        if op == 2 and buff == 2:
            print(f"\nLista de Vértices: {G2.nodes()}")
    
        print(f"Quantidade de Arestas: {contaAresta}")

        tamanho = len(lista)/2
        print("Tamanho do Grafo = ", tamanho)

        ordem = len(sorted(set(lista2)))
        print("Ordem do Grafo = ", ordem)

        print("\nLista de Adjacências:")
        for j in range(0, len(lista2), 2):
            print(
                f"Vértice destino: {lista2[j]}, Destinos: {lista2[j+1]}")

        if op == 2 and buff == 1:
            print('\nMatriz de adjacências de GRAFO')
            A = nx.adjacency_matrix(G)
            print(A.todense())
            print("\n")
        if op == 2 and buff == 2:
            print('\nMatriz de adjacências de GRAFO')
            A = nx.adjacency_matrix(G2)
            print(A.todense())
            print("\n")

        print(
            "Dado um par de vértices, retorne se os dois vértices são adjacentes ou não")
        print("Vértice 1: ")
        u = input()
        print("Vértice 2: ")
        v = input()
        contador = 0

        for j in range(0, len(lista2), 2):
            if lista2[j] == u:
                if lista2[j+1] == v:
                    contador += 1
            j += 2

        if contador == 1:
            print("São adjacentes")
        elif contador == 0:
            print("Não são adjacentes")
        print("\n")

        # Plot do grafo
        # Direcionado
        if op == 2 and buff == 1:
            pos = nx.spring_layout(G)

            nx.draw(G, pos, with_labels=True)

            plt.show()
        # Não direcionado
        if op == 2 and buff == 2:
            pos = nx.spring_layout(G2)

            nx.draw(G2, pos, with_labels=True)

            plt.show()

    except ValueError:
        print(f"Erro no tipo da entrada {ValueError}")


menu_Grafos()
