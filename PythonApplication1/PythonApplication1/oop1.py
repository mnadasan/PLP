class MaxSize:
    def __init__(self, initval=None):
        self.val = initval
       
    def __get__(self, obj, objtype):
        print("Getting: %s" % self.val)
        return self.val

    def __set__(self, obj, val):
        print("Setting: %s" % val)
        self.val = val

    def __delete__(self, obj):
        print("Deleting: %s" % self.val)
        del self.val

class Queue:
    """A quick implementation of a FIFO queue
       data structure."""
    max_size = MaxSize()
    def __init__(self, init_list=[]):
        self.list = init_list
    def push(self, obj):
        self.list.insert(0,obj)
    def pop(self):
        item = self.list.pop()
        return item
    def is_empty(self):
        return self.list == []
    pass


q = Queue()
s = q.max_size
q.max_size = 10
q.push("lolo")
q.push("lololo")
print(q.pop())
print(q.is_empty())
print(q.pop())
print(q.is_empty())
del q.max_size
print (q.max_size)
