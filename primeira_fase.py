import numpy as np
from numpy import ones, inf
from operator import itemgetter

np.set_printoptions(precision=0)


def floyd_warshall(dim, conexoes):
    
    dim+=1
    dist = ones([dim, dim], dtype=np.int)
    dist = inf*dist
    
    for i in range(dim):
        dist[i, i] = 0

    for i, j in conexoes:
        dist[i, j] = 1

    for i in range(dim):
        for j in range(dim):
            if i == j:
                continue
            for k in range(dim):
                dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])

    return dist


def farness(aresta, distancias):
    return sum(distancias[aresta])


def closeness(aresta, distancias):
    return 1/farness(aresta, distancias)


def rank_close(proximidades):
    '''Recebe um dict com cuja chave é a aresta, e o valor é o closeness
        Retorna a lista de arestas organizada por closeness
    '''
    return [l for l, _ in sorted(proximidades.items(), key=itemgetter(1), reverse=True)]
    

if __name__ == '__main__':
    f = open('edges.dat', 'r')

    conexoes = []
    maximo_local = 0
    for linha in f.readlines():                   
        i, j = linha.replace('\n','').split(' ')
        conexoes.append((int(i), int(j)))
        maximo_local = max(int(i), int(j),maximo_local)
        
        
    dist = floyd_warshall(maximo_local, conexoes)

    proximidades = {}
    for i in range(maximo_local+1):
        proximidades[i] = closeness(i, dist)

    _ = [print('Closeness do nó {}:\t{:03f}'.format(l, k)) 
            for l, k in sorted(proximidades.items(), key=itemgetter(1), reverse=True)]
