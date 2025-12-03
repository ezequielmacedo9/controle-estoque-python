import os
from tabulate import tabulate
# Cores do Padrão ANSI
preto = "\033[0;30m"
vermelho = "\033[0;31m"
verde = "\033[0;32m"
amarelo = "\033[0;33m"
azul = "\033[0;34m"
magenta = "\033[0;35m"
ciano = "\033[0;36m"
branco = "\033[0;37m"
# Cores em negrito
preto_negrito = "\033[1;30m"
vermelho_negrito = "\033[1;31m"
verde_negrito = "\033[1;32m"
amarelo_negrito = "\033[1;33m"
azul_negrito = "\033[1;34m"
magenta_negrito = "\033[1;35m"
ciano_negrito = "\033[1;36m"
branco_negrito = "\033[1;37m"
# Resetar cor
resetar = "\033[0m"   

#Criando um cabeçalho pro programa
cabecalho = (f"""{magenta_negrito }                                                                                                                             
                                                                                                                            
▄█████ ▄████▄ ███  ██ ██████ █████▄  ▄████▄ ██     ██████  ████▄  ██████  ██████ ▄█████ ██████ ▄████▄ ▄█████▄ ██  ██ ██████ 
██     ██  ██ ██ ▀▄██   ██   ██▄▄██▄ ██  ██ ██     ██▄▄    ██  ██ ██▄▄    ██▄▄   ▀▀▀▄▄▄   ██   ██  ██ ██ ▄ ██ ██  ██ ██▄▄   
▀█████ ▀████▀ ██   ██   ██   ██   ██ ▀████▀ ██████ ██▄▄▄▄  ████▀  ██▄▄▄▄  ██▄▄▄▄ █████▀   ██   ▀████▀ ▀█████▀ ▀████▀ ██▄▄▄▄ 
                                                                                                           ▀▀               {resetar}""")
# Carregar txt
def load_txt():
    dados = {} #Dicionário recebendo arquivo TXT 
    with open("dados.txt", "r", encoding="utf-8") as arquivo: #Convertendo o encoding para BR e carregando TXT
        for linha in arquivo:
            linha = linha.strip().split(";") #Tirando os espaços e separando a cada ;
            id = int(linha[0])
            nome = linha[1]
            preco = float(linha[2]) #Colocando cada elemento numa variável
            qtd = int(linha[3])

            dados[id] = [nome, preco, qtd]
    return dados

# Salvar txt
def salvar_txt(dados):
    with open("dados.txt", "w", encoding="utf-8") as arquivo: #Convertendo o encoding novamente para não corromper o TXT E escrevendo no TXT
        for id, info in dados.items():
            arquivo.write(f"{id};{info[0]};{info[1]:.2f};{info[2]}\n")
# Listar Produto
def listar(dados):
    tabela = []
    for id, info in dados.items():
        nome = info[0]
        preco = f"R$ {float(info[1]):.2f}".replace(".", ",") #Convertendo o preço para ter duas casas decimais e substituindo . por ,
        qtd = int(info[2])
        tabela.append([id, nome, preco, qtd]) #Classificando elementos (ID, NOME, PREÇO E QUANTIDADE)

    print (cabecalho)
    print("-" * 123)
    print(tabulate(tabela,headers=[f"{branco_negrito}ID", "Nome", "Preço", "Quantidadeb"],tablefmt="rounded_grid")) #Criando uma tabela
    print("-" * 123)
    input(f"{branco_negrito}Pressione ENTER para voltar ao menu{resetar}")

# Pesquisar Produto
def pesquisar(dados):
    while True:
        print(cabecalho)
        print("-" * 123)
        busca = input(f"{branco_negrito}Digite o nome para pesquisar ou pressione ENTER para listar todos : {resetar}").lower().strip()

        tabela = [] # Lista que vai armazenar os produtos encontrados
        achou = False # para indicar se houve alguma correspondência

        for id, info in dados.items(): # Varre todos os itens (id = chave, info = valores)
            nome = info[0] #Colocando numa variável a informação na posição 0 da lista
            preco = f"R${float(info[1]):.2f}".replace(".", ",") #Convertendo o preço para ter duas casas decimais e substituindo . por ,
            qtd = int(info[2])

            if busca in nome.lower(): #Pesquisa não apenas se colocar o nome completo, mas também letras
                tabela.append([id, nome,preco, qtd]) #Cria uma linha em formato de tabela
                achou = True

        os.system("cls")
        print(cabecalho)
        print("-" * 123)
        if achou:
            print(tabulate(tabela, headers=[f"{branco_negrito}ID", "Nome", "Preço", "Quantidade"], tablefmt="rounded_grid")) #Criando uma tabela de acordo com os itens
        else:
            print(f"{vermelho}Nenhum produto encontrado.{resetar}")

        print("-" * 123)
        continuar = (input(f"{branco_negrito}Aperte ENTER para voltar ao menu ou [S] para pesquisar outro produto: {resetar}")).lower() #sistema de repetição dentro da pesquisa
        if continuar == "s":
            os.system("cls")
            continue
        else:
            break

