import time
from interface import *

# Verifica se o arquivo existe tentando abrir ele.
def fileExists(nome):
    try:
        a = open(nome, 'rt') # RT = Read Text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
# Cria um arquivo com o nome passado no parâmetro da função.
def createFile(nome):
    try:
        a = open(nome, 'wt') # WT = Write Text
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')

# Salva o cadastro realizado pelo usuário
def setUserData(arquivo, user):
    try:
        with open(arquivo, 'r+') as a: # R+ = Read and Write
            linhas = a.readlines()

            # Lê linha por linha no arquivo
            for lin in linhas:
                userSalvo, _, _, _, _, _ = lin.strip().split(';')  # Tira o ; do arquivo .txt separando os dados em duas listas.

                # Verifica se o usuário informado já foi cadastrado anteriormente.
                if user == userSalvo:
                    print('Este usuário já existe!')
                    return
            
            # Caso o usuário não exitir, solicita a senha para o cadastro:
            senha = input('DIGITE SUA SENHA: ')
            verificarSenha = input('DIGITE A SENHA NOVAMENTE: ')

            # Loop para verificar se o usuário re-digitou a senha corretamente
            while verificarSenha != senha:
                print('A senha não coincide. Tente novamente!')
                verificarSenha = input('DIGITE A SENHA NOVAMENTE: ')

            # Escreve no 'userData.txt' as informações do usuário e com uma contagem de pontos em 0.
            a.write(f'{user};{senha};0;0;0;0\n') # Escreve no userData.txt os dados informados pelo usuário.

    except Exception as e:
        print(f'Houve um erro ao escrever os dados: {e}')
    else:
        time.sleep(0.5)
        print(f'Cadastro de {user.upper()} adicionado!')
        a.close()
        time.sleep(1)
        clearConsole()
        


# Verifican se os dados informados no login coincidem com os dados cadastrados.
def verifyLogin(arquivo, user):
    # Declara a quantidade de tentativas para o usuário acertar a senha.
    tentativas = 3

    # Enquanto as tentativas não forem zeradas, continuará verificando o login.
    while tentativas > 0:
        try:
            with open(arquivo, 'r+') as f: # R+ = Read and Write
                linhas = f.readlines()
                f.seek(0) # Volta ao início do arquivo.

                userEncontrado = False

                # Passa linha por linha no arquivo.
                for lin in linhas:
                    userSalvo, senhaSalva, _, _, _, _ = lin.strip().split(';')  # Tira o ; do arquivo .txt separando os dados em duas listas.

                    # Verifica se o usuário digitado existe.
                    if userSalvo == user:
                        userEncontrado = True
                        senha = input('DIGITE SUA SENHA: ')
                        # Verifica se a senha informada é a mesma da senha cadastrada.
                        if senhaSalva == senha:
                            header('LOGIN FEITO COM SUCESSO!')
                            clearConsole()
                            return True
                        # Se a senha não coincidir, diminui uma tentativa.
                        else:
                            print('SENHA INVÁLIDA, TENTE NOVAMENTE!')
                            tentativas -= 1
                            break
                
                # Caso o usuário não for encontrado, diminui uma tentativa.
                if not userEncontrado:
                    print('USUÁRIO NÃO ENCONTRADO, TENTE NOVAMENTE!')
                    tentativas -= 1
                    user = input('DIGITE O NOME DE USUÁRIO: ')

        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return
        except Exception as e:
            print(f"Erro ao verificar o login: {e}")
            return
    
    # Se o limite de tentativas acabar, o programa encerra.
    header('NÚMERO MÁXIMO DE TENTATIVAS ATINGIDO!')


# Salva a quantidade de pontos do jogador.
def setPoints(arquivo, user, pontos, vitorias, derrotas, empates):
    try:
        with open(arquivo, 'r+') as f: # R+ = Read and Write
            linhas = f.readlines()
            f.seek(0)

            # Lê linha por linha e verifica o usuário.
            for lin in linhas:
                dados = lin.strip().split(';')
                senha = dados[1]
                # Se o usuário coincidir com o usuário logado, atualiza as estatísticas do jogador.
                if dados[0] == user:
                    lin = f'{user};{senha};{pontos};{vitorias};{derrotas};{empates}\n'
                f.write(lin)
            f.truncate()

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao alterar os pontos: {e}")


# Obtém a quantidade de pontos do jogador.
def getPoints(arquivo, user, imprimir = False):
    try:
        a = open(arquivo, 'rt') # RT = Read Text
    except:
        print('Houve um erro ao ler o arquivo!')
    else:
        # Lê linha por linha e verifica se o usuário.
        for linha in a:
            dados = linha.split(';') # Tira o ; do arquivo .txt separando os dados em uma lista.
            # Verifica se o user (índice 0 da lista) é o passado pelo usuário.
            dados[0] = dados[0].replace('\n', '') # 0 = Nome

            if dados[0] == user:
                # Remove o breakline de cada índice da lista.
                pontos = dados[2].replace('\n', '') # 2 = Pontos
                vitorias = dados[3].replace('\n', '') # 3 = Vitórias
                derrotas = dados[4].replace('\n', '') # 4 = Derrotas
                empates = dados[5].replace('\n', '') # 5 = Empates
                
                # Se o parâmetro imprimir for verdadeiro, imprime as estatísticas do jogador.
                if imprimir == True:
                    line()
                    print(f'VITÓRIA: +100', 'DERROTA: -75'.rjust(28))
                    header(f'PONTUAÇÃO: {pontos}\n',
                            f'VITÓRIAS: {vitorias}',
                            f'DERROTAS: {derrotas}',
                            f'EMPATES: {empates}')

                # Retorna os valores encontrados no arquivo.
                return int(pontos), int(vitorias), int(derrotas), int(empates)
        # Se não encontrar nenhum dado correspondente, retorna valores padrão.
        return 0, 0, 0, 0
    finally:
        a.close()


# Obtém o ranking de maior quantidade de pontos do .txt
def getRanking(arquivo):
    try:
        a = open(arquivo, 'rt') # RT = Read Text
    except:
        print('Houve um erro ao ler o arquivo!')
    else:
        dados = []

        # Lê linha por linha no arquivo.
        for linha in a:
            userSalvo, _, pontos, _, _, _ = linha.split(';') # Tira o ; do arquivo separando os dados em uma lista.
            dados.append((userSalvo, pontos)) # Adiciona o usuário e os pontos na lista dados.

        # Imprime o cabeçalho da função
        header('RANKING')
        print(f'{'USER'.rjust(1)} {'PONTOS'.center(68)}\n')
        
        # Faz uma lista ordenada pela maior quantidade de pontos
        ranking = sorted(dados, key = lambda x: x[1], reverse = True)

        # Comprimento total desejado para cada linha
        comprimentoTotal = 40

        # Loop que imprime o ranking de pontos em ordem crescente dos usuários
        for i, (userSalvo, pontos) in enumerate(ranking):
            ranking = sorted(dados, key = lambda x: x[1], reverse = True) # Atualiza a lista de ranking
            espacosLivres = comprimentoTotal - len(userSalvo) - len(str(i+1)) - len(pontos)

            # Imprime os usuários e a pontuação em ordem do maior para o menor
            print(f'{i+1}. {userSalvo.upper()}{' ' *  espacosLivres}{pontos}')
        a.close()