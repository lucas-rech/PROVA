import handlers.candidatesHandler
import handlers.pollsHandler


def showMenu() :
    while(True) : 
        choice = int(input("DIGITE UMA OPÇÃO ABAIXO: \n1 - Ler arquivo com a listagem dos candidatos\n2 - Ler arquivo de urna\n3 - Listar urnas\n4 - Realizar apuração\n9 - SAIR"))

        if(choice == 9) :
            print("PROGRAMA ENCERRADO.")
            break
        elif(choice == 1) :
            handlers.candidatesHandler.insertCandidatesFromFile()
        elif(choice == 2):
            handlers.pollsHandler.insertPollDatasFromFile()
            

