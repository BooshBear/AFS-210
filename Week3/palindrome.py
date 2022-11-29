class Stack:
    def __init__(self):
        self.stack = []

    def putTop(self, e):
        return self.stack.append(e)

    def delTop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) < 1:
            return "Empty"
        else:
            return "Not Empty"

    def peek(self):
        return self.stack[0]
    
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        return self.queue.append(e)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if len(self.queue) < 1:
            return "Empty"
        else:
            return "Not Empty"

    def peek(self):
        return self.queue[0]

def isPalindrome(str):
    stack = Stack()
    queue = Queue()
    stack.putTop(str)
    queue.enqueue(stack.peek())
    strings = queue.peek()

    if (strings == strings[::-1]):
        return print(True)
    else:
        return print(False)
        
isPalindrome("racecar")
isPalindrome("noon")
isPalindrome("python")
isPalindrome("madam")