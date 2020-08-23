from multiprocessing import Process
import funcoesAuxiliares as aux


# calcula os tempos de espera dos processos
def calculaTempoDeEspera(quantPaginas, tempoDeBurst, tempoDeEspera, quantum=5):
    tempoDeBurstRestante = tempoDeBurst.copy()  # copia o tempo de burst
    tempo = 0  # tempo inicial

    # enquanto existir tempo de Brust(processamento) execute
    while True:
        parar = True

        for i in range(quantPaginas):

            # se existir tempo para processar
            if tempoDeBurstRestante[i] > 0:
                parar = False

                if tempoDeBurstRestante[i] > quantum:
                    # se o tempo para processar for maior que a unidade de processamento permitida, somente processe
                    # essa quantidade de tempo e subtraia a quantidade do burst restante e guarde o tempo

                    tempo += quantum
                    tempoDeBurstRestante[i] -= quantum

                # se o tempo restante é menor ouu igual que o maximo possivel,
                # indica que a pagina do processo ja vai ser finalizada
                else:

                    # quantidade de tempo que o processo teve para ser finalizado
                    tempo = tempo + tempoDeBurstRestante[i]

                    # o tempo de espera é o tempo de processamento menos o tempo total
                    tempoDeEspera[i] = tempo - tempoDeBurst[i]

                    # completou a execução
                    tempoDeBurstRestante[i] = 0

        # quando todos tempos de processamentos (brusts) forem iguais a zero, pare
        if parar == True:
            break


# calcula o tempo de rotacao das paginas do processo
def calculaTempoDeRotacao(quantPaginas, tempoDeBurst, tempoDeEspera, tempoDeRotacao):

    for i in range(quantPaginas):
        tempoDeRotacao[i] = tempoDeBurst[i] + tempoDeEspera[i]


def roundRobin(processo, quantum=5):  # Function to calculate average waiting and turn-around times

    idProcesso = processo[0]
    paginasProcesso = aux.pegaPaginas(processo[1])
    tempoDeBurst = aux.pegaTempos(processo[1])
    quantPaginas = len(paginasProcesso)

    # inicialização com 0 para a espera e rotação
    tempoDeEspera = [0] * quantPaginas
    tempoDeRotacao = [0] * quantPaginas

    # calcula o tempo de espera para todos processos
    calculaTempoDeEspera(quantPaginas, tempoDeBurst, tempoDeEspera, quantum)

    # calcula o tempo de rotação(o tempo que demora para uma pagina ser executada e voltar a ser exacutada novamente)
    # para todas paginas
    calculaTempoDeRotacao(quantPaginas, tempoDeBurst, tempoDeEspera, tempoDeRotacao)

    tempoDeEsperaTotal = 0
    tempoDeRotacaoTotal = 0

    for i in range(quantPaginas):
        tempoDeEsperaTotal = tempoDeEsperaTotal + tempoDeEspera[i]
        tempoDeRotacaoTotal = tempoDeRotacaoTotal + tempoDeRotacao[i]
    print("Tempo médio de espera = %.5f " % (tempoDeEsperaTotal / quantPaginas))
    print("Tempo médio de rotação = %.5f " % (tempoDeRotacaoTotal / quantPaginas))


def startRoundRobin(processos, quantum=5):  # cria os processos e retorna em uma lista
    procs = []
    for p in processos:
        p = Process(target=roundRobin, args=(p, quantum))
        procs.append(p)
    return procs
