class fibnum:
    def __init__(self):
        self.fn2 = 1 # "f_(n-2)"
        self.fn1 = 1 # "f_(n-1)"
    def next(self): #next() is the heart of any iterator
        (self.fn1, self.fn2, oldfn2) = (self.fn1+self.fn2,self.fn1,self.fn2)
        return oldfn2
    def __iter__(self):
        return self

class fibnum20:
    def __init__(self):
        self.fn2 = 1 # "f_{n-2}"
        self.fn1 = 1 # "f_{n-1}"
    def next(self):
        (self.fn1, self.fn2, oldfn2) = (self.fn1+self.fn2,self.fn1,self.fn2)
        if oldfn2 > 20: raise StopIteration
        return oldfn2
    def __iter__(self):
        return self
