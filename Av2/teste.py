import time
import networkx as nx
import matplotlib.pyplot as plt
import sys
import numpy as np

buffer = 0
d = 1
e = 1
G = nx.DiGraph()  # Direcionado
G2 = nx.Graph()  # Não Direcionado
contaAresta = 0


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
        a = input("    Opção: ").upper()
        if a == "SIM":
            grafos()
        elif a == "NÃO" or a == "NAO":
            sys.exit()
        else:
            print("\nRESPONDA APENAS SIM OU NÃO")


def menu_Tipo_Grafo():
    print("""
    -----------------------------
            ADICIONAR GRAFO
    -----------------------------
    """)
    print("""
    Escolha a opção do grafo:
    (1) Direcionado
    (2) Não Direcionado
    (3) Sair
    """)


def menu_Tipo():
    print("""
    -----------------------------
            TIPO GRAFO
    -----------------------------
    """)
    print("""
    (1) Valorado
    (2) Não Valorado
    (3) Sair
        """)


def menu_Visualização(peso, buffer):
    global opcao
    if (peso == 1 and buffer == 1) or (peso == 1 and buffer == 2):
        print("""
    -----------------------------
            VISUALIZAÇÃO
    -----------------------------
    """)
        print("""
    (1) Lista de arestas
    (2) Lista de graus
    (3) Lista de vertices
    (4) Tamanho do grafo
    (5) Matriz de adjacências
    (6) Verificar vertices adjacentes
    (7) Plot do Grafo
    (8) Algoritmo de dijkstra
    (9) Algoritmo de Bellman-Ford
    (10) Sair
    """)
        opcao = int(input("    Opção: "))
        print("\n")

    if (peso == 2 and buffer == 1) or (peso == 2 and buffer == 2):
        print("""
    -----------------------------
            VISUALIZAÇÃO
    -----------------------------
    """)
        print("""
    (1) Lista de arestas
    (2) Lista de graus
    (3) Lista de vertices
    (4) Tamanho do grafo
    (5) Matriz de adjacências
    (6) Verificar vertices adjacentes
    (7) Plot do Grafo
    (8) Algoritmo de dijkstra
    (9) Algoritmo de Bellman-Ford
    (10) Todos
    (11) Sair
    """)
        opcao = int(input("    Opção: "))
        print("\n")


def grafos():

    while d == 1:
        menu_Tipo_Grafo()
        try:
            buffer = int(input("    Opção: "))
            # FOR DIRECIONADO
            if buffer == 1:
                menu_Tipo()
                peso = int(input("    O seu grafo direcionado vai ser:"))
                # FOR DIRECIONADO E VALORADO
                if peso == 1:
                    opcoes(peso, buffer)

                # FOR DIRECIONADO E NÃO VALORADO
                elif peso == 2:
                    opcoes(peso, buffer)

                # SAIR DA OPÇÃO DIRECIONADO: VALORADO OU NÃO VALORADO
                elif peso == 3:
                    menu_Grafos()()

            # FOR NÃO DIRECIONADO
            elif buffer == 2:
                menu_Tipo()
                peso = int(
                    input("    O seu grafo não direcionado vai ser: "))
                # FOR NÃO DIRECIONADO E VALORADO
                if peso == 1:
                    opcoes(peso, buffer)

                # FOR NÃO DIRECIONADO E NÃO VALORADO
                elif peso == 2:
                    opcoes(peso, buffer)
                # SAIR
                elif peso == 3:
                    menu_Grafos()
            elif buffer == 3:
                menu_Grafos()
        except ValueError:
            print(f"    Erro no tipo da entrada {ValueError}")

        break


def menu_Opcoes(peso, buffer):
    global opcao
    if (peso == 1 and buffer == 1) or (peso == 1 and buffer == 2):
        print("""
    -----------------------------
            OPÇÕES
    -----------------------------
    """)
        print("""
    (1) Incluir Vertices e Arestas
    (2) Remover Vertices
    (3) Visualizar o grafo e os dados
    (4) Sair
            """)
        opcao = int(input("    Opção: "))
        print("\n")
    if (peso == 2 and buffer == 1) or (peso == 2 and buffer == 2):
        print("""
    -----------------------------
            OPÇÕES
    -----------------------------
    """)
        print("""
    (1) Incluir Vertices
    (2) Remover Vertices
    (3) Visualizar o grafo e os dados
    (4) Sair
            """)
        opcao = int(input("    Opção: "))
        print("\n")


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
        # REMOVER VERTICE
        elif opcao == 2:
            removerVertice()
            return opcoes(peso, buffer)
        # VISUALIZAR GRAFO E OS DADOS
        elif opcao == 3:
            opcoes_Visualização(peso, buffer)
            return opcoes(peso, buffer)

        # SAIR
        elif opcao == 4:
            G.clear()
            G2.clear()
            contaAresta = 0
            return grafos()

    except ValueError:
        print(f"Erro no tipo da entrada {ValueError}")


def opcoes_Visualização(peso, buffer):
    global opcao
    menu_Visualização(peso, buffer)
    if opcao == 1:
        gerar_Grafo_Lista(peso, buffer)
        return opcoes_Visualização(peso, buffer)
    elif opcao == 2:
        imprimir_GrauVertice(peso, buffer)
        return opcoes_Visualização(peso, buffer)
    elif opcao == 3:
        print("""
        -----------------------------
                LISTA DE VERTICES
        -----------------------------
        """)
        if (peso == 1 and buffer == 1) or (peso == 1 and buffer == 2):
            print(f"    Lista de Vértices: {G.nodes()}")
        if peso == 2 and buffer == 1:
            print(f"    Lista de Vértices: {G.nodes()}")
        if peso == 2 and buffer == 2:
            print(f"    Lista de Vértices: {G2.nodes()}")
        print("---------------------------------------------------")
        print("\n")
        return opcoes_Visualização(peso, buffer)
    elif opcao == 4:
        print("""
        -----------------------------
                TAMANHO DO GRAFO
        -----------------------------
        """)
        print(f"    Tamanho do Grafo: {contaAresta}")
        print("---------------------------------------------------")
        print("\n")
        return opcoes_Visualização(peso, buffer)
    elif opcao == 5:
        print("""
        -----------------------------
                MATRIZ DE ADJACÊNCIA
        -----------------------------
        """)
        if peso == 1 and buffer == 1:
            A = nx.adjacency_matrix(G2)
            print(f"    {A.todense()}")
            print("\n")
            return opcoes_Visualização(peso, buffer)
        if peso == 1 and buffer == 2:
            A = nx.adjacency_matrix(G)
            print(f"    {A.todense()}")
            print("\n")
            return opcoes_Visualização(peso, buffer)
        if peso == 2 and buffer == 1:
            A = nx.adjacency_matrix(G)
            print(f"    {A.todense()}")
            print("\n")
            return opcoes_Visualização(peso, buffer)
        if peso == 2 and buffer == 2:
            A = nx.adjacency_matrix(G2)
            print(f"    {A.todense()}")
            print("\n")
            return opcoes_Visualização(peso, buffer)
    elif opcao == 6:
        print("""
        -----------------------------
                VERTICES ADJACENTES
        -----------------------------
        """)
        u = input("    Vértice 1: ")
        v = input("    Vértice 2: ")
        contador = 0

        for edge in G.edges():
            i = 0
            if peso == 1 and buffer == 1:
                if edge[i] == u:
                    if edge[i + 1] == v:
                        contador += 1
            if peso == 1 and buffer == 2:
                if edge[i] == u:
                    if edge[i + 1] == v:
                        contador -= 1
            i += 1

        if contador == 1:
            print("    São adjacentes")
            print("\n")
            return opcoes_Visualização(peso, buffer)
        elif contador <= 0:
            print("    Não são adjacentes")
            print("\n")
            return opcoes_Visualização(peso, buffer)

    elif opcao == 7:
        print("""
    -----------------------------
            PLOT DO GRAFO
    -----------------------------
        """)
        fig, ax = plt.subplots(figsize=(25, 25))
        # Plot do Grafo Direcionado Valorado
        if peso == 1 and buffer == 1:
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
            return opcoes_Visualização(peso, buffer)

        # Plot do Grafo Não Direcionado Valorado
        elif peso == 1 and buffer == 2:
            pos = nx.spring_layout(G2)
            labels = nx.get_edge_attributes(G2, 'weight')

            nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels)
            nx.draw(G2, pos, with_labels=True)

            plt.show()
            return opcoes_Visualização(peso, buffer)
        # Plot do grafo
        # Direcionado e Não Valorado
        elif peso == 2 and buffer == 1:
            pos = nx.spring_layout(G)

            nx.draw(G, pos, with_labels=True)

            plt.show()
            return opcoes_Visualização(peso, buffer)
        # Não direcionado e Não Valorado
        elif peso == 2 and buffer == 2:
            pos = nx.spring_layout(G2)

            nx.draw(G2, pos, with_labels=True)

            plt.show()
            return opcoes_Visualização(peso, buffer)

    elif opcao == 8:
        print("""
        -----------------------------
                ALGORITMO DE DIJKSTRA
        -----------------------------
        """)
        if (peso == 1 and buffer == 1):
            x = input("    Vertice de Origem: ")
            y = input("    Vertice de Destino: ")
            dijkstra_one_to_one(G, x, y)
            return opcoes_Visualização(peso, buffer)
        else:
            print("    O algoritmo é exclusivo para a opção de direcionado e valorado")
            return opcoes_Visualização(peso, buffer)
    
    elif opcao == 9:
        return opcoes_Visualização(peso, buffer)

    elif opcao == 10:
        return opcoes(peso, buffer)


def incluir_Vertice_ArestaValorado(op, buff):
    global contaAresta
    global verticeInput1
    global verticeInput2
    global valor
    try:
        while e == 1:

            if op == 1 and buff == 1:
                verticeInput1 = input("    Digite o vertice de saida: ")
                verticeInput2 = input("    Digite o vertice de chegada: ")
            if op == 1 and buff == 2:
                verticeInput1 = input("    Digite o vertice: ")
                verticeInput2 = input("    Digite o vertice: ")
            if ((verticeInput1 != verticeInput2) and (verticeInput2 != None) and (verticeInput1 != None)):
                if verticeInput2 != "":
                    valor = int(input("    Digite o peso da aresta: "))
                    contaAresta += 1
                    G.add_node(verticeInput1)
                    G2.add_node(verticeInput1)
                else:
                    valor = 0
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
                print("    Operação não válida, tente novamente")

            x = input(
                "\n    Você deseja continuar adicionando vértices[S/N]? ").upper()
            if x == "S":
                continue
            if x == "N":
                break

    except ValueError:
        print(f"    Erro no tipo da entrada {ValueError}")


def incluir_Vertice_ArestaNValorado(op, buff):
    global contaAresta
    global verticeInput1
    global verticeInput2
    try:
        while e == 1:
            if op == 2 and buff == 1:
                verticeInput1 = input("    Digite o vertice de saida: ")
                verticeInput2 = input("    Digite o vertice de chegada: ")

            if op == 2 and buff == 2:
                verticeInput1 = input("    Digite o vertice: ")
                verticeInput2 = input("    Digite o vertice: ")
            if ((verticeInput1 != verticeInput2) and (verticeInput2 != None) and (verticeInput1 != None)):
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

            x = input(
                "\n    Você deseja continuar adicionando vértices[S/N]? ").upper()
            if x == "S":
                continue
            if x == "N":
                break
    except ValueError:
        print(f"    Erro no tipo da entrada {ValueError}")


def gerar_Grafo_Lista(modo, tipo):

    # Direcionado e Valorado
    if modo == 1 and tipo == 1:
        print("""    
        -----------------------------
                LISTA DE ARESTAS
        -----------------------------
        """)
        i = 1
        for edge in G.edges():
            u = edge[0]
            v = edge[1]
            print(
                f"\n    Par {i}: O peso da aresta: {edge}, vale: {G[u][v]['weight']}")
            i += 1
        print("---------------------------------------------------")
        print("\n")

    # Direcionado e Não Valorado
    elif modo == 2 and tipo == 1:
        print("""    
        -----------------------------
                PARES DE VERTICES
        -----------------------------
        """)
        i = 1
        for edge in G.edges():
            u = edge[0]
            v = edge[1]
            print(f"\n    Par {i} de Vertices: {edge}")
            i += 1
        print("---------------------------------------------------")
        print("\n")

    # Não Direcionado e Valorado
    elif modo == 1 and tipo == 2:
        print("""    
        -----------------------------
                LISTA DE ARESTAS
        -----------------------------
        """)
        i = 1
        for edge in G2.edges():
            u = edge[0]
            v = edge[1]
            print(
                f"\n    Par {i}: O peso da aresta: {edge}, vale: {G2[u][v]['weight']}")
            i += 1
        print("---------------------------------------------------")
        print("\n")

    # Não Direcionado e Não valorado
    elif modo == 2 and tipo == 2:
        print("""    
        -----------------------------
                PARES DE VERTICES
        -----------------------------
        """)
        i = 1
        for edge in G.edges():
            u = edge[0]
            v = edge[1]
            print(f"\n    Par {i} de Vertices: {edge}")
            i += 1
        print("---------------------------------------------------")
        print("\n")


def imprimir_GrauVertice(modo, tipo):

    # Direcionado
    if (modo == 1 or modo == 2) and tipo == 1:
        print("""    
        -----------------------------
                LISTA DE GRAUS
        -----------------------------
        """)
        print(f"    {G.degree}")

        print("---------------------------------------------------")
        print("\n")

    # Não Direcionado
    elif (modo == 1 or modo == 2) and tipo == 2:
        print("""    
        -----------------------------
                LISTA DE GRAUS
        -----------------------------
        """)
        print(f"    {G.degree}")

        print("---------------------------------------------------")
        print("\n")


def removerVertice():
    global contaAresta
    try:
        while e == 1:
            print(f"\n    Lista de Vértices: {G.nodes()}")
            r = input("    Deseja remover qual vertice: ")
            if r in G.nodes():
                G.remove_node(r)
                contaAresta -= 1
            else:
                print("    Vertice não se encontra no grafo")

            x = input(
                "\n    Você deseja continuar adicionando vértices[S/N]? ").upper()
            if x == "S":
                continue
            if x == "N":
                break

    except ValueError:
        print(f"    Erro no tipo da entrada {ValueError}")


def dijkstra_one_to_all(G):

    path_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))
    print(f"\n    Caminhos: ")
    print(f"\n    {path_lengths}")
    # sum the lengths to individual nodes
    new_dict = {node1: sum([length for length in path_lengths[node1].values()]) for node1 in path_lengths.keys()}
    # print the lengths
    for node,length in new_dict.items():
        print('\n    A soma dos comprimentos do nó {} para todos os outros nós é {}.'.format(node,length))
    return


def dijkstra_one_to_one(G, origem, destino):
    if destino != origem:
        try:
            length = nx.shortest_path_length(
                G, source=origem, target=destino, weight="weight", method='dijkstra')
            print("    Comprimento do caminho mais curto de ",
                  origem, " para ", destino, " : ", length)
            path = nx.shortest_path(
                G, source=origem, target=destino, weight="weight")
            print("    Os caminhos mais curtos de ",
                  origem, " para ", destino, " : ", path)
            dijkstra_one_to_all(G)
            x = input(
                "\n    Você deseja visualizar o grafo [S/N]? ").upper()
            if x == "S":
               plotGraphDijkstra(G, path)
            if x == "N":
                return
        except nx.exception.NetworkXNoPath:
            print('    Sem caminho de ', origem, ' to ', destino)
    else:
        print("origem = destino")

    return


def plotGraphDijkstra(G, path):
    fig, ax = plt.subplots(figsize=(25, 25))
    node_size = [2500 for node in G.nodes]
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    # Separa as arestas que fazem parte do menor caminho e guarda em arestas_vermelhas
    arestas_vermelhas = list(zip(path, path[1:]))

    # Marca as arestas que estão no Path para serem pintados de vermelho e as outras de preto
    cor_arestas = [
        'black' if not edge in arestas_vermelhas else 'red' for edge in G.edges()]
    # Marca os vértices que estão no Path para serem pintados de azul e os outros de branco
    cor_vertices = [
        'yellow' if not node in path else 'green' for node in G.nodes()]

    nx.draw_networkx_edges(G, pos, edge_color=cor_arestas)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    options = {
        'width': 1.0,
        'arrowstyle': '-|>',
        'arrowsize': 12,
    }
    nx.draw_networkx(G, pos, arrows=True,
                     with_labels=True, node_color=cor_vertices, edge_color=cor_arestas, node_size=node_size, **options)

    # Mostra o grafo
    plt.show()


menu_Grafos()
