from priorityQueue.PQbinaryHeap import PQbinaryHeap as PriorityQueue
from graph.base import Edge
from graph.GraphHelper import GraphHelper
from tree.treeArrayList import TreeArrayListNode as TreeNode
from tree.treeArrayList import TreeArrayList as Tree


INFINITE = float("inf")


def BellmanFord(graph, root):
    """
    Bellman-Ford's algorithm for the computation of the shortest path.
    The algorithm assumes a graph implemented as incidence list.
    ---
    Time Complexity: O(|V|*|E|)
    Memory Complexity: O()

    :param graph: the graph.
    :param root: the root node to start from.
    :return: the list of distances.
    """
    nodes = len(graph.nodes)

    # initialize distances
    dist = nodes * [INFINITE]
    dist[root] = 0

    # apply the relaxation step |V| times
    for i in range(nodes):
        for j in range(len(graph.inc)):
            curr = graph.inc[j].getFirstRecord()
            while curr is not None:
                edge = curr.elem
                tail = edge.tail
                head = edge.head
                weight = edge.weight
                # relaxation step
                if dist[tail] + weight < dist[head]:
                    dist[head] = dist[tail] + weight
                curr = curr.next

    return dist


def FloydWarshall(graph):
    """
    Floyd-Warshall's algorithm for the computation of the shortest path.
    The algorithm assumes a graph implemented as incidence list.
    ---
    Time Complexity: O(|V|^3)
    Memory Complexity: O()

    :param graph: the graph.
    :return: the list of distances.
    """
    nodes = len(graph.nodes)

    # initialize distances:
    # dist[i,j]=inf, if (i,j) not in E
    # dist[i,i]=0,
    # dist[i,j]=w(i,j), if (i,j) in E
    dist = [[INFINITE] * nodes for i in range(nodes)]
    for i in range(nodes):
        dist[i][i] = 0
        curr = graph.inc[i].getFirstRecord()
        while curr is not None:
            edge = curr.elem
            dist[edge.tail][edge.head] = edge.weight
            curr = curr.next

    # apply the relaxation step |V| times
    for i in range(nodes):
        for x in range(nodes):
            for y in range(nodes):
                # relaxation step
                if dist[x][i] + dist[i][y] < dist[x][y]:
                    dist[x][y] = dist[x][i] + dist[i][y]

    return dist[0]


def Dijkstra(graph, root):
    """
    Dijkstra's algorithm for the computation of the shortest path.
    The algorithm assumes a graph implemented as incidence list.
    This implementation leverages the BinaryTree and PriorityQueue data
    structures.
    ---
    Time Complexity: O(|E|*log(|V|))
    Memory Complexity: O()

    :param graph: the graph.
    :param root: the root node to start from.
    :return: the shortest path.
    """
    n = len(graph.nodes)

    # initialize weights:
    # d[i] = inf for every i in E
    # d[i] = 0, if i == root
    currentWeight = n * [INFINITE]
    currentWeight[root] = 0


    # initialize the tree
    tree = Tree(TreeNode(root))
    mstNodes = {root}
    mstWeight = 0

    # initialize the frontier (priority queue)
    pq = PriorityQueue()
    pq.insert((root,Edge(root,root,0)), 0)

    # while the frontier is not empty ...
    while not pq.isEmpty():
        # pop from the priority queue the node u with the minimum weight
        pq_elem = pq.popMin()
        node = pq_elem[0]
        # if node not yet in the tree, update the tree
        if node not in mstNodes:
            edge = pq_elem[1]
            treeNode = TreeNode(node)
            father = tree.foundNodeByElem(edge.tail)
            father.sons.append(treeNode)
            treeNode.father = father
            mstNodes.add(node)
            mstWeight += edge.weight

        # for every edge (u,v) ...
        curr = graph.inc[node].getFirstRecord()
        while curr is not None:
            edge = curr.elem # the edge
            head = edge.head # the head node of the edge
            # if node v not yet added into the tree, push it into the priority
            # queue and apply the relaxation step
            if head not in mstNodes:
                tail = edge.tail
                weight = edge.weight
                currWeight = currentWeight[head]
                distTail = currentWeight[tail]
                pq.insert((head, edge), distTail + weight)
                # relaxation step
                if currWeight == INFINITE:
                    currentWeight[head] = distTail + weight
                elif distTail + weight < currWeight:
                    currentWeight[head] = distTail + weight
            curr = curr.next

    return currentWeight


if __name__ == "__main__":
    graph = GraphHelper.buildGraph(5)

    graph.print()

    print("BellmanFordMoore:")
    distances = BellmanFord(graph, 0)
    print("\tDistances:", distances)

    print("FloydWarshall:")
    distances = FloydWarshall(graph)
    print("\tDistances:", distances)

    print("Dijkstra:")
    distances = Dijkstra(graph, 0)
    print("\tDistances:", distances)
