from queue import Queue
from threading import Thread

# A thread that produces data


def producer(out_q):
    while True:
        # Produce some data

        out_q.put(2)

# A thread that consumes data


def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data


q = Queue()
t1 = Thread(target=consumer, args=(q, ))
t2 = Thread(target=producer, args=(q, ))
t1.start()
t2.start()
