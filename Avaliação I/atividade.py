print("Teoria dos Grafos 2021.1 - Avaliação I")

lista = []

#O usuário deverá ser capaz de interagir com o sistema para criar um grafo.
entrada = int(input("Quantos pares de vertice você quer criar?: "))
especif = print("Você quer criar grafos:")
#O usuário poderá criar grafos direcionados e não-direcionados
print("1-direcionados ou 2-não direcionados")
entrada2 = int(input())
#O usuário poderá criar grafos valorados e não-valorados
print("3-valorados ou 4-não valorados")
entrada3 = int(input())

for i in range(entrada*2):
    print("digite a letra do vertice:")
    x = input()
    lista.append(x)

    if entrada3 == 3:
        print("digite o valor da aresta (?):")
        valor = int(input())  
        lista.append(valor)
        
    print(lista)

#ideia de como printar a matriz com lista
if entrada2 == 1:
    direc = "--"
else:
    direc = "-->"
#lista[j] = vertice 1, lista[j+2] = vertice 2, lista[j+3] = valor
#fazer o for ir de 3 em 3 para ir passando os pares de vertices
for j in range(len(lista)):
    print(lista[j], direc, lista[j+1], lista[j+2])
    j+=3