# Incluir
def incluir(dados):
    while True:
        print(cabecalho)
        print("-" * 123)
        try:
            id = int(input(f"{branco_negrito}ID do Produto (Digite apenas números): {resetar}")) #Solicita um ID para cadastro do produto
            if id in dados: #Verifica se há o ID no dicionário
                print (f"{vermelho}Esse ID já está sendo utilizado, utilize outro!\n{resetar}")
                nome, preco, qtd = dados[id]
                preco= f"R$ {float(preco):.2f}".replace(".", ",") #Formata o preço
                linha = [[id, nome, preco, qtd]] #Cria uma linha em formato de tabela

                print(tabulate(linha, headers=["ID", "Nome", "Preço", "Quantidade"], tablefmt="rounded_grid")) #Exibe a tabela
                #Sistema de repetição
                continuar = (input (f"{branco_negrito}Pressione [S] para refazer ou ENTER para retornar ao menu: {resetar}")).lower().strip()
                if continuar == "s":
                    os.system("cls")
                    continue
                else:                           
                    return  
            #Prossegue com o programa caso o ID ainda não esteja sendo utilizadp    
            else:     
                nome = input(f"{branco_negrito}Nome: {resetar}").strip()
                preco = float(input(f"{branco_negrito}Preço do Produto: R$ {resetar}").replace(",", "."))
                qtd = int(input(f"{branco_negrito}Quantidade: {resetar}"))
            #Armazena os dados
                dados[id] = [nome, preco, qtd]
                salvar_txt(dados)
                print(f"{verde}Produto adicionado com sucesso!\n{resetar}")
            #Sistema de repetição
                continuar = input (f'{branco_negrito}Deseja incluir mais um produto? Pressione [S] para incluir ou ENTER para retornar: {resetar}').lower().strip()
                if continuar == "s":
                    continue
                else:
                    print (f"{magenta_negrito}Obrigado por utilizar nossos serviços{resetar}")
                    break 
        #Captura erros (ID inválido, preço inválido, quantidade inválida etc.)          
        except:
                print(f"{vermelho}Coloque os dados corretos{resetar}")
                input(f"{branco_negrito}Pressione ENTER para retornar{resetar}")
                break

# Alterar
def alterar(dados):
    while True:
        try:
            os.system("cls")
            print (cabecalho)        
            print("-" * 123)
            id = int(input(f"{branco_negrito}Digite o ID do Produto: {resetar}"))
            #Varredura nos IDs presentes 
            if id not in dados:
                print(f"{vermelho}Produto não encontrado!{resetar}")
                continuar = (input (f"{branco_negrito}Pressione [S] para refazer ou ENTER para retornar ao menu: {resetar}")).lower().strip()
                if continuar == "s": #Caso o usuário queira alterar outro produto
                    os.system("cls")
                continue
            #Carrega os dados
            nome, preco, qtd = dados[id]
            preco = f"R$ {float(preco):.2f}".replace(".", ",")
            linha = [[id, nome, preco, qtd]]

            print(tabulate(linha, headers=[f"{branco_negrito}ID", "Nome", "Preço", "Quantidade"], tablefmt="rounded_grid"))

            #Recebe novos valores
            nome = input(f"{branco_negrito}Alterar o Nome: {resetar}")
            if nome.strip() == "":
                input(f"{vermelho}O nome NÃO pode ficar vazio! (Pressione ENTER){resetar}")
                continue
            preco = float (input(f"{branco_negrito}Preço: R${resetar}").replace("," ,"."))
            qtd = int(input(f"{branco_negrito}Quantidade: {resetar}"))
        

            dados[id] = [
            nome, #Novo Nome
            float(preco) if preco else dados[id][1], # Mantém o preço antigo se não digitar nada
            int(qtd) if qtd else dados[id][2], # Mantém a quantidade antiga se não digitar nada
            ]
            #Salva o Arquivo
            salvar_txt(dados)
            print (f"{verde}Produto alterado com sucesso!!\n{resetar}")
            input(f"{branco_negrito}Pressione ENTER para retornar{resetar}")
            break 
        #Captura erros (ID inválido, preço inválido, quantidade inválida etc.)          
        except ValueError:
                print(f"{vermelho}Coloque os dados corretos{resetar}")
                input(f"{branco_negrito}Pressione ENTER para retornar{resetar}")
                break


# Excluir
def excluir(dados):
    os.system("cls")
    print(cabecalho)        
    print("-" * 123)

    try:
        #Pergunta ao usuário o ID para exclusão
        id = int(input(f"{branco_negrito}Digite o ID do produto para excluir: {resetar}"))
        #Mostra os valores caso o ID bata com algum já existente
        if id in dados:
        
            nome, preco, qtd = dados[id]
            preco = f"R$ {float(preco):.2f}".replace(".", ",")
            linha = [[id, nome, preco, qtd]]

            print(tabulate(linha, headers=[f"{branco_negrito}ID", "Nome", "Preço", "Quantidade"], tablefmt="rounded_grid")) #Formata em tabela
            print("-" * 123)
        #Pergunta ao usuário se o mesmo deseja de fato excluir o produto
            certeza = input(f"{vermelho}Tem certeza que deseja excluir? (S/N): {resetar}").lower().strip()
            if certeza == "s":
                #Deleta o produto e salva o TXT 
                salvar_txt(dados)
                print(f"{verde}\nProduto removido com sucesso!{resetar}")
                #Cancela a exclusão
            else:
                print(f"{vermelho_negrito}\nExclusão cancelada.{resetar}")
        #Mensagem caso não exista o ID        
        else:
            print(f"{amarelo_negrito}ID não encontrado.{resetar}")
    #Captura erros 
    except ValueError:
        print(f"{vermelho_negrito}Digite apenas números para o ID!{resetar}")

    #Volta ao MENU    
    input(f"{branco_negrito}\nPressione ENTER para voltar ao menu...{resetar}")





