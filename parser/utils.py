class NoRollback(Exception):
    pass


class Buffered:
    layers = []

    def __init__(self, iterator):
        self.buffer = []
        self.pointer = 0
        self.iter = iterator

    def rollback(self, n):
        self.pointer -= n
        if self.layers:
            self.layers[-1] -= n

    def skip(self, n):
        for _ in range(self.pointer + n - len(self.buffer)):
            next(self)
        self.pointer += n
        if self.layers:
            self.layers[-1] += n

    def peek(self):
        if self.pointer < len(self.buffer):
            return self.buffer[self.pointer]
        self.buffer.append(next(self.iter))
        return self.buffer[-1]

    def __next__(self):
        if self.layers:
            self.layers[-1] += 1
        res = self.peek()
        self.pointer += 1
        return res

    def __enter__(self):
        self.layers.append(0)
        layer = len(self.layers)
        return lambda: self.layers[layer - 1]

    def __exit__(self, exc_type, exc_value, exc_tb):
        rb = self.layers.pop()
        if exc_type != NoRollback:
            self.pointer -= rb
        elif self.layers:
            self.layers[-1] += rb
        # supress exception
        return exc_type == NoRollback
