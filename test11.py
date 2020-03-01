class Queue:
    def __init__(self):
        self.e_s = []
    def enQ(self,data):
        self.e_s.append(data)
    def dQ(self):
        if len(self.e_s) == 1:
            return self.e_s.pop()
        item = self.e_s.pop()
        dq_item = self.dQ()
        self.e_s.append(item)
        return dq_item

Q = Queue()

Q.enQ(10)
Q.enQ(5)
Q.enQ(20)
print(Q.dQ())
Q.enQ(100)
print(Q.dQ())
print(Q.dQ())
print(Q.dQ())