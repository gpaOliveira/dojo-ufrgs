
def substrMatchPar(tokens):
    count = 0  
    firstIndex = -1      
    lastIndex = -1
    for i in range(len(tokens)):
        if tokens[i] == '(':
            if count == 0:
                firstIndex = i
            count += 1
        
        if tokens[i] == ')':
            count = count - 1
            if count == 0:
                lastIndex = i

        if lastIndex != -1 and firstIndex != -1:
           return ( tokens[firstIndex+1:lastIndex] , tokens[lastIndex+1:])

def tokens2list(tokens):
    pass

def i2p(infix):

    if infix == "":
        return ""

    tokens = infix.split()

    pseudoPostfix = parseList(tokens)
    return " ".join(pseudoPostfix)
                          
def parseList(tokens):    
    
    #base case
    if len(tokens) == 1:
        return tokens
    
    #others
    if tokens[0] == '(':
        first, rest = substrMatchPar(tokens)
    else:
        first = [tokens[0]]
        rest = tokens[1:]
                
    op = rest[0]
    second = rest[1:]        
        
    if second[0] == '(':
        second, _ = substrMatchPar(second)
        
    return  parseList(first) + parseList(second) + [op]
