# yieldex.py example of yield, return in generator functions

def gy():
    x = 2
    y = 3
    yield x, y, x+y
    z = 12
    yield z/x
    print z/y
    return

def main():
    g = gy()
    print g.next() # prints x, y, x+y
    print g.next() # prints z/x
    print g.next()

if __name__ == '__main__':
    main()
