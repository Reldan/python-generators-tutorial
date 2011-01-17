# getword.py

# the function getword() reads from the text file f1, returning one word
# at a time; will not return a word until an entire line has been read

def getword(fl):
    for line in fl:
        for word in line.split():
            yield word
    return
