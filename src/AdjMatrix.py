class AdjMatrix:
    def __init__(self, size):
        self.size = size
        self.entries = [[False] * size for _ in range(size)]

    def size(self):
        return self.size

    def get(self, row, col):
        return self.entries[row][col]

    def add_edge(self, row, col):
        self.entries[row][col] = True

    def remove_edge(self, row, col):
        self.entries[row][col] = False

    def equals(self, other):
        if self.size != other.size:
            return False
        for i in range(self.size):
            for j in range(self.size):
                if self.get(i, j) != other.get(i, j):
                    return False
        return True
    
    def cycleLens(self):
        cycles = []
        curCycle = 1

        nodes = [i for i in range(self.size)]

        x = nodes.pop(0)
        prev = x

        while len(nodes) > 0:
            # set x
            i = 0
            while i == prev or self.get(x, i) == 0:
                i += 1
            if i in nodes:
                prev = x
                x = i
                nodes.remove(i)
                curCycle += 1
            else:
                cycles.append(curCycle)
                curCycle = 1
                if len(nodes) > 0:
                    x = nodes.pop(0)
                    prev = x

        cycles.append(curCycle)

        # print(cycles, "cycles")

        return sorted(cycles)

    def __str__(self):
        result = ""
        for i in range(self.size):
            for j in range(self.size):
                if self.entries[i][j]:
                    result += "1 "
                else:
                    result += "0 "
            result += "\n"
        return result
