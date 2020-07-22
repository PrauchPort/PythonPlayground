class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def __iter__(self):
        return iter(self._children)

    def add_child(self, node):
        self._children.append(node)


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.add_child(n2)
    n1.add_child(n3)
    for child in n1:
        print(child)
