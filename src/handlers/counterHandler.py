#ESSE MÓDULO É RESPONSÁVEL PELA CONTAGEM DE VOTOS DOS CANDIDATOS E VALIDAÇÃO DE QUAL DOS CANDIDATOS ESTÁ GANHANDO A CADA CONTAGEM DE URNA

import repositories.candidatesRepository as candidates
import repositories.pollsRepository as polls



def checkVoteCount():
    votes_count = { candidate[0]: 0 for candidate in candidates.candidates_list }
    
    for poll in polls.polls_list:
        pollVotes = poll[1] #Os votos estão no segundo elemento de cada lista da urna

        for vote in pollVotes:
            candidateCode = vote[3] #o código do candidato é o 4ª item da tupla
            if candidateCode in votes_count:
                votes_count[candidateCode] += 1

# validação caso o usuário não tenha inserido a lista de candidatos no sistema
    if votes_count:
        winner = max(votes_count, key=votes_count.get)
        print(f"Após a leitura da urna, o candidato com mais votos é: {winner} com {votes_count[winner]} votos.")
    else:
        print(f"Não há candidatos registrados! Insira os candidatos para contar os votos!\n")
