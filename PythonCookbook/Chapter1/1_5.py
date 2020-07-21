import heapq


class PriorityQueue():

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item():
    def __init__(self, string):
        self._string = string

    def __repr__(self):
        return f"Item( { self._string } )"


if __name__ == "__main__":

    pqueue = PriorityQueue()
    pqueue.push(Item("a"), 10)
    pqueue.push(Item("b"), 12)
    pqueue.push(Item("c"), 8)
    pqueue.push(Item("d"), 9)

    print(pqueue.pop())
    print(pqueue.pop())
    print(pqueue.pop())
    print(pqueue.pop())
