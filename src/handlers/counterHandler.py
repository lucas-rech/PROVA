#ESSE MÓDULO É RESPONSÁVEL PELA CONTAGEM DE VOTOS DOS CANDIDATOS E VALIDAÇÃO DE QUAL DOS CANDIDATOS ESTÁ GANHANDO A CADA CONTAGEM DE URNA

import repositories.candidatesRepository as candidates
import repositories.pollsRepository as polls


#Checa a apuração de votos a cada leitura de urna
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
        print(f"Não há candidatos registrados! Insira os candidatos para contar os votos!")


#Função 4 de apuração
def carryCount():
    candidatesList = []
    totalOfVotes, totalOfValid, totalOfNull, totalOfBlank = 0, 0, 0, 0

    # caso os repositórios de candidatos OU de urnas estejam vazios, não irá realizar a apuração
    if len(polls.polls_list) or len(candidates.candidates_list) < 1:
        return print("Não há dados suficientes para realizar a apuração.")

    #faz a contagem dos totais de votos
    for poll in polls.polls_list:
        totalOfBlank += poll[2]
        totalOfNull += poll[3]
        totalOfVotes += poll[4]
        totalOfValid += poll[5]

    #esse bloco de for é responsável por fazer a contagem de votos de cada candidato, um por um. Ele acessa cada um dos elementos de urna e identifica quantas vezes o codigo desse mesmo candidato se repéte e adiciona a uma variável contadora
    for cand in candidates.candidates_list:
        code, name = cand
        votesCounter = 0

        for poll in polls.polls_list:
            pollVotes = poll[1]

            for vote in pollVotes:
                if vote[3] == code:
                    votesCounter += 1

        #criada uma nova lista para facilitar a ordenação dos candidatos no output futuro
        candidate = code, name, votesCounter
        candidatesList.append(candidate)

    #uso de lambda (função anonima para facilitar o algoritmo de sort da lista, poderia ser feita uma função para isso mas seria mais extenso)
    sortedCandidates = sorted(candidatesList, key=lambda x: x[2], reverse=True)

    i = 1
    for candidate in sortedCandidates:
        percentageOfVotes = (candidate[2] / totalOfVotes) * 100
        candidateToString = f"{i}° - {candidate[1]} - {candidate[0]} - Quantidade de votos: {candidate[2]} - {round(percentageOfVotes, 2)}%"
        
        if i == 1:
            candidateToString += "- ELEITO"
        else:
            candidateToString += "- NÃO ELEITO"
        
        print(candidateToString)
        i += 1

    print(f"\nTOTAL DE URNAS APURADAS: {len(polls.polls_list)}\nTOTAL DE VOTOS COMPUTADOS: {totalOfVotes}\nTOTAL DE VOTOS EM BRANCO: {totalOfBlank}\nTOTAL DE VOTOS NULOS: {totalOfNull}\nTOTAL DE VOTOS VÁLIDOS: {totalOfValid}\n" + "="*50)



    #print(candidatesList)

    



