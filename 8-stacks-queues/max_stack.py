# max() O(1) time | O(n) space
class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.cache = []

    def push(self, number) -> None:
        self.stack.append(number)

        if not self.cache:
            self.cache.append(number)
        else:
            max_cache = self.cache[-1]
            self.cache.append(max(max_cache, number))

    def pop(self, number) -> int:
        self.cache.pop()
        return self.stack.pop()

    def max(self, number) -> int:
        return self.cache[-1]
