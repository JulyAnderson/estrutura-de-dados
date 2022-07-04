def busca(v, chave): 
    for i in range(len(v)): 
        if chave == v[i]: 
            return i 
    return -1
