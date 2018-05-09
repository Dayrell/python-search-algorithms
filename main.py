import sys
import math

from PIL import Image
from PIL import ImageDraw

from graph import Graph

from search_algorithms.ids import ids
from search_algorithms.aestrela import aestrela
from search_algorithms.ucs import ucs
from search_algorithms.bfs import bfs

from utils import create_map_image, escreve_output, define_custo

if __name__ == '__main__':
    try:
        map_name = sys.argv[1]

        inicial_y = int(sys.argv[2])
        inicial_x = int(sys.argv[3])

        final_y = int(sys.argv[4])
        final_x = int(sys.argv[5])

        algoritmo_escolhido = sys.argv[6]

        if (algoritmo_escolhido == 'aestrela'):
            heuristica = sys.argv[7]

    except:
        print ('A entrada deve seguir o padrão python main.py <map_name> <beginning_state> <final_state>')
    
    g = Graph()
    g.read_map(map_name)
    g.build_graph()
    
    img = create_map_image(g)
    
    vertice_inicial = g.width * inicial_y + inicial_x
    vertice_final = g.width * final_y + final_x

    algoritmos = {'ids': ids, 'ucs': ucs, 'bfs': bfs, 'aestrela': aestrela}

    if (algoritmo_escolhido == 'aestrela'):
        caminho = algoritmos[algoritmo_escolhido] (g, vertice_inicial, vertice_final, img, heuristica)
    else:
        caminho = algoritmos[algoritmo_escolhido] (g, vertice_inicial, vertice_final, img)
    
    img = escreve_output (caminho, g, img)
    
    # draw = ImageDraw.Draw(img)
    # draw.text((1, 0),algoritmo_escolhido + ' <' + str(inicial_y) + ', ' + str(inicial_x) + '> -> ' + ' <' + str(final_y) + ', ' + str(final_x) + '> ' + str(define_custo(g, caminho)[0]),(0,255,0))

    # if (algoritmo_escolhido == 'aestrela'):
    #     draw.text((1, 15),heuristica,(0,255,0))
    #     img.resize((1024,1024), resample=Image.NEAREST).save(algoritmo_escolhido + heuristica + '.jpeg', format="jpeg", dpi=(800,800), resolution=1024)
    # else:
    #     img.resize((1024,1024), resample=Image.NEAREST).save(algoritmo_escolhido + '.jpeg', format="jpeg", dpi=(800,800), resolution=1024)