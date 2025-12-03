import funcoes as fc
import os
amarelo = "\033[0;33m"
resetar = "\033[0m" 
branco_negrito = "\033[1;37m"
vermelho_negrito = "\033[1;31m"

os.system('cls')

def menu():
    print(fc.cabecalho)                                                                                                                                                   
    print("-" * 123)
    print(f'''
    {amarelo}[1]{resetar} {branco_negrito}Pesquisa por Produto {resetar}
    {amarelo}[2]{resetar} {branco_negrito}Listar Todos {resetar}
    {amarelo}[3]{resetar} {branco_negrito}Incluir Novo Produto {resetar}
    {amarelo}[4]{resetar} {branco_negrito}Alterar Produto {resetar}
    {amarelo}[5]{resetar} {branco_negrito}Excluir Produto {resetar}
    {vermelho_negrito}[S] Sair {resetar}
''')
    print("-" * 50)

def main():
    dados = fc.load_txt()
    while True:
        menu()
        op = input(f"{branco_negrito}Digite a opção desejada: {resetar}").upper()

        if op == "1":
            os.system("cls")
            fc.pesquisar(dados)
        elif op == "2":
            os.system("cls")
            fc.listar(dados)
        elif op == "3":
            os.system("cls")
            fc.incluir(dados)
        elif op == "4":
            os.system("cls")
            fc.alterar(dados)
        elif op == "5":
            os.system("cls")
            fc.excluir(dados)
        elif op == "S":
            break
        else:
            print("Opção inválida!")

        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()

