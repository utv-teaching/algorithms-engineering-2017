from graph.Graph import GraphBase
from graph.base import Edge, Node


class GraphAdjacencyMatrix(GraphBase):
    """
    A graph, implemented as an incidence list.
    """

    EMPTY = 0

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.adj = [] # adjacency matrix (list of lists)

    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        num_edges = 0
        for adj_row in self.adj:
            num_edges += sum(x != GraphAdjacencyMatrix.EMPTY for x in adj_row)
        return num_edges

    def addNode(self, elem):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """
        newnode = super().addNode(elem) # create a new node with the correct ID

        self.nodes[newnode.id] = newnode  # add the new node to the dictionary
        #self.adj[newnode.id] = Lista()  # create the incidence list for the new node

        #self.nodes.append(newnode) # add the node to the list of nodes

        # initialize/adapt the adjacency matrix because of the new node
        self.adj.append(len(self.adj) * [GraphAdjacencyMatrix.EMPTY])
        for l in self.adj:
            l.append(GraphAdjacencyMatrix.EMPTY)

        return newnode

    def deleteNode(self, index):
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """
        # if node does not exists, return
        if index < 0 or index >= len(self.adj):
            return

        # remove from the list of nodes
        del self.nodes[index]

        # update index of all nodes
        for i in range(index, len(self.nodes)-1):
            self.nodes[i] = self.nodes[i+1]
            self.nodes[i].id = i

        # update next node ID
        self.nextId = len(self.nodes)

        # remove all the edges starting from the node and pointing to the node,
        # that is to remove all rows/columns involving the node
        del self.adj[index]
        for l in self.adj:
            del l[index]

    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        return None if id not in self.nodes else self.nodes[id]

    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        return list(self.nodes.values())

    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        # if tail or head do not exist, return
        if tail < 0 or tail >= len(self.adj) or head < 0 or head >= len(self.adj):
            return

        # insert the weight into the adjacency matrix
        self.adj[tail][head] = weight

    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        # if tail or head do not exist, return
        if tail < 0 or tail >= len(self.adj) or head < 0 or head >= len(self.adj):
            return

        # if tail and head exist, delete the edge
        self.adj[tail][head] = GraphAdjacencyMatrix.EMPTY

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        # if tail or head do not exist, return None
        if tail < 0 or tail >= len(self.adj) or head < 0 or head >= len(self.adj):
            return None

        # if tail and head exist, but the edge does not exists
        # otherwise, return the edge
        if self.adj[tail][head] == GraphAdjacencyMatrix.EMPTY:
            return None
        else:
            return Edge(tail, head, self.adj[tail][head])

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        edges = []
        for src in range(len(self.adj)):
            for dst in range(len(self.adj)):
                if self.adj[src][dst] is not None and self.adj[src][dst] != GraphAdjacencyMatrix.EMPTY:
                    edges.append(Edge(src, dst, self.adj[src][dst]))
        return edges

    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        # if tail or head do not exist, return False
        if tail < 0 or tail >= len(self.adj) or head < 0 or head >= len(self.adj):
            return False

        # else, look for the entry in the adjacency matrix
        return self.adj[tail][head] != GraphAdjacencyMatrix.EMPTY

    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        """
        result = []
        for j in range(len(self.adj)):
            if self.adj[nodeId][j] != GraphAdjacencyMatrix.EMPTY:
                result.append(j)
        return result

    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        if nodeId not in self.nodes:
            return 0
        else:
            return sum(x != GraphAdjacencyMatrix.EMPTY for x in self.adj[nodeId])

    def print(self):
        """
        Print the graph.
        :return: void.
        """
        # if the adjacency matrix is empty ...
        if self.isEmpty():
            print ("Adjacency Matrix: EMPTY")
            return

        # else ...
        print("Adjacency Matrix:")
        s = "     "
        #for n in self.nodes:
            #s += "{:4}".format(n.id)
        #s += "\n"
        for i in range(len(self.adj)):
            s += "{:>5}".format(i)
        s += "\n"

        for i in range(len(self.adj)):
            s += "{:>5}".format(i)
            for j in range(len(self.adj[i])):
                entry = self.adj[i][j]
                s += "{:>5}".format("-" if entry == GraphAdjacencyMatrix.EMPTY else entry)
            s += "\n"
        print(s)

if __name__ == "__main__":
    graph = GraphAdjacencyMatrix()

    graph.print()

    # add nodes
    nodes = []
    for i in range(3):
        node = graph.addNode(i)
        print("Node inserted:", node)
        nodes.append(node)

    graph.print()

    # connect all nodes
    for node_src in nodes:
        for node_dst in nodes:
            if node_src != node_dst:
                print("---")
                print("Adjacent nodes {},{}: {}"
                      .format(node_src.id, node_dst.id,
                              graph.isAdj(node_src.id, node_dst.id)))
                graph.insertEdge(node_src.id, node_dst.id,
                                 node_src.id + node_dst.id)
                print("Edge inserted: from {} to {}".format(node_src.id,
                                                            node_dst.id))
                print("Adjacent nodes {},{}: {}"
                      .format(node_src.id, node_dst.id,
                              graph.isAdj(node_src.id, node_dst.id)))
                graph.print()
                print("---")

    # num nodes/edges
    print("Num Nodes:", graph.numNodes())
    print("Num Edges:", graph.numEdges())

    # degree
    for node in nodes:
        print("Degree node {}: {}".format(node.id, graph.deg(node.id)))

    # get specific node
    for node in nodes:
        print("Node {}: {}".format(node.id, graph.getNode(node.id)))

    # get all nodes
    print("Nodes:", [str(i) for i in graph.getNodes()])

    # get specific edge
    for node_src in nodes:
        for node_dst in nodes:
            print("Edge {},{}: {}".format(node_src.id, node_dst.id, graph.getEdge(node_src.id, node_dst.id)))

    # get all edges
    print("Edges:", [str(i) for i in graph.getEdges()])

    # execute a generic search
    for node in nodes:
        tree = graph.genericSearch(node.id)
        s = tree.BFS()
        print("Generic Search with root {}: {}".format(node.id,
                                                       [str(item) for item in
                                                        s]))

    # execute a BFS
    for node in nodes:
        s = graph.bfs(node.id)
        print("BFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))

    # execute a DFS
    for node in nodes:
        s = graph.dfs(node.id)
        print("DFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))

    # remove all nodes
    for node in nodes:
        graph.deleteNode(node.id)
        print("Node removed:", node.id)
        graph.print()