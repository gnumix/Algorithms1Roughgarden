import math
import random


class KargerAlgorithm():

    def __init__(self, edges, num_edges):
        '''
        INPUT: Dictionary, Int
        OUTPUT: None

        Initialize the object with a graph dictionary and the number of edges.
        '''
        self.edges = edges
        self.num_edges = num_edges

    def minimum_cut(self):
        '''
        INPUT: None
        OUTPUT: Int

        Compute and return the number of minimum cuts in the graph. Because
        this is an undirected graph, the number of edges is actually double.
        '''
        while len(self.edges) > 2:
            v1, v2 = self.random_edge()
            self.contract_edge(v1, v2)
        return (self.num_edges / 2)

    def random_edge(self):
        '''
        INPUT: None
        OUTPUT: Int, Int

        Randomly (and uniformly) select and return an edge from the graph.
        '''
        r = random.randint(0, self.num_edges - 1)
        for vertex, neighbors in self.edges.items():
            if len(neighbors) <= r:
                r -= len(neighbors)
            else:
                return vertex, neighbors[r]

    def contract_edge(self, v1, v2):
        '''
        INPUT: Int, Int
        OUTPUT: None

        Given 2 vertices, contract the edge between them. See comments below.
        '''
        # For each vertex that is adjacent to the second vertex, and that is
        # not the first vertex, go through that vertex's adjacent vertices,
        # and replace all instances found of the second vertex with the first
        # vertex. When finished, delete the second vertex from the graph.
        for v in self.edges[v2]:
            if v != v1:
                for i, w in enumerate(self.edges[v]):
                    if w == v2:
                        self.edges[v][i] = v1
                self.edges[v1].append(v)
        del self.edges[v2]
        # Go through the vertices that are adjacent to the first vertex. If the
        # vertex is not the second vertex, append it to a new list of vertices.
        # Otherwise, decrease the number of edges by 2 (because this is an
        # undirected graph). If the new list of adjacent vertices is not empty,
        # assign it to the first vertex. Otherwise, delete the first vertex.
        neighbors = []
        for v in self.edges[v1]:
            if v != v2:
                neighbors.append(v)
            else:
                self.num_edges -= 2
        if neighbors:
            self.edges[v1] = neighbors
        else:
            del self.edges[v1]


def read_file(filename):
    '''
    INPUT: String
    OUTPUT: Dictionary, Int

    Read in the given file name, and store the resultant graph as a dictionary,
    with the vertices as the keys and each vertex's list of adjacent vertices
    as the values. Return the graph dictionary, along with the number of edges.
    '''
    edges = {}
    num_edges = 0
    with open(filename) as f:
        for line in f:
            vertices = list(map(int, line.strip().split('\t')))
            edges[vertices[0]] = vertices[1:]
            num_edges += len(vertices) - 1
    return edges, num_edges


if __name__ == '__main__':
    filename = 'kargerMinCut.txt'
    edges, num_edges = read_file(filename)

    # Number of iterations is (n^2 * log2(n)), where n is number of vertices.
    iterations = int((len(edges) ** 2) * math.log(len(edges), 2))
    # Initial number of minimum cuts is the number of edges in the given graph.
    min_cuts = num_edges

    for i in range(iterations):
        karger = KargerAlgorithm(edges, num_edges)
        min_cuts = min(min_cuts, karger.minimum_cut())
        # Re-read in the graph, for use in the next iteration. This is actually
        # faster than using the deepcopy function from Python's copy module.
        edges, num_edges = read_file(filename)
        # Print the number of minimum cuts found so far every 100th iteration.
        if not ((i + 1) % 100):
            print('Iteration {:6} - Minimum Cut:\t{}'.format(i + 1, min_cuts))

    print('\nIteration {:6} - Minimum Cut:\t{}'.format(iterations, min_cuts))
    # Answer: 17
