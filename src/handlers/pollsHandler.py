import os
import handlers.fileHandler as file
import repositories.pollsRepository as polls
import handlers.counterHandler as counter

pollPath = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'urnas')


def insertPollDatasFromFile():
    path = input('Digite o nome do arquivo que deseja ler (Ex: urna_01): ')
    finalPath = os.path.join(pollPath, f'{path}.txt')

    newPoll = file.readPoll(finalPath)
    if newPoll[0] in polls.polls_list:
        print(f"\n\nUrna já inserida.")
        print("="*50)
    else:
        polls.insertNewPoll(newPoll)
        printPollData(polls.polls_list)
        counter.checkVoteCount()





def printPollData(poll_data):
    print('\n'*3)
    print("\n" + "="*50)

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
        
        print("\n" + "="*50)