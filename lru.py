
from multiprocessing import Process
from collections import deque
from funcoesAuxiliares import pegaTempos, pegaPaginas


def lru(processo, frames):

    # inicialização de variaveis
    filaLRU = deque()
    st = []
    faltaDePaginas = 0
    paginaMaisAntiga = 0
    # boolFaltouPagina = False

    idProcess = processo[0]
    paginasProcesso = pegaPaginas(processo[1])
    temposProcesso = pegaTempos(processo[1])

    for pag in paginasProcesso:

        try:

            if pag not in filaLRU:

                if len(filaLRU) < frames: # se tiver pagina disponivel nos frames adicione na fila
                    filaLRU.append(pag)

                else:                               # substitui a pagina mais antiga quando os frames acabam
                    filaLRU[paginaMaisAntiga] = pag
                    paginaMaisAntiga = (paginaMaisAntiga + 1) % frames # reinicia o topo da fila quando os frames acabam

                # boolFaltouPagina = True
                faltaDePaginas += 1

            else:
                filaLRU.remove(pag)  # atualiza a pagina informando que foi recentemente usada(joga page para o inicio)
                filaLRU.appendleft(pag)
                # boolFaltouPagina = False

        except:
            print("Erro no LRU")

    print("Total de requerimento de páginas: %d" % len(paginasProcesso))
    print("Total de Falta de páginas: %d" % faltaDePaginas)
    print("Porcentagem de Falta de páginas: %0.2f" % ((faltaDePaginas / len(paginasProcesso)) * 100))


def startLRU(processos, frames):
    procs = []
    for p in processos:
        p = Process(target=lru, args=(p, frames))
        procs.append(p)
    return procs
