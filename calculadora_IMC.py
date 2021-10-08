#Import das bibliotecas usadas no projeto
import os
from time import sleep

#Função que checa o tipo de sistema operacional e limpa a tela do terminal
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#Função que chama a edição do cabeçalho no terminal
def header():
    print('=-' * 50)
    print('\n                                     Bem vindo a Calculadora\n')
    print('\n                        @@@@@@@@@        @@@@@@    @@@@@@       @@@@@@@@@@@@@@')
    print('\n                           @@@          @@@  @@    @@  @@@      @@@')
    print('\n                           @@@         @@@    @@  @@    @@@     @@@')
    print('\n                           @@@        @@@      @@@@      @@@    @@@')
    print('\n                        @@@@@@@@@    @@@                  @@@   @@@@@@@@@@@@@@\n')
    print('=-' * 50)
    print('\n')


#Função que realiza o cálculo do IMC
def imc():
    clear()
    header()

    while True:
        try:
            peso = float(input('Digite o seu peso usando o ponto " . " para separar quilos das gramas: '))
            clear()
            header()
            print(f'Digite o seu peso usando o ponto " . " para separar quilos das gramas: {peso:.2f}')
            if peso == float:
                break
            break
        except:
            print('\nDigite apenas números separando quilos e gramas por um ponto " . "')
            sleep(2)
            clear()
            header()
    
    while True:
        try:
            altura = float(input('Digite sua altura usando o ponto " . " para separar metros de centímetros: '))
            clear()
            header()
            print(f'Digite o seu peso usando o ponto " . " para separar quilos das gramas: {peso:.2f}')
            print(f'Digite sua altura usando o ponto " . " para separar metros de centímetros: {altura:.2f}')
            if altura == float:
                break
            break
        except:
            print('\nDigite apenas números separando metros e centímetros por um ponto " . "')
            sleep(2)
            clear()
            header()
            print(f'Digite o seu peso usando o ponto " . " para separar quilos das gramas: {peso:.2f}')
    
    res_imc = peso / (altura * altura)

    if res_imc < 18.5:
        print(f'\n\nSeu IMC é {res_imc:.2f} e você está abaixo do peso!\n')
        print('IMC menor que 18,5 é considerado abaixo do peso pela Organização Mundial de Saúde (OMS)')
        input('Precione ENTER para voltar ao menu.')
    elif res_imc >= 18.5 and res_imc <= 24.99:
        print(f'\n\nSeu IMC é {res_imc:.2f} e você está com peso normal!\n')
        print('IMC entre 18,5 e 24,99 é considerado normal pela Organização Mundial de Saúde (OMS)')
        input('Precione ENTER para voltar ao menu.')
    elif res_imc >= 25 and res_imc <= 34.99:
        print(f'\n\nSeu IMC é {res_imc:.2f} e você está em pré-obesidade ou acima do peso!\n')
        print('IMC entre 25 e 29,99 é considerado normal pela Organização Mundial de Saúde (OMS)')
        input('Precione ENTER para voltar ao menu.')
    elif res_imc >= 30 and res_imc <= 34.99:
        print(f'\n\nSeu IMC é {res_imc:.2f} e você está em obesidade grau um!\n')
        print('IMC entre 30 e 34,99 é considerado obesidade grau um pela Organização Mundial de Saúde (OMS)')
        input('Precione ENTER para voltar ao menu.')
    elif res_imc >= 35 and res_imc <= 39.99:
        print(f'\n\nSeu IMC é {res_imc:.2f} e você está em obesidade grau dois!\n')
        print('IMC entre 35 e 39,99 é considerado obesidade grau dois pela Organização Mundial de Saúde (OMS)')
        input('Precione ENTER para voltar ao menu.')
    else:
        print(f'\n\nSeu IMC é {res_imc:.2f} e você está em obesidade grau três ou mórbida!\n')
        print('IMC a partir de 40 é considerado obesidade grau três ou mórbida pela Organização Mundial de Saúde (OMS)')
        input('Precione ENTER para voltar ao menu.')


#Função que realiza o cálculo do consumo diário de água
def consumo_agua():
    clear()
    header()

    while True:
        try:
            peso = float(input('Digite o seu peso usando o ponto " . " para separar quilos das gramas: '))
            clear()
            header()
            print(f'Digite o seu peso usando o ponto " . " para separar quilos das gramas: {peso:.2f}')
            if peso == float:
                break
            break
        except:
            print('\nDigite apenas números separando quilos e gramas por um ponto " . "')
            sleep(2)
            clear()
            header()
    
    consumo_dia = peso * 0.035
    print(f'\nSeu consumo mínimo por dia é de {consumo_dia:.2f} litros de água!')
    input('Precione ENTER para voltar ao menu.')


#Menu principal do programa
while True:
    clear()
    header()
    print('[1] - Calculadora IMC')
    print('[2] - Consumo diário de água')
    print('[3] - Sair')

    while True:
        try:
            opcao = int(input('\nDigite a opção desejada: '))
            if opcao == int:
                break
            break
        except:
            print('\nOpção inválida, digite apenas o número correspondente!')
            sleep(2)
            clear()
            header()
            print('[1] - Calculadora IMC')
            print('[2] - Consumo diário de água')
            print('[3] - Sair')
    
    
    if opcao == 1:
        imc()
    elif opcao == 2:
        consumo_agua()
    elif opcao == 3:
        break
    else:
        print('\nOpção inválida, digite apenas o número correspondente!')
        sleep(2)
