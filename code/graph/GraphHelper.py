from graph.Graph_IncidenceList import GraphIncidenceList as Graph
from graph.base import Edge


class GraphHelper():
    """
    Utility functions for graph management.
    """

    @staticmethod
    def sortEdges(graph):
        """
        Return the list of edges, sorted by their weight.
        :param graph: the graph.
        :return: the list of edges, sorted by their weight.
        """
        #l = []
        #for i in range(len(graph.nodes)):
        #    curr = graph.inc[i].getFirstRecord()
        #    while curr != None:
        #        edge = CmpEdge(curr.elem.tail, curr.elem.head\
        #                , curr.elem.weight)
        #        if edge.head < edge.tail:   #sto prendendo solo meta' dei nodi
        #            l.append(edge)
        #        curr = curr.next
        l = graph.getEdges()
        l.sort()
        return l

    @staticmethod
    def buildGraph(num_nodes):
        """
        Build a sample complete graph.
        :param num_nodes number of nodes.
        :return: a sample complete graph.
        """
        graph = Graph()

        nodes = []
        for i in range(num_nodes):
            nodes.append(graph.addNode(i))

        for src in nodes:
            for dst in nodes:
                if dst.id > src.id:
                    graph.insertEdge(src.id, dst.id, num_nodes - src.id)

        return graph

"""
    @staticmethod
    def cleanGraph(graph):
        #Rende un qualsiasi grafo connesso ed elimina archi multipli.
        node_index = 0
        w = len(graph.nodes) * 100
        for _ in graph.inc.values():
            graph.inc[node_index].addAsLast(Edge(node_index,\
                    (node_index + 1) % len(graph.nodes), w))
            graph.inc[(node_index + 1) % len(graph.nodes)]\
                    .addAsLast(Edge((node_index + 1) % len(graph.nodes),\
                    node_index, w))
            w += 1
            node_index += 1
        for inc in graph.inc.values():
            heads = []
            curr = inc.getFirstRecord()
            while curr != None:
                if curr.elem.head not in heads:
                    heads.append(curr.elem.head)
                else:
                    inc.deleteRecord(curr)
                curr = curr.next

    @staticmethod
    def clean_graph_AdjMatrix(graph):
        #Rende un qualsiasi grafo connesso.
        node_index = 0
        w = len(graph.nodes) * 100
        for _ in graph.nodes:
            node2 = (node_index + 1) % len(graph.nodes)
            if graph.adj[node_index][node2] == GraphAdjacencyMatrix.EMPTY:
                graph.adj[node_index][node2] = w
                graph.adj[node2][node_index] = w
            w += 1
            node_index += 1            
"""


if __name__ == "__main__":
    graph = GraphHelper.buildGraph(5)

    graph.print()

    edges = GraphHelper.sortEdges(graph)

    print([str(i) for i in edges])