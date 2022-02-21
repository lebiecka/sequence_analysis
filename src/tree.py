class Leaf:
    def __init__(self, tag): 
        self.left = None
        self.right = None
        self.tag = tag 


class Node:
    def __init__(self, tag, left, right): 
        self.left = left
        self.right = right
        self.tag = tag 


class Tree(Node):

    def __init__(self, tag): 
        self.root = tag 


if __name__ == "__main__":
 
    x = Node(8, Node(3, Leaf(1), Node(6, Leaf(4), Leaf(7))),Node(10, None, Node(14, Leaf(13), None)))
    drzewo = Tree(x)

