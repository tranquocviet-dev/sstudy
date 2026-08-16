class LinkedList:
        class score:
                def __init__(self,index):
                        self.index = index
                        self.next = None
        def __init__(self):
                self.head = None
                self.tail = None
                self.size = 0
        def append(self, data):
