# testgw.py, test of getword; counts words and computes average length
# of words

# usage: python testgw.py [filename]
# (stdin) is assumed if no file is specified)

from getword import *

def main():
    import sys
    # determine which file we'll evaluate
    try:
        f = open(sys.argv[1])
    except:
        f = sys.stdin
    # generate the iterator
    w = getword(f)
    wcount = 0
    wltot = 0
    for wrd in w:
        wcount += 1
        wltot += len(wrd)
    print "%d words, average length %f" % (wcount, wltot/float(wcount))

if __name__ == '__main__':
    main()
