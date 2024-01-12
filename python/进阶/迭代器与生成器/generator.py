class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.next = None

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next


node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)  # node1 node2 node3


def gen(num):
    while num > 0:
        tmp = yield num
        if tmp is not None:
            num = tmp
        num -= 1


g = gen(5)
first = next(g)  # first = g.send(None)
print(f"first: {first}")  # first: 5
print(f"send: {g.send(10)}")  # send: 9

for i in g:
    print(i)  # 8 7 6 5 4 3 2 1
