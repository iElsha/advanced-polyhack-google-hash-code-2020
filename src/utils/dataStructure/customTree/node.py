class Node:
    """
    A node of a tree to store the data of a file
    """

    def __init__(self, value):
        """

        :param value:String name of the file
        """
        self.value = value
        self.children = []
        self.children_str = []  # avoid to check in every node

    def is_leave(self):
        return len(self.children) == 0

    def insert(self, child, father):
        """

        :param child: NodeFile
        :param father:String name of the father
        :return:
        """
        self.children_str.append(child.value)
        if self.value == father:
            self.children.append(child)
        elif not self.is_leave():
            for i in range(len(self.children)):
                if father in self.children[i].children_str or self.children[i].value == father:
                    self.children[i].insert(child, father)

    def get_nb_node(self):
        """

        :return: numbers of node(s) in the tree
        """
        nb = 1
        for i in range(len(self.children)):
            nb += self.children[i].get_nb_node()
        return nb

    def search(self, v):
        node = None
        if self.value == v:
            node = self
        elif not self.is_leave():
            for i in range(len(self.children)):
                if node is not None:
                    return node
                node = self.children[i].search(v)
        return node

    def remove_node(self, v):
        """
        remove a node from the tree
        :param v:String name of the file
        :return:
        """
        n = False
        if len(self.children) != 0:
            self.children_str.remove(v)
            for i in range(len(self.children)):
                if v == self.children[i].value:
                    self.children.pop(i)
                    return True
            for k in range(len(self.children)):
                if n is True:
                    return n
                n = self.children[k].remove_node(v)
            return n
