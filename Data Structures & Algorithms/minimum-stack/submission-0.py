# class MinStack:

#     def __init__(self):
#         self.stack = deque()
#         self.mini = 0

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.mini = min(self.mini, val)

#     def pop(self) -> None:
#         v = self.stack.pop()
#         if self.mini == v:
#             self.mini = min(self.stack)

#     def top(self) -> int:
#         self.stack[-1]        

#     def getMin(self) -> int:
#         return self.mini
        
class MinStack:
 
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
    
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]