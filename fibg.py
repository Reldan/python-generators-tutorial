# fibg.py generator example

def fib():
    fn2 = 1
    fn1 = 1
    while True:
        (fn1, fn2, oldfn2) = (fn1+fn2, fn1, fn2)
        yield oldfn2
