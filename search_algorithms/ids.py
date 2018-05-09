import math

def dls (g, vertice_inicial, vertice_final, profundidade, profundidade_maxima, visitados, caminho, img):
    if vertice_inicial == vertice_final:
        return True

    if profundidade <= 0:
        return False
    
    profundidade_atual = profundidade_maxima - profundidade

    for i in g.graph[vertice_inicial]:

        # pos_y = vertice_inicial % g.width
        # pos_x = math.floor(vertice_inicial / g.width)
        # img.putpixel( (  pos_y, pos_x ), (255,0,0) )
        
        if (visitados[i] == -1 or profundidade_atual < visitados[i]):
            visitados[i] = profundidade_atual
        else:
            continue
        
        if (dls (g, i, vertice_final, (profundidade - 1), profundidade_maxima, visitados, caminho, img)):
            caminho.append(i)
            return caminho
    
    return False
 
def ids (g, vertice_inicial, vertice_final, img):
    resultado = False
    profundidade = 0
    caminho = []

    while (resultado == False):
        visitados = [-1] * (g.width * g.height)
        temp = dls (g, vertice_inicial, vertice_final, profundidade, profundidade, visitados, caminho, img)
        if (temp):
            resultado = True
        profundidade += 1
    
    caminho.append(vertice_inicial)
    return caminho