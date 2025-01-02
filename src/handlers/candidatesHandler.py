import os
import handlers.fileHandler as file
import repositories.candidatesRepository as candidates

candidates_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'candidatos.txt')


def listCandidates():
    file.readFile(candidates_path)

def insertCandidatesFromFile():

    #validação para caso usuário tente registrar a lista mais de uma vez
    if not candidates.candidates_list :
        candidates.insertMultipleCandidates(file.readCandidates(candidates_path))
        printCandidatesList(candidates.candidates_list)
    else :
        print('\n\nA lista de candidatos já foi registrada.\n')
        print('='*50)
    

def printCandidatesList(data_list):
    for candidate in data_list:
        code, name = candidate
    
        print(f"CANDIDATO: {name} - {code}")


