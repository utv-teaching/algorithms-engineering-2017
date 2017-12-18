class Node:
    """
    The graph basic element: node.
    """

    def __init__(self, id, value):
        """
        Constructor.
        :param id: node ID (integer).
        :param value: node value.
        """
        self.id = id
        self.value = value

    def __eq__(self, other):
        """
        Equality operator.
        :param other: the other node.
        :return: True if ids are equal; False, otherwise.
        """
        return self.id == other.id

    def __str__(self):
        """
        Returns the string representation of the node.
        :return: the string representation of the node.
        """
        return "[{}:{}]".format(self.id, self.value)


class Edge:
    """
    The graph basic element: (weighted) edge.
    """

    def __init__(self, tail, head, weight=None):
        """
        Constructor.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        """
        self.head = head
        self.tail = tail
        self.weight = weight

    def __cmp__(self, other):
        """
        Compare two edges with respect to their weight.
        :param other: the other edge to compare.
        :return: 1 if the weight is greater than the other;
        -1 if the weight is less than the other; 0, otherwise.
        """
        if self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0

    def __lt__(self, other):
        """
        Less than operator.
        :param other: the other edge.
        :return: True, if the weight is less than the others; False, otherwise.
        """
        return self.weight < other.weight

    def __gt__(self, other):
        """
        Greater than operator.
        :param other: the other edge.
        :return: True, if the weight is greater than the others; False, otherwise.
        """
        return self.weight > other.weight

    def __eq__(self, other):
        """
        Equality operator.
        :param other: the other edge.
        :return: True if weights are equal; False, otherwise.
        """
        return self.weight == other.weight

    def __str__(self):
        """
        Returns the string representation of the edge.
        :return: the string representation of the edge.
        """
        return "({},{},{})".format(self.tail, self.head, self.weight)


if __name__ == "__main__":
    node_src = Node(0, "SRC")
    print('Node created:', node_src)
    node_dst = Node(1, "DST")
    print('Node created:', node_dst)
    edge = Edge(node_src.id, node_dst.id, 1.5)
    print('Edge created:', edge)
