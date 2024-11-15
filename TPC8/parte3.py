def quantosPost (redeSocial):
    return len(redeSocial)

def postsAutor (redeSocial, autor):
    posts = []
    for p in redeSocial:
        if p['autor'] == autor:
            posts.append(p)
    return posts

def autores (redeSocial):
    listaAutores = []
    for post in redeSocial:
        listaAutores.append(post['autor'])
    listaAutores = sorted(listaAutores)
    return listaAutores

def insPost (redeSocial, conteudo, autor, dataCriacao, comentarios):
    ultimoId = int(redeSocial[-1]['id'].split('p')[1]) + 1
    novoId = 'p' + str(ultimoId)
    novopost = {'id': novoId, 'conteudo': conteudo, 'autor': autor, 'dataCriacao': dataCriacao, 'comentarios': comentarios}
    redeSocial.append(novopost)
    return redeSocial 

def remPost (redeSocial, id):
    novaRedeSocial = []
    for post in redeSocial:
        if post['id'] != id:
            novaRedeSocial.append(post)
    return novaRedeSocial

def postsPorAutor (redeSocial):
    dicPorAutor = {}
    listaAutores = autores(redeSocial)
    for autor in listaAutores:
        dicPorAutor[autor] = []
        for post in redeSocial:
            if post['autor'] == autor:
                dicPorAutor[autor].append(post)

    return dicPorAutor

def comentadoPor (redeSocial, autor):
    postsComentados = []
    for post in redeSocial:
        for comentarios in post['comentarios']:
            if comentarios['autor'] == autor:
                postsComentados.append(post)
    return postsComentados




