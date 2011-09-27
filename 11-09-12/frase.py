def numero_linhas(frase):
    numeroDeLinhas = 1
    for i in frase:
        if i == '\n':
            numeroDeLinhas += 1
        
    return numeroDeLinhas

def quebra_linha(frase, colunas):
    lista = list(frase)
    tamanhoFrase = len(frase)
    
    while tamanhoFrase > colunas:
        if (tamanhoFrase <= colunas):
            return frase
        else:
            a = colunas
            if frase[colunas] != ' ' and tamanhoFrase < colunas+1 and frase[colunas+1] == ' ':
                lista[colunas+1] = '\n'
            elif frase[colunas] == ' ':
                lista[colunas] = '\n' 
            else:
                while frase[a] != ' ':
                    a -= 1
                lista[a] = '\n'
            
            tamanhoFrase -= a
            lista = lista[(a+1):]

    return "".join (lista)
