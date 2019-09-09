def construirProcessos(texto):
    processos = []

    linhas = texto.split("\n")  # separa o texto pro linha

    for l in linhas[:100]:
        tempo = l.split(", ")  # separa o texto por virgula e um espaço

        try:
            idProcesso = tempo.pop(0)  # remove o id da lista dos tempos
            tempo.pop()  # remove o oultimo elemento de tempo onde é uma string vazia
            processo = (idProcesso, tempo)  # cria uma tupla pra identificar cada processo

            processos.append(processo)  # guarda o processo
        except:
            print("Erro na leitura do Texto")
            continue
    return processos


def pegaTempos(tempoPaginas):  # retorna o uma lista de inteiros referentes ao tempo(brust)
    tempos = []

    for pt in tempoPaginas:
        tempos.append(pegaTempo(pt))

    return tempos


def pegaPaginas(tempoPaginas): # retorna o uma lista de inteiros referentes as paginas do processo
    paginas = []

    for pt in tempoPaginas:
        paginas.append(pegaPagina(pt))

    return paginas


def pegaTempo(pagina):  # retorna o tempo da pagina

    try:
        return int(pagina.split(":")[0])

    except:
        print("Erro ao tentar pegar  o tempo")
        return 0


def pegaPagina(pagina):  # retorna numero da pagina

    try:
        return int(pagina.split(":")[1])

    except:
        print("Erro ao tentar pegar a pagina")
        return 0



