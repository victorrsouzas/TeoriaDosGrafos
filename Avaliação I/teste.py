import time

c = 0
d = 1

def grafos():

    while d == 1:
        print("    ------ADICIONAR GRAFO------")
        print("""
        Escolha a opção do grafo:
        (1) Direcionado
        (2) Não Direcionado
        (3) Sair
        """)
        c = int(input("Opção: "))
        if c == 1:
            print("""
        (1) Valorado
        (2) Não Valorado
        (3) Sair
            """)
            direcionado = int(input("O seu grafo direcionado vai ser: "))
            if direcionado == 1:
                lista = []
                lista2 = []
                try:
                    entrada = int(input("Quantos pares de vertice você quer criar?: "))
                    for i in range(entrada*2):
                        print("digite a letra do vertice:")
                        x = input()
                        lista.append(x)
                        lista2.append(x)

                        if (i+1) % 2 == 0:
                            print("digite o valor da aresta (?):")
                            valor = int(input())
                            lista.append(valor)

                        print(lista)
                    
                    for j in range(0,len(lista),3):
                        
                        print(f"""
                        ({lista[j+2]})
                        {lista[j]} ----> {lista[j+1]}
                        """)
                        j +=3
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
