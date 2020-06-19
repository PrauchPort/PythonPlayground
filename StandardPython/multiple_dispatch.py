import random
import math

class Outcome:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self):
        return self.name
    def __eq__(self, other):
        return self.value == other.value

Outcome.WIN = Outcome('win', 0)
Outcome.LOSE = Outcome('loss', 1)
Outcome.DRAW = Outcome('draw', 2)

class Item(object):
    def __str__(self):
        return self.__class__.__name__

class Paper(Item):
    def compete(self, other):
        return other.evalPaper(self)
    def evalPaper(self, other):
        return Outcome.DRAW
    def evalRock(self, other):
        return Outcome.LOSE
    def evalScissors(self, other):
        return Outcome.WIN

class Scissors(Item):
    def compete(self, other):
        return other.evalScissors(self)
    def evalPaper(self, other):
        return Outcome.LOSE
    def evalRock(self, other):
        return Outcome.WIN
    def evalScissors(self, other):
        return Outcome.DRAW

class Rock(Item):
    def compete(self, other):
        return other.evalRock(self)
    def evalPaper(self, other):
        return Outcome.WIN
    def evalRock(self, other):
        return Outcome.DRAW
    def evalScissors(self, other):
        return Outcome.LOSE

def match(item1, item2):
    print("%s <--> %s : %s" % (
      item1, item2, item1.compete(item2)))

# Generate the items:
def itemPairGen(n):
    # Create a list of instances of all Items:
    Items = Item.__subclasses__()
    for i in range(n):
        yield (random.choice(Items)(),
               random.choice(Items)())

for item1, item2 in itemPairGen(20):
    match(item1, item2)
