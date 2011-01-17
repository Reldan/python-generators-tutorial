import sys

class file01(file):
    def __init__(self, name, mode, ni):
        file.__init__(self, name, mode)
        self.ni = ni
    def next(self):
        line = file.next(self)
        items = line.split()
        if len(items) != self.ni:
            print 'wrong number of items'
            print line
            raise StopIteration
        for itm in items:
            if itm != '1' and itm != '0':
                print 'non=0/1 item:', itm
                raise StopIteration
        return line

def main():
    f = file01(sys.argv[1], 'r', int(sys.argv[2]))
    for l in f: print l[:-1]

if __name__ == '__main__': main()
