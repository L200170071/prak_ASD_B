#No 4a
class Queue(object):
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(), 'Antrian sedang Kosaosng'
        return self.qlist.pop(0)
    def getFrontMost(self):
        return self.qlist[0]
a = Queue()
a.enqueue(10)
a.enqueue(32)
a.enqueue(12)
a.enqueue(59)
a.enqueue(33)
print ('item paling depan = ', a.getFrontMost())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())

#No 4b
class Queue(object):
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(), 'Antrian sedang Kosaosng'
        return self.qlist.pop(0)
    def getRearMost(self):
        return self.qlist[-1]
a = Queue()
a.enqueue(10)
a.enqueue(32)
a.enqueue(28)
a.enqueue(59)
a.enqueue(33)
print ('item paling belakang = ', a.getRearMost())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())

#No 5
class PriorityQueue(object):
    def __init__(self):
        self.qlist=[]
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self, data, priority):
        entry=_PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        assert not self.isEmpty()
        x=[]
        for i in self.qlist:
            x.append(i.priority)
        a=x.index(min(x))
        return self.qlist.pop(a).item
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item=data
        self.priority=priority
b=PriorityQueue()
b.enqueue("Muhammadiyah", 5)
b.enqueue("Universitas", 1)
b.enqueue("Surakarta", 7)
print (b.dequeue())
print (b.dequeue())
print (b.dequeue())
