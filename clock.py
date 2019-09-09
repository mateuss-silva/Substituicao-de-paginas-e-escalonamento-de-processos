
from multiprocessing import Process
from funcoesAuxiliares import pegaTempos, pegaPaginas


def atualizaBoolPagina(pagina, filaClock, boolSegundaChance, frames):
    for i in range(frames):

        if filaClock[i] == pagina:
            # atribui verdadeiro paro o bool da pagina pois ela existe na memoria
            boolSegundaChance[i] = True

            # Retorna e atribui true pq a pagina existia na fila e não há necessidade de substituir nenhuma página
            return True

    # Retorna false para que a página para substituição seja selecionada, pq a página reutilizada não existe na memória
    return False


# atualiza a pagina na memoria
def substituiEAtualiza(pagina, filaClock, boolSegundaChance, frames, pointer):

    while True:
        # //We found the page to replace
        if not boolSegundaChance[pointer]:
            # //Replace with new page
            filaClock[pointer] = pagina

            # //Return updated pointer
            return (pointer + 1) % frames

        # //Mark it 'false' as it got one chance
        # // and will be replaced next time unless accessed again
        boolSegundaChance[pointer] = False

        # //Pointer is updated in round robin manner
        pointer = (pointer + 1) % frames


def clock(processo, frames):

    idProcess = processo[0]
    paginasProcesso = pegaPaginas(processo[1])
    temposProcesso = pegaTempos(processo[1])
    faltaDePaginas = 0
    pointer = 0
    filaClock = [-1 for x in range(frames)]  # -1 para sinalizar que nenhuma pagina existe na fila

    boolSegundaChance = [False for x in range(frames)]  # inicializa vetor de bool com falso sinalizando o nao uso

    lenStrings = len(paginasProcesso)

    for pag in paginasProcesso:

        # //Finds if there exists a need to replace
        # //any page at all
        if not atualizaBoolPagina(pag, filaClock, boolSegundaChance, frames):
            # //Selects and updates a victim page
            pointer = substituiEAtualiza(pag, filaClock, boolSegundaChance, frames, pointer)

            # //Update page faults
            faltaDePaginas += 1

    print("Total de requerimento de páginas: %d" % len(paginasProcesso))
    print("Total de Falta de páginas: %d" % faltaDePaginas)
    print("Porcentagem de Falta de páginas: %0.2f" % ((faltaDePaginas / len(paginasProcesso)) * 100))


def startClock(processos, frames):
    procs = []
    for p in processos:
        p = Process(target=clock, args=(p, frames))
        procs.append(p)
    return procs


