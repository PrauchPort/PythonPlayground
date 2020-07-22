from collections import deque


class LineHistory():
    def __init__(self, lines, maxlen=3):
        self.lines = lines
        self.history = deque(maxlen=maxlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('file.txt') as f:
    lines = LineHistory(f)
    for lineno, line in enumerate(lines, 1):
        if 'python' in line:
            for lineno, hline in lines.history:
                print(f"{lineno}: {hline}")
