def busca(v, i, f, chave): 
    if f < i: 
        return -1 
    m = (i + f) // 2 
    if v[m] == chave: 
        return m 
    if chave < v[m]: 
        return busca(v, i, m - 1, chave) 
    else: 
        return busca(v, m + 1, f, chave)
