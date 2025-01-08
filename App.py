import random as rd
from colorama import Fore, Style, init
import os
from time import sleep

#Resetando a cor do prompt 
init(autoreset=True)

def prompt_cls():
    #limpa o terminal
    os.system('cls' if os.name== 'nt' else 'clear')

def welcome():
    print(Fore.GREEN + '''
    ██   ██▄       ▄   ▄█    ▄    ▄  █ ▄███▄   
    █ █  █  █       █  ██     █  █   █ █▀   ▀  
    █▄▄█ █   █ █     █ ██ ██   █ ██▀▀█ ██▄▄    
    █  █ █  █   █    █ ▐█ █ █  █ █   █ █▄   ▄▀ 
       █ ███▀    █  █   ▐ █  █ █    █  ▀███▀   
      █           █▐      █   ██   ▀           
     ▀            ▐                   
                                                                                                                                                    
o computador gera um número aleatório entre 1 e 100, e você deve adivinhar qual é o número.
O programa irá informar se o palpite do jogador está alto ou baixo e contar quantas tentativas 
foram feitas até que você acerte o número.          
''')
    input('Precione enter para continuar...')

def main():
    while True:
        num= rd.randrange(1, 100)
        n_attempt= 0
        while True:
            prompt_cls()
            print(f'Número de tentativas: {n_attempt}\n')
            n_choice = input('Qual número você acha que é: ')
            try:
                n_choice = int(n_choice)
                if n_choice == num:
                    prompt_cls()
                    print(Fore.GREEN + 'Parabéns você acertou!!')
                    quest= input('Deseja jogar novamente?(s/n)\n')
                    while quest not in ['s', 'n']:
                        print(Fore.RED + 'Por favor, responda com "s" para sim ou "n" para não.')
                        quest= input('Deseja jogar novamente?\n')
                    break
                        
                elif n_choice > num:
                    prompt_cls()
                    print(Fore.YELLOW + 'O número escolhido é maior que o número do programa')
                    n_attempt += 1
                    input(Fore.GREEN + 'Precione enter para continuar...')
                    
                elif n_choice < num:
                    prompt_cls()
                    print(Fore.RED + 'O número escolhido é menor que o número do programa')
                    n_attempt += 1
                    input(Fore.GREEN + 'Precione enter para continuar...')
            except:
                prompt_cls()
                print(Fore.RED + 'Apenas números inteiros, por favor!!! >:(')
                sleep(1)
                
        if quest == 's':
            pass
        elif quest == 'n':
            prompt_cls()
            print(Fore.GREEN + 'Foi muito bom jogar com você. Tchau!! :)')
            break
        else:
            pass

              
if __name__ == '__main__':
    welcome()
    main()