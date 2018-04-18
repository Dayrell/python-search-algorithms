import sys

class Graph:
    # constructor
    def __init__(self):
        self.height     = 0
        self.width      = 0
        self.name       = 'no name'
        self.list       = []
        self.graph      = {}

    # function to transform the chart list in a graph
    def build_graph (self):
        map_list    = self.list
        map_width   = self.width
        map_height  = self.height

        for pos in range (0, len(map_list)):
            
            if (map_list[pos] == '.'):
                north       = pos - map_width
                northeast   = pos - map_width + 1
                northwest   = pos - map_width
                south       = pos + map_width
                southeast   = pos + map_width + 1
                southwest   = pos + map_width - 1
                west        = pos - 1
                east        = pos + 1

                # add north
                if (north >= 0):
                    self.add_edge(pos, pos - map_width, 1.0)
                    
                # add south
                if (south <= (map_width * map_height)):
                    self.add_edge(pos, pos + map_width, 1.0)

                # if it isn't on the extreme right
                if ((pos + 1) % map_width != 0):
                    # add east
                    if (east <= (map_width * map_height)):
                        self.add_edge(pos, pos + 1, 1.0)
                    
                    # add northeast if it exists in list
                    if (northeast - 1 >= 0):
                        self.add_edge(pos, northeast, 1.5)
                    
                    # add southeast if it exists in list
                    if ((southeast + 1) <= (map_width * map_height)):
                        self.add_edge(pos, southeast, 1.5)

                # if it isn't on the extreme left
                if ((pos - 1) >= 0 and (pos % map_width != 0)):
                    # add west
                    self.add_edge(pos, west, 1.0)

                    # add northwest if it exists
                    if (northwest - 1 >= 0):
                        self.add_edge(pos, northwest - 1, 1.5)

                    # add southwest if it exists
                    if (southwest <= (map_width * map_height)):
                        self.add_edge(pos, southwest, 1.5)
    
    # function to read input text file
    def read_map (self, map_name):
        map_file    = open(map_name,'r')

        map_type    = map_file.readline().rstrip('\n')
        map_height  = int(map_file.readline().rstrip('\n').split()[1])
        map_width   = int(map_file.readline().rstrip('\n').split()[1])
        map_name    = map_file.readline().rstrip('\n')

        map_list = []
        
        for _ in range(map_height + 1):
            line = map_file.readline().rstrip('\n')

            for char in line:
                map_list.append(char)
        
        self.height = map_height
        self.width  = map_width
        self.name   = map_name
        self.list   = map_list
    
    # add new edge in graph dictionary
    def add_edge (self, u, v, weight):
        if u in self.graph:
            self.graph[u].update({v: weight})
        else:
            self.graph[u] = {v: weight}

if __name__ == '__main__':
    try:
        map_name        = sys.argv[1]
        state_beginning = sys.argv[2]
        state_final     = sys.argv[3]

        if (len(sys.argv) == 5):
            heuristic = sys.argv[4]
    except:
        print ('A entrada deve seguir o padrão python main.py <map_name> <beginning_state> <final_state>')
    
    g = Graph()
    g.read_map(map_name)
    g.build_graph()

    print (g.graph[7])