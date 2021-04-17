import time

c = 0
d = 1

def imprimirGrafo(grafo, modo):

    # Direcionado e Valorado
    if modo == 1:
        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 3):

            print(f"""
                              ({grafo[j+2]})
                            {grafo[j]} ----> {grafo[j+1]}
                            """)
            j += 3
        print("\n")
        print("---------------------------------------------------")
        print("\t\t\tLista de Arestas")
        for j in range(0, len(grafo), 3):

            print(f"""Nome da aresta | Vértice de Saída | Vértice de Chegada
        ({grafo[j+2]})               {grafo[j]}          {grafo[j+1]}
            """)
            j += 3

        print("---------------------------------------------------")
        print("\n")

    # Direcionado e Não Valorado
    elif modo == 2:
        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 2):
            print(f"""

                            {grafo[j]} ----> {grafo[j+1]}
                            """)
            j += 2
        for j in range(0, len(grafo), 2):

            print(f"""Vértice de Saída | Vértice de Chegada
            {grafo[j]}                  {grafo[j+1]}
            """)
            j += 2

        print("---------------------------------------------------")
        print("\n")

    # Não Direcionado e Valorado
    elif modo == 4:
        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 3):

            print(f"""
                              ({grafo[j+2]})
                            {grafo[j]} ---- {grafo[j+1]}
                            """)
            j += 3
        print("---------------------------------------------------")
        print("\t\t\tLista de Arestas")
        for j in range(0, len(grafo), 3):

            print(f"""Nome da aresta |         Vértices
        ({grafo[j+2]})               {grafo[j]}          {grafo[j+1]}
            """)
            j += 3

        print("---------------------------------------------------")
        print("\n")

    # Não Direcionado e Não valorado
    elif modo == 5:

        print("---------------------------------------------------")
        print("\t\t\tVisualização")
        for j in range(0, len(grafo), 2):
            print(f"""

                            {grafo[j]} ---- {grafo[j+1]}
                            """)
            j += 2
        for j in range(0, len(grafo), 2):

            print(f"""Vértice de Saída | Vértice de Chegada
            {grafo[j]}                  {grafo[j+1]}
            """)
            j += 2


def grauVertice(vertices, grafo, modo):
    
    # Direcionado
    if modo == 1 or modo == 2:
        
        for j in range(0, len(vertices), 1):
            grauSaida = 0
            grauEntrada = 0 
            for i in range(0, len(grafo), 2):
                if vertices[j] == grafo[i]:
                    grauSaida+=1
            for i in range(1, len(grafo), 2):
                if vertices[j] == grafo[i]:
                    grauEntrada+=1
            print("Grau de saída vértice   ", vertices[j]," = ", grauSaida)
            print("Grau de entrada vértice ", vertices[j]," = ", grauEntrada)
           
          
    # Não Direcionado 
    elif modo == 4 or modo == 5:
        for j in range(0, len(vertices), 1):
            grau = 0
            for i in range(0, len(grafo), 1):
                if vertices[j] == grafo[i]:
                    grau+=1
            print("Grau do vértice ", vertices[j]," = ", grau)
            

def grafos():

    while d == 1:
        print("    ------ADICIONAR GRAFO------")
        print("""
        Escolha a opção do grafo:
        (1) Direcionado
        (2) Não Direcionado
        (3) Sair
        """)
        try:
            c = int(input("Opção: "))
            if c == 1:
                print("""
            (1) Valorado
            (2) Não Valorado
            (3) Sair
                """)
                direcionado = int(input("O seu grafo direcionado vai ser:"))
                if direcionado == 1:
                    lista = []
                    lista2 = []
                    try:
                        entrada = int(
                            input("Quantos pares de vértice você quer criar:"))
                        for i in range(entrada):
                            print("Digite a letra do primeiro vértice: ")
                            verticeInput1 = input()
                            print("Digite a letra do segundo vértice: ")
                            verticeInput2 = input()
                            if ((verticeInput1 != verticeInput2) and (verticeInput2 != None) and (verticeInput1 != None)):
                                lista.append(verticeInput1)
                                lista2.append(verticeInput1)
                                lista.append(verticeInput2)
                                lista2.append(verticeInput2)
                                print("Digite o valor da aresta:")
                                valor = int(input())
                                lista.append(valor)
                            else:
                                print("Operação não válida, tente novamente")
                                i-=1


                        imprimirGrafo(lista, direcionado)
                        print(f"Lista de Vértices: {lista2}")
                        tamanho = len(lista)/3
                        print("Tamanho do Grafo = ", tamanho)
                        ordem = len(sorted(set(lista2)))
                        print("Ordem do Grafo = ", ordem)
                        print("\nLista de Adjacências:")
                        for j in range(0, len(lista2), 2):
                            print(
                                f"Vértice destino: {lista2[j]}, Destinos: {lista2[j+1]}")
                        
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

                        vertices = sorted(set(lista2))
                        grauVertice(vertices,lista2, direcionado)

                    except ValueError:
                        print(f"Erro no tipo da entrada {ValueError}")
                        

                elif direcionado == 2:
                    lista = []
                    lista2 = []
                    try:
                        entrada = int(
                            input("Quantos pares de vértice você quer criar?: "))
                        for i in range(entrada*2):
                            print("Digite a letra do vértice:")
                            x = input()
                            lista.append(x)
                            lista2.append(x)

                        imprimirGrafo(lista, direcionado)
                        tamanho = len(lista)/2
                        print("Tamanho do Grafo = ", tamanho)
                        print(f"Lista de Vértices: {lista2}")
                        ordem = len(sorted(set(lista2)))
                        print("Ordem do Grafo = ", ordem)
                        print("\nLista de Adjacências:")
                        for j in range(0, len(lista2), 2):
                            print(
                                f"Vértice destino: {lista2[j]}, Destinos: {lista2[j+1]}")

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

                        vertices = sorted(set(lista2))
                        grauVertice(vertices,lista2, direcionado)

                    except ValueError:
                        print(f"Erro no tipo da entrada {ValueError}")

                elif direcionado == 3:
                    return grafos()

            elif c == 2:
                print("""
            (4) Valorado
            (5) Não Valorado
            (6) Sair
                """)
                naoDirecionado = int(
                    input("O seu grafo não direcionado vai ser: "))
                if naoDirecionado == 4:
                    lista = []
                    lista2 = []
                    try:
                        entrada = int(
                            input("Quantos pares de vértice você quer criar?: "))
                        for i in range(entrada):
                            print("Digite a letra do primeiro vértice: ")
                            verticeInput1 = input()
                            print("Digite a letra do segundo vértice: ")
                            verticeInput2 = input()
                            if ((verticeInput1 != verticeInput2) and (verticeInput2 != None) and (verticeInput1 != None)):
                                lista.append(verticeInput1)
                                lista2.append(verticeInput1)
                                lista.append(verticeInput2)
                                lista2.append(verticeInput2)
                                print("Digite o valor da aresta:")
                                valor = int(input())
                                lista.append(valor)
                            else:
                                print("Operação não válida, tente novamente")
                                i-=1
        
                        imprimirGrafo(lista, naoDirecionado)
                        aux = len(lista)/3
                        tamanho = aux * 4
                        print("Tamanho do Grafo = ", tamanho)
                        print(f"Lista de Vertices: {lista2}")
                        ordem = len(sorted(set(lista2)))
                        print("Ordem do Grafo = ", ordem)
                        print("\nLista de Adjacências:")
                        for j in range(0, len(lista2), 2):
                            print(
                                f"Vértice destino: {lista2[j]}, Destinos: {lista2[j+1]}")
                        print("\n")
                        print(
                            "Dado um par de vértices, retorne se os dois vértices são adjacentes ou não")
                        print("Vértice 1: ")
                        u = input()
                        print("Vértice 2: ")
                        v = input()

                        for j in range(0, len(lista2), 2):
                            if lista2[j] == u:
                                if lista2[j+1] == v:
                                    print("São adjacentes")
                            elif lista2[j] == v:
                                if lista2[j+1] == u:
                                    print("São adjacentes")
                            else:
                                print("Não são adjacentes")
                            j += 2
                        
                        print("\n")
                        vertices = sorted(set(lista2))
                        grauVertice(vertices,lista2, naoDirecionado)

                    except ValueError:
                        print(f"Erro no tipo da entrada {ValueError}")

                elif naoDirecionado == 5:
                    lista = []
                    lista2 = []
                    try:
                        entrada = int(
                            input("Quantos pares de vértice você quer criar?: "))
                        for i in range(entrada*2):
                            print("Digite a letra do vértice:")
                            x = input()
                            lista.append(x)
                            lista2.append(x)

                        imprimirGrafo(lista, naoDirecionado)
                        tamanho = len(lista) * 2
                        print("Tamanho do Grafo = ", tamanho)
                        print(f"Lista de Vértices: {lista2}")
                        ordem = len(sorted(set(lista2)))
                        print("Ordem do Grafo = ", ordem)
                        print("\nLista de Adjacências:")
                        for j in range(0, len(lista2), 2):
                            print(
                                f"Vértice destino: {lista2[j]}, Destinos: {lista2[j+1]}")
                        print("\n")
                        print(
                            "Dado um par de vértices, retorne se os dois vértices são adjacentes ou não")
                        print("Vértice 1: ")
                        u = input()
                        print("Vértice 2: ")
                        v = input()

                        for j in range(0, len(lista2), 2):
                            if lista2[j] == u:
                                if lista2[j+1] == v:
                                    print("São adjacentes")
                            elif lista2[j] == v:
                                if lista2[j+1] == u:
                                    print("São adjacentes")
                            else:
                                print("Não são adjacentes")
                            j += 2

                        print("\n")
                        vertices = sorted(set(lista2))
                        grauVertice(vertices,lista2, naoDirecionado)

                    except ValueError:
                        print(f"Erro no tipo da entrada {ValueError}")

                elif naoDirecionado == 6:
                    return grafos()
            elif c == 3:
                break

            else:
                print("\nResponda Apenas(1-2-3)")
            print("-------------------------")
            print("(1) VOLTAR MENU")
            b = int(input(""))
            if d == 2:
                break
        except ValueError:
            print(f"Erro no tipo da entrada {ValueError}")


def menuGrafos():
    b = 1
    print("""
    -----------------------------
             Teoria Grafos
    -----------------------------
    """)
    time.sleep(1)
    while b == 1:
        print("""
    -----------------------------
      SISTEMA GRAFOS
    -----------------------------
        VOCÊ DESEJA INICIAR UM GRAFO?
        - SIM
        - NÃO
    -----------------------------""")
        a = input("Opção: ").upper()
        print("\n")
        if a == "SIM":
            grafos()
        elif a == "NÃO" or a == "NAO":
            break
        else:
            print("\nRESPONDA APENAS SIM OU NÃO")

        print("-------------------------")
        print("(1) VOLTAR MENU")
        # b=int(input(""))
        try:
            b = int(input(""))
            if b == 1:
                continue
        except ValueError:
            print(
                "Se você deseja voltar ao menu digite 1, caso realmente queira sair digite 0")
            b = int(input(""))
            if b == 1:
                continue
            if b == 0:
                break


menuGrafos()
