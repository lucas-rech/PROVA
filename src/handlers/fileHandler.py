import os

def readFile(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {filePath}")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")



#Essa função é específica para leitura dos candidatos pois trata os dados conforme recebidos plos arquivos
def readCandidates(filePath):
    listOfCandidates = []
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file:

                #checa se a linha não está em branco
                if line:
                    line = line.strip()
                    code, name = line.split(' - ')
                    name = name.strip()
                    code = int(code)
                    candidate = [code, name]
                    listOfCandidates.append(candidate)
                else:
                    continue
                

    except FileNotFoundError:
        normalizedPath = os.path.normpath(filePath)
        print(f"\nArquivo de candidatos não encontrado: {normalizedPath}. Certifique-se de salvar o arquivo com o número de 'candidatos.txt' dentro da pasta data")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
    
    return listOfCandidates


def readPoll(filePath):
    pollName = []
    listOfVotes = []
    totalOfBlankVotes = 0
    totalOfNullVotes = 0
    votesCounted = 0
    votesValid = 0

    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file:

                # CONDIÇÃO PARA SALVAR O NUMERO E LOCAL DA URNA
                if 'URNA' in line:
                    pollNumber, location = line.split(' - ')
                    pollNumber = pollNumber.split(':')[1].strip()
                    location = location.split(':')[1].strip()

                    pollName.append((pollNumber, location))

                # CONDIÇÕES QUE CHECAM TOTAL DE VOTOS
                elif 'BRANCOS' in line:
                    totalOfBlankVotes = int(line.split(': ')[1].strip())
                elif 'NULOS' in line:
                    totalOfNullVotes = int(line.split(': ')[1].strip())
                elif 'COMPUTADOS' in line:
                    votesCounted = int(line.split(': ')[1].strip())
                elif 'VÁLIDOS' in line:
                    votesValid = int(line.split(': ')[1].strip())

                # LÊ UM VOTO E SALVA NA LISTA DE VOTOS DO ARQUIVO
                else:
                    data, time, identNumber, candidateVote = line.split(' - ')
                    #VALIDA SE O CODIGO DO CANDIDATO NO ARQUIVO É UM NÚMERO OU ESTÁ EM BRANCO
                    if candidateVote != '':
                        try:
                            candidateVote = int(candidateVote.strip())
                            vote = (data.strip(), time.strip(), identNumber, candidateVote)
                            listOfVotes.append(vote)
                        except ValueError:
                            continue  # Ignora a linha com erro
                    else:
                        candidateVote = 0
                        vote = (data.strip(), time.strip(), int(identNumber.strip()), candidateVote)
                        listOfVotes.append(vote)

    except FileNotFoundError:
        normalizedPath = os.path.normpath(filePath)
        print(f"Arquivo de urna não encontrado: {normalizedPath}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    dataFile = []
    dataFile.append((pollName, listOfVotes, totalOfBlankVotes, totalOfNullVotes, votesCounted, votesValid))

    return dataFile

                
                 
                


                    