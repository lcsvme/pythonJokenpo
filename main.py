from interface import *  # Importa as funções do módulo interface.
from arquivo import *  # Importa as funções do módulo arquivo.
import random
import time

arquivo = 'userData'  # Define o nome do arquivo que será criado.

# Verifica se já existe um arquivo criado no sistema.
if not fileExists(arquivo):
    createFile(arquivo)  # Se não, cria um arquivo.


# Obtém a opção (Login, Cadastrar, Sair) do jogador.
def getUserData():

    # Imprime o menu de escolhas para o jogador.
    header('LOGIN')
    menu('Login',
         'Cadastrar',
         'Sair')
    
    userOption = input('DIGITE O NÚMERO DA OPÇÃO: ')
    options = {'1': 'Login', '2': 'Cadastrar', '3': 'Sair'}  # Dicionário com as opções.

    # Verifica se o usuário digitou uma opção válida.
    if userOption in options:
        return options[userOption]
    # Se não, imprime uma mensagem de erro.
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        return getUserData()  # Chama a função novamente para o usuário poder digitar uma opção válida.


# Obtém a escolha (Pedra, Papel, Tesoura) do jogador.
def getUserChoice():
    # Imprime o menu de escolhas para o jogador.
    header('JOKENPÔ')
    menu('Pedra', 'Papel', 'Tesoura', 'Ver Pontuação', 'Ver Ranking', 'Sair')

    userChoice = input('DIGITE O NÚMERO DA SUA ESCOLHA: ')
    choices = {'1': 'Pedra', '2': 'Papel', '3': 'Tesoura', '4': 'Ver Pontuação', '5': 'Ver Ranking', '6': 'Sair'}  # DIcionário com as opções.

    # Verifica se o usuário digitou uma escolha válida.
    if userChoice in choices:
        return choices[userChoice]
    # Se não, imprime uma mensagem de erro.
    else:
        print('ESCOLHA INVÁLIDA! TENTE NOVAMENTE!')
        return getUserChoice()  # Chama a função novamente para o usuário poder digitar uma opção válida.


# Obtém a escolha aleatória do computador.
def getComputerChoice():
    choices = ['Pedra', 'Papel', 'Tesoura']  # Lista com as opções disponíveis para o computador.
    return random.choice(choices)  # Retorna uma escolha aleatória para o computador.


# Obtém o vencedor da partida atual.
def getWinner(userChoice, computerChoice):
    # Mostra quais escolhas foram feitas pelo usuário e o computador.
    print(f'SUA ESCOLHA: {userChoice}')
    print('O COMPUTADOR ESCOLHEU... ', end='')
    time.sleep(1)
    print(computerChoice)

    # Verifica se o jogo deu empate.
    if userChoice == computerChoice:
        return 'EMPATE!'
    # Verifica se o usuário ganhou a partida.
    elif (userChoice == 'Pedra' and computerChoice == 'Tesoura') or \
         (userChoice == 'Papel' and computerChoice == 'Pedra') or \
         (userChoice == 'Tesoura' and computerChoice == 'Papel'):
        return 'VOCÊ GANHOU!'
    # Caso nenhuma das condições passem, significa que o usuário perdeu a partida.
    else:
        return 'VOCÊ PERDEU!'


# Controla o fluxo do jogo, gerenciando o login do usuário, a execução das rodadas de jogo e a atualização dos pontos.
def playGame():
    # Enquanto o usuário não fazer o login, não irá jogar!
    while True:
        userOption = getUserData()  # Guarda o retorno da função getUserData() dentro da variável userOption.

        # Caso o usuário escolha sair, o programa irá encerrar.
        if userOption == 'Sair':
            header('SAINDO!')
            return
        # Caso o usuário escolha a opção login, irá verificar os dados.
        elif userOption == 'Login':
            user = input('DIGITE O NOME DE USUÁRIO: ')
            if verifyLogin(arquivo, user):
                break
        # Caso o usuário escolha a opção cadastrar, irá requisitar os dados para o cadastro.
        elif userOption == 'Cadastrar':
            user = input('DIGITE O NOME DE USUÁRIO: ').strip().lower()
            setUserData(arquivo, user)       

    # Se login for realizado com sucesso, o jogo irá começar .
    while True:
        userChoice = getUserChoice()  # Guarda o retorno da função getUserChoice() dentro da variável userChoice.

        # Obtém os pontos, vitórias, derrotas e empates do usuário do .txt, sem imprimir os resultados na tela.
        pontos, vitorias, derrotas, empates = getPoints(arquivo, user, imprimir = False)

        # Caso o usuário escolha sair, o programa irá encerrar.
        if userChoice == 'Sair':
            header('SAINDO!')
            return
        # Caso o jogador escolher ver a pontuação, irá mostrar os dados e continuar o jogo.
        elif userChoice == 'Ver Pontuação':
            clearConsole()
            getPoints(arquivo, user, True)
            time.sleep(1.5)
            continue
        # Caso o jogador escolher ver o ranking, irá mostrar o ranking e continuar o jogo.
        elif userChoice == 'Ver Ranking':
            clearConsole()
            getRanking(arquivo)
            time.sleep(1.5)
            continue

        computerChoice = getComputerChoice() # Guarda o retorno da função getComputerChoice() dentro da variável computerChoice.
        result = getWinner(userChoice, computerChoice) # Guarda o retorno da função getWinner() dentro da variável result.
        time.sleep(1)
        header(result)
        time.sleep(1)

        # Atualiza a contagem de pontos
        if result == 'VOCÊ GANHOU!':
            clearConsole(0.75)
            vitorias += 1 # Atualiza a contagem de vitórias
            pontos += 100 # Atualiza a quantidade de pontos

        elif result == 'VOCÊ PERDEU!':
            clearConsole(0.75)
            derrotas += 1 # Atualiza a contagem de derrotas
             # Atualiza a quantidade de pontos, não permitindo o usuário ficar com pontos negativos.
            if pontos >= 75:
                pontos -= 75
            if pontos == 50:
                pontos -= 50
            if pontos == 25:
                pontos -= 25

        elif result == 'EMPATE!':
            clearConsole(0.75)
            empates += 1 # Atualiza a contagem de empates

        setPoints(arquivo, user, pontos, vitorias, derrotas, empates)

# Inicia o jogo
if __name__ == "__main__":
    playGame()