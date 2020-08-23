
from multiprocessing import Process
from funcoesAuxiliares import pegaTempos, pegaPaginas


def fifo(processo, frames):

    # inicialização das variaveis
    filaFifo = []
    faltaDePaginas = 0
    paginaAntiga = 0
    idProcesso = processo[0]

    paginasProcesso = pegaPaginas(processo[1])  # pega as paginas do processo
    temposProcesso = pegaTempos(processo[1])  # pega os tempos do processo

    # boolFaltouPagina = False

    for pag in paginasProcesso:

        try:

            if pag not in filaFifo:

                if len(filaFifo) < frames:          # se ainda tiver pagina disponivel, utilize
                    filaFifo.append(pag)            # adiciona a pagina na fila
                else:                               # caso nao tenha pagina disponivel

                    filaFifo[paginaAntiga] = pag    # substitui a pagina mais antiga quando os frames acabam
                    paginaAntiga = (paginaAntiga + 1) % frames  # Reiniciar o topo da fila quando os frames acabarem
                faltaDePaginas += 1                 # quantidade de falta de paginas
                # boolFaltouPagina = True
            else:
                # boolFaltouPagina = False
                pass

        except:
            print("Erro no FIFO")

    print("Total de requerimento: %d" % len(paginasProcesso))
    print("Total de Falta de páginas: %d" % faltaDePaginas)
    print("Porcentagem de Falta de páginas: %0.2f" % ((faltaDePaginas / len(paginasProcesso)) * 100))


def startFifo(processos, frames):
    procs = []
    for p in processos:
        p = Process(target=fifo, args=(p, frames))
        procs.append(p)
    return procs
