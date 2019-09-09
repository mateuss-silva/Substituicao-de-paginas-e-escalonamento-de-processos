from multiprocessing import Process
from funcoesAuxiliares import pegaTempos, pegaPaginas


def otimo(processo, frames):
    # inicialização de variaveis
    filaOtimo = []
    faltaDePaginas = 0

    idProcesso = processo[0]
    paginasProcesso = pegaPaginas(processo[1])  # pega a lista de pagins do processo
    temposProcesso = pegaTempos(processo[1])  # pega a lista de tempos do processo

    # boolFaltouPagina = False

    ocorrencias = [None for i in range(frames)]  # inicializa as ocorrencias vazias
    for i in range(len(paginasProcesso)):

        try:

            pag = paginasProcesso[i]
            tempo = temposProcesso[i]

            if pag not in filaOtimo:  # se a pagina ainda nao foi exacutada na fila

                if len(filaOtimo) < frames:  # se tiver pagina disponivel adicione a pagina na fila
                    filaOtimo.append(pag)
                else:  # caso nao tenha frame disponivel
                    for x in range(len(filaOtimo)):  # faz a previsao de proximas ocorrencias
                        # se o elemento da fila nao for ocorrer nas paginas restantes
                        if filaOtimo[x] not in paginasProcesso[i + 1:]:
                            filaOtimo[x] = paginasProcesso[i]
                            # substitua o elemento atual da fila pela pagina ainda nao processada
                            break
                        else:
                            # caso contrario adicione a posição da proxima ocorrencia do elemento atual (filaOtimo[x])
                            # na lista de previsao de ocorrencias, na posição atual X
                            ocorrencias[x] = paginasProcesso[i + 1:].index(filaOtimo[x])
                    else:
                        # caso o laço nao break(todos elementos da fila estao nas proximas paginas a serem processadas)
                        filaOtimo[ocorrencias.index(max(ocorrencias))] = paginasProcesso[i]

                faltaDePaginas += 1
                # boolFaltouPagina = True
            else:
                # boolFaltouPagina = False
                pass

        except:
            print("Erro no Otimo")

    print("Total de requerimento: %d" % len(paginasProcesso))
    print("Total de Falta de páginas: %d" % faltaDePaginas)
    print("Porcentagem de Falta de páginas: %0.2f" % ((faltaDePaginas / len(paginasProcesso)) * 100))


def startOtimo(processos, frames):
    procs = []
    for p in processos:
        p = Process(target=otimo, args=(p, frames))
        procs.append(p)
    return procs
