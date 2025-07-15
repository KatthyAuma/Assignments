from collections import deque

class PalindromeChecker:
    def __init__(self, s):
        self.stack = []
        self.queue = deque()
        self.cleaned_chars = [char.lower() for char in s if char.isalnum()]

        for ch in self.cleaned_chars:
            self.stack.append(ch)
            self.queue.append(ch)

    def is_palindrome(self):
        for san in range(len(self.cleaned_chars) // 2):
            if self.stack.pop() != self.queue.popleft():
                return False
        return True
