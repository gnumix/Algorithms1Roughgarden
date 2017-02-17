import networkx as nx
import heapq


def dijkstra_algorithm(graph, start):
    '''
    INPUT: NetworkX Graph, Int
    OUTPUT: NetworkX Graph

    Given the source node, use Dijkstra's algorithm to calculate all other
    nodes' shortest paths from the source node. Return the resulting graph.
    '''
    heap = []
    graph.node[start]['explored'] = True
    graph.node[start]['distance'] = 0
    graph, heap = push_heap(graph, heap, start)
    # While the min-heap still contains distances and their tuple of nodes.
    while heap:
        # Pop from min-heap to return node-pair with the shortest distance.
        distance, (node1, node2) = heapq.heappop(heap)
        # First node has been explored, but second node may not have been.
        if not graph.node[node2]['explored']:
            graph.node[node2]['explored'] = True
            graph.node[node2]['distance'] = graph.node[node1]['distance'] + \
                graph[node1][node2]['weight']
            graph, heap = push_heap(graph, heap, node2)
    return graph


def push_heap(graph, heap, node):
    '''
    INPUT: NetworkX Graph, List, Int
    OUTPUT: NetworkX Graph, List

    Use a min-heap to keep track of the distances found, in ascending order.
    '''
    for neighbor in graph[node]:
        # If a node's neighbor has not yet been explored, add the weight of
        # that neighbor to the current node's distance, and add to min-heap.
        if not graph.node[neighbor]['explored']:
            distance = graph.node[node]['distance'] + \
                graph[node][neighbor]['weight']
            heapq.heappush(heap, (distance, (node, neighbor)))
    return graph, heap


if __name__ == '__main__':
    graph = nx.Graph()
    # By default, a node has not been explored, and its distance is infinity.
    explored = False
    distance = float('inf')
    with open('dijkstraData.txt') as f:
        for line in f:
            line = line.strip().split('\t')
            node1 = int(line[0])
            graph.add_node(node1, explored=explored, distance=distance)
            for pair in line[1:]:
                node2, weight = list(map(int, pair.split(',')))
                graph.add_edge(node1, node2, weight=weight)

    # All other nodes' shortest paths will be found with respect to this node.
    start = 1
    graph = dijkstra_algorithm(graph, start)
    nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for node in nodes:
        print('Shortest Path Between Node {:1} & Node {:3}:\t{:4}'
              .format(start, node, graph.node[node]['distance']))

    '''
    Answer = {
        7:      2599,
        37:     2610,
        59:     2947,
        82:     2052,
        99:     2367,
        115:    2399,
        133:    2029,
        165:    2442,
        188:    2505,
        197:    3068
    }
    '''
