import pyfiglet
import hashlib
import json
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Listas para armazenar dados
usuarios = []
livros = []
def criptografar_senha(senha):
    salt = "biblioteca_digital_2025"
    return hashlib.sha256((senha + salt).encode()).hexdigest()

def verificar_senha(senha_digitada, hash_armazenado):
    return criptografar_senha(senha_digitada) == hash_armazenado

def salvar_usuarios():
    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

def cadastro_usuario():
    usuario = {
        "id": len(usuarios) + 1,
        "username": input("Nome de usuário: "),
        "password_hash": criptografar_senha(input("Insira sua senha: ")),
        "tipo": input("Adm/User: "),
        "nome_completo": input("Insira seu nome completo: ")
    }
    usuarios.append(usuario)
    salvar_usuarios()
    print(Fore.GREEN + f"\nUsuário '{usuario['username']}' cadastrado com sucesso!\n")

def login():
    if not usuarios:
        print(Fore.RED + "Nenhum usuário cadastrado. Cadastre um antes de logar.\n")
        return False

    while True:
        username = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        for a in usuarios:
            if a["username"] == username:
                if verificar_senha(senha, a["password_hash"]):
                    print(Fore.GREEN + "\nLogin realizado com sucesso!\n")
                    return True
                else:
                    print(Fore.RED + "\nSenha incorreta. Tente novamente.\n")
                    break
        else:
            print(Fore.RED + "\nUsuário não encontrado. Tente novamente.\n")

def sair():
    salvar_usuarios()
    print(Fore.RED + "\nSaindo do sistema...")
    sys.exit()

def cadastro_livro():
    livro = {
        "isbn": input("Digite o ISBN do livro: "),
        "titulo": input("Digite o título do livro: "),
        "autor": input("Digite o autor: "),
        "categoria": input("Digite a categoria: "),
        # "disponivel": 
    }
    livros.append(livro)
    print(Fore.GREEN + f"\nLivro '{livro['titulo']}' cadastrado com sucesso!\n")
    
tt = pyfiglet.figlet_format("\n=== Biblioteca Digital ===\n" )
print(Fore.BLUE + Style.BRIGHT + tt)
# Menu principal
while True:
    print(Fore.CYAN + "Menu\n")
    print(Fore.GREEN + "1 - Login")
    print(Fore.YELLOW +"2 - Cadastro de Usuário")
    print(Fore.RED + "3 - Sair")
    opc = input(Fore.MAGENTA + "O que deseja fazer: ")

    if opc == "1":
        login()
    elif opc == "2":
        cadastro_usuario()
    elif opc == "3":
        sair()
    else:
        print("Escolha uma opção válida!!")

