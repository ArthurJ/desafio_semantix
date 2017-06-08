import numpy as np
from numpy import ones, inf
from operator import itemgetter


def floyd_warshall(dim, conexoes):
    
    dim+=1
    dist = ones([dim, dim], dtype=np.int)
    dist = inf*dist
    
    for i in range(dim):
        dist[i, i] = 0

    for i, j in conexoes:
        dist[i, j] = 1
        dist[j, i] = 1
    
    grafo = np.array(dist)

    for i in range(dim):
        for j in range(dim):
            if i == j:
                continue
            for k in range(dim):
                dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])
                dist[j, i] = min(dist[j, i], dist[j, k] + dist[k, i])

    return dist, grafo


def farness(vertice, distancias):
    return sum(distancias[vertice])


def closeness(vertice, distancias):
    return 1/farness(vertice, distancias)


def rank_close(proximidades):
    '''Recebe um dict com cuja chave é o vertice, e o valor é o closeness
        Retorna a lista de vertices organizada por closeness
    '''
    return [l for l, _ in sorted(proximidades.items(), key=itemgetter(1), reverse=True)]
    

if __name__ == '__main__':
    f = open('edges.dat', 'r')

    conexoes = []
    tamanho_da_rede = 0
    for linha in f.readlines():                   
        i, j = linha.replace('\n','').split(' ')
        conexoes.append((int(i), int(j)))
        tamanho_da_rede = max(int(i), int(j),tamanho_da_rede)
        
        
    dist, grafo = floyd_warshall(tamanho_da_rede, conexoes)

    proximidades = {}
    for i in range(tamanho_da_rede+1):
        proximidades[i] = closeness(i, dist)

    _ = [print('Closeness do nó {}:\t{:03f}'.format(l, k)) 
            for l, k in sorted(proximidades.items(), key=itemgetter(1), reverse=True)]
