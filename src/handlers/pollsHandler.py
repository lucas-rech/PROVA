import os
import handlers.fileHandler as file
import repositories.pollsRepository as polls

pollPath = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'urnas')


def insertPollDatasFromFile():
    path = input('Digite o nome do arquivo que deseja ler (Ex: urna_01): ')
    finalPath = os.path.join(pollPath, f'{path}.txt')

    try:
        newPoll = file.readPoll(finalPath)
        
        #caso o arquivo tenha retornado nulo, não será inserido no repositório de urnas
        if newPoll != [([], [], 0, 0, 0, 0)]:
            print('\n' + "="*50)
            if newPoll[0] in polls.polls_list:
                print(f"\n\nUrna já inserida.")
                print("="*50)
            else:
                polls.insertNewPoll(newPoll)
                printPollData(polls.polls_list)

    except Exception as e:
        print(f"Erro inesperado: {e}")


def printPollData(poll_data):

    for poll in poll_data:
        poll_name, votes, blank_votes, null_votes, total_votes, valid_votes = poll

        for poll_info in poll_name:
            poll_number, location = poll_info

        print(f"Urna {poll_number} - {location}")
        print(f"Total de Votos Computados: {total_votes}")
        print(f"Votos Válidos: {valid_votes}")
        print(f"Votos Nulos: {null_votes}")
        print(f"Votos Brancos: {blank_votes}")
        print("\nVotos Registrados:")

        for vote in votes:
            if isinstance(vote, tuple) and len(vote) == 4:
                data, time, ident_number, candidate_vote = vote
                print(f"Data: {data}, Hora: {time}, Identificação: {ident_number}, Voto no Candidato: {candidate_vote}")
            else:
                print("Formato de voto inválido:", vote)

def listPolls() :
    
    if len(polls.polls_list) >= 1:
        for poll in polls.polls_list:
            #Descompacta cada tupla iterável
            code, name = poll[0][0]
            dataFormated = f"Código: {code} - Nome: {name}"
            print(dataFormated)
    else:
        print("Nenhuma urna registrada.")