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
