def iterator(i, n):
    result = lookandsay(i)
    for i in range(0, n-1, 1):
        result = lookandsay(result)
    return result


def lookandsay(i):

    string = str(i)
    final = ""
    
    ant = string[0]
    cont = 1
    
    for i in range(1, len(string), 1):
        if string[i] == ant:
            cont += 1 
        else:
            final += str(cont) + ant
            ant = string[i]
            cont = 1

    final += str(cont) + ant

    return int(final)

