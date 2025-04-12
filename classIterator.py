class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        self.a += 1
        return self.a
    
myClass = myNumbers()
myIter = iter(myClass)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
