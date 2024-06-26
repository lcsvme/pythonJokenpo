import time

# Imprime uma linha ( ========================================== )
def line(tamanho = 42):
    print('=' * tamanho)

# Imprime um cabeçalho com a linha() e o texto centralizado no meio
def header(* texto, tamanho = 42):
    line(tamanho)
    for i in range (len(texto)):
        print(texto[i].center(42))
    line(tamanho)

# Imprime o menu com as opções recebidas no parâmetro da função
def menu(* lista):
    for i in range(0, len(lista)):
        print(f'[{i+1}]. {lista[i]}')
    line()

# Limpa o console imprimindo 20 (ou o valor passado no parâmetro) linhas vazias
def clearConsole(tempo = 1, quantidade = 20):
    time.sleep(tempo)
    for i in range(quantidade):
        print()