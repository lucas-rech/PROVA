# Sistema de Apuração de Votos

Este projeto foi desenvolvido como parte de um trabalho final, cujo objetivo é criar um sistema de apuração de votos de uma eleição. O sistema foi feito em Python e é responsável por contabilizar os votos dos eleitores, apresentar boletins parciais durante a apuração e gerar um relatório final com os resultados da eleição.

## Descrição do Sistema

O sistema realiza a leitura de arquivos de texto contendo informações sobre candidatos e urnas. Durante o processo de apuração, o sistema calcula o total de votos válidos, nulos, brancos, e computa os votos para cada candidato, atualizando em tempo real quem está liderando a eleição. Ao final da apuração, o sistema exibe um boletim final com os resultados, incluindo o número de votos por candidato, a porcentagem de votos e a informação se o candidato foi **ELEITO** ou **NÃO ELEITO**.

## Funcionalidades

- **Leitura de Arquivo com Candidatos**: O sistema lê um arquivo contendo os dados dos candidatos (número e nome).
- **Leitura de Arquivos de Urnas**: O sistema processa múltiplos arquivos que representam votos de diferentes urnas. Cada voto contém a data, hora, o número do eleitor e o número do candidato.
- **Apuração em Tempo Real**: O sistema imprime boletins parciais a cada vez que o candidato líder muda durante a apuração dos votos.
- **Relatório Final**: Após a apuração, o sistema gera e exibe:
  - Lista dos candidatos ordenados por número de votos.
  - O total de votos válidos, nulos, brancos, e computados.
  - O número total de urnas apuradas.
  - A porcentagem de votos de cada candidato em relação ao total apurado.
  - A informação de quem foi **ELEITO** ou **NÃO ELEITO**.

### Opções do Menu

1. **Ler arquivo com a listagem dos candidatos**: Lê o arquivo contendo os dados dos candidatos (número e nome).
2. **Ler arquivo de urna**: Lê os arquivos das urnas, processando os votos.
3. **Listar urnas**: Exibe as urnas que foram lidas até o momento.
4. **Realizar apuração**: Inicia o processo de apuração dos votos e exibe os boletins parciais.
9. **SAIR**: Encerra o sistema.

## Entradas do Sistema

1. **Arquivo de Candidatos**: Um arquivo texto contendo uma lista com o número (com 5 dígitos) e o nome dos candidatos. A lista deve conter no mínimo 5 candidatos.
   - Exemplo de formato:
     ```
     29531 - GUILHERME
     38172 - LUIZA
     58391 - ROBERTO
     65984 - FABIOLA
     47203 - ANDRÉ
     ```

2. **Arquivos de Urnas**: Conjunto de arquivos texto representando as urnas. Cada linha de arquivo contém:
   - Data, Hora, Identificador do Eleitor (10 dígitos) e Número do Candidato Escolhido.
   - Exemplo de formato:
     ```
     24/11/2023 - 20:00 - 1098765432 - 58391
     24/11/2023 - 20:01 - 1087654321 - 65984
     24/11/2023 - 20:02 - 1076543210 - 29531
     ```

## Estrutura do Projeto

- **candidatesRepository.py**: Contém a lista de candidatos e funções para manipulação dos dados dos candidatos.
- **pollsRepository.py**: Contém a lista das urnas e funções para manipulação dos dados de votos.
- **counterHandler.py**: Lida com a contagem dos votos e apuração em tempo real.
- **menu.py**: Exibe o menu de opções para o usuário.
- **main.py**: Arquivo principal que inicializa o programa e gerencia o fluxo de execução.

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/lucasrech/contador-de-votos.git

2. Navegue até a pasta do projeto:
    ```bash
    cd nome-do-repositorio

3. Execute o script principal:
    ```bash
    python main.py

