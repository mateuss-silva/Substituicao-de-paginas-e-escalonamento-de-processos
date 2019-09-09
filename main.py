import fifo
import lru
import clock
import otimo
import roundRobin
from multilevelFeedback import StartMultilevelFeedback
from funcoesAuxiliares import construirProcessos

ref = """
        https://github.com/int-main/Page-Replacement-Algorithms-in-Python/
        https://www.geeksforgeeks.org/optimal-page-replacement-algorithm/
        https://www.geeksforgeeks.org/second-chance-or-clock-page-replacement-policy/
        https://www.geeksforgeeks.org/lru-cache-implementation/
        https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/
        https://www.geeksforgeeks.org/program-round-robin-scheduling-set-1/
        https://www.geeksforgeeks.org/multilevel-paging-in-operating-system/
        """


def chamaClock(processos, frames):
    print("-" * 31, "###__CLOCK__###", "-" * 32)
    pro = clock.startClock(processos, frames)
    for p in pro:
        p.start()
    for p in pro:
        p.join()


def chamaFIFO(processos, frames):
    print("-" * 32, "###__FIFO__###", "-" * 32)
    pro = fifo.startFifo(processos, frames)
    for p in pro:
        p.start()
    for p in pro:
        p.join()


def chamaLRU(processos, frames):
    print("-" * 32, "###__LRU__###", "-" * 33)
    pro = lru.startLRU(processos, frames)
    for p in pro:
        p.start()
    for p in pro:
        p.join()


def chamaOtimo(processos, frames):
    print("-" * 32, "###__OTIMO__###", "-" * 31)

    pro = otimo.startOtimo(processos, frames)
    for p in pro:
        p.start()
    for p in pro:
        p.join()


def chamaRoundRobin(processos, quantum):
    print("-" * 28, "###__ROUND_ROBIN__###", "-" * 29)

    pro = roundRobin.startRoundRobin(processos, quantum)
    for p in pro:
        p.start()
    for p in pro:
        p.join()


def chamaMultilevelFeedback(processos, frames):
    print("-" * 25, "###__MULTILEVEL_FEEDBACK__###", "-" * 24)

    pro = StartMultilevelFeedback(processos, frames)
    for p in pro:
        p.start()
    for p in pro:
        p.join()


def printSubPag():
    print("-" * 80)
    print("|", " " * 26, "SUBSTITUIÇÃO DE PAGINAS", " " * 25, "|")
    print("-" * 80)


def printEsc():
    print("-" * 80)
    print("-" * 26, "ESCALONAMENTO DE PROCESSOS", "-" * 26)
    print("-" * 80)


def main():
    # Average waiting time = 450.68182 Average turn around time = 483.09091 proc = (1, ['43:0', '48:0', '11:1',
    # '52:1', '35:1', '39:1', '15:2', '22:2', '26:3', '62:4', '12:4', '7:4', '38:4','20:5', '23:5', '64:5', '42:8',
    # '63:8', '46:8', '19:9', '21:9', '5:9'])
    quantum = 5
    quantFrames20, quantFrames30 = 20, 30  # quantidade de quadros de memória disponível igual a 20 e 30 para os testes
    processos = construirProcessos(open('referencias1.txt', 'r').read())  # Processos da entrada

    printSubPag()

    # chamaFIFO(processos.copy(), quantFrames30)
    # chamaLRU(processos.copy(), quantFrames30)
    # chamaOtimo(processos.copy(), quantFrames30)
    # chamaClock(processos.copy(), quantFrames30)

    printEsc()

    # chamaRoundRobin(processos.copy(), quantum)
    # chamaMultilevelFeedback(processos.copy(), quantFrames30)


if __name__ == "__main__":
    main()
