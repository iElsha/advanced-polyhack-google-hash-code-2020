class Tree:
    """
    A tree to store the data of the file's dependencies
    """

    def __init__(self, root_node):
        """
        create a tree
        :param root_node:NodeFile the root node or None
        """
        self.root = root_node
        self.nb_node = 0


    def empty(self):
        """

        :return: is the tree empty ? true if empty otherwise false
        """
        return self.root is None or len(self.root.children) == 0

    def get_nb_node(self):
        """

        :return: numbers of node(s) in the tree
        """
        return self.root.get_nb_node()

    def insert(self, child, father):
        """

        :param child: FileNode
        :param father:String name of the father
        :return:
        """
        self.nb_node += 1
        if self.root is None or father is None:
            self.root = child
        else:
            self.root.insert(child, father)

    def search(self, v):
        return self.root.search(v)

    def remove_node(self, v):
        """

        :param v:String name of the file
        :return:
        """
        self.nb_node -= 1
        return self.root.remove_node(v)
