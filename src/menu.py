import handlers.candidatesHandler
import handlers.counterHandler
import handlers.pollsHandler


def showMenu() :
    
    while(True) : 
        print('\n')
        choice = int(input("DIGITE UMA OPÇÃO ABAIXO: \n1 - Ler arquivo com a listagem dos candidatos\n2 - Ler arquivo de urna\n3 - Listar urnas\n4 - Realizar apuração\n9 - SAIR"))

        if(choice == 9) :
            print("\nPROGRAMA ENCERRADO.")
            break
        elif(choice == 1) :
            print('\n\n\n' + "="*50)
            handlers.candidatesHandler.insertCandidatesFromFile()
            print("="*50)
        elif(choice == 2):
            print('\n\n\n')
            handlers.pollsHandler.insertPollDatasFromFile()
            print('\n')
            handlers.counterHandler.checkVoteCount()
            print("="*50)
        elif(choice == 3):
            print('\n\n\n' + "="*50)
            handlers.pollsHandler.listPolls()
            print("="*50)
        elif(choice == 4):
            print('\n\n\n' + "="*50)
            handlers.counterHandler.carryCount()
            print("="*50)
        else:
            print("\n" + "="*50 + "\nDigite um número válido.\n" + "="*50)
            continue
            

