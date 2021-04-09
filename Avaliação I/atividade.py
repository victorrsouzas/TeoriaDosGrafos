print("Teoria dos Grafos 2021.1 - Avaliação I")

#O usuário deverá ser capaz de interagir com o sistema para criar um grafo.
entrada = int(input("Quantos pares de vertice você quer criar?: "))

lista = []

for i in range(entrada*2):
    print("digite a letra do vertice:")
    x = input()
    print("aqui e o indice",(i+1))
    lista.append(x)
    if (i+1) % 2 == 0:
        #O usuário poderá criar grafos direcionados e não-direcionados
        print("Você quer criar grafos:")
        print("1-direcionados ou 2-não direcionados")
        entrada2 = int(input())
        lista.append(entrada2)
        #O usuário poderá criar grafos valorados e nã)
        lista.append(entrada3)

    print(lista)


# if entrada2 == 1 and entrada3 == 3:
#     print("1")
# elif entrada2 == 1 and entrada3 == 4:
#     print("2")
# elif entrada2 == 2 and entrada3 == 3:
#     print("3")
# elif entrada2 == 2 and entrada3 == 4:
#     print("4")
# else:
#     print("Você digitou a opção errada")
