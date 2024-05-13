class MyList (list):
    
    def __init__(self, lst):
        super.__init__(lst)
        
    def pop(self):
        return self.pop()
    
    def push(self, item):
        self.append(item)
        
if __name__ == "__main__":
    a = MyStack([])
    a.push(1)
    a.push(2)
    print(a.pop())