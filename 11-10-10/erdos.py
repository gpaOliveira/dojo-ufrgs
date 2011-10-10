import sys

ERDOS = "Erdos"
INFINITY = float("inf")

def erdosSecret(author, l):

    if author.name == ERDOS:
        return 0
    
    numbers = []
    l.append(author)
    for relatedAuthor in author.related:
        if relatedAuthor not in l:
            numbers.append( erdosSecret(relatedAuthor, l) )
    if len(numbers) == 0:
        return INFINITY

    return 1 + min(numbers)
    
def erdos(author):
    return erdosSecret(author, [])

def readIn():
    authors = int(sys.stdin.next())

    while authors != 0:
        

class Author():
    def __init__(self, name):
        self.name = name
        self.related = []

    def addRelation(self, author):
        self.related.append(author)
        author.related.append(self)

    def isRelated(self, author):
        return author in self.related

