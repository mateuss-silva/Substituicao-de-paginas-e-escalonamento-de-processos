from multiprocessing import Process
from funcoesAuxiliares import pegaTempo, pegaPagina
from roundRobin import roundRobin
from collections import deque


def multilevel_Feedback(processo, frames, quantum=5):

    idProcesso = processo[0]
    paginasProcesso = deque(processo[1])  # fila com popleft em O(1)


def StartMultilevelFeedback(processos, frames):  # inicia os processos utilizando a função de Multilevel_Feedback
    procs = []
    for p in processos:
        p = Process(target=multilevel_Feedback, args=(p, frames))
        procs.append(p)
    return procs
