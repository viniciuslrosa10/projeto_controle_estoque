proxID = 3

produtos = [
    ["1", "Martelo", 100, "M-01-01"],
    ["2", "Chave de Fenda", 150, "C-01-01"],
    ["3", "Chave Philips", 200, "C-01-02"]
    ]

def adicionarprodutos(): ##Criei essa função para adicionar novos produtos no estoque
    global proxID
    novoProduto = input("Adicione o nome do novo produto: ")
    
    localizacao = input("Qual a localização do produto?: ")
    
    quantidade = input("Digite a quantidade do produto: ")
    
    proxID = proxID + 1 ##Conta feita para mudar o ID
    
    produtos.append([proxID, novoProduto, quantidade, localizacao])
    
    print("Produto inserido com sucesso! 📦")

def listar_produtos(): ##Função criada para o usuário ver o que tem no estoque e as informações do produto
    for lista in produtos:
        print(f"Os produtos disponíveis são: {lista}")

def busca_ID(): ##Função de buscar um produto pelo seu ID
    produtoProcurado = input("Insira o ID do produto: ")
    for linha in produtos:
            if produtoProcurado == linha[0]:
                print(f"Produto encontrado: {linha}")
                break
    else:
        print("Produto não encontrado!")

def atualizar_Estoque(): ##Essa função funciona para o usuário atualizar a quantidade de um produto específico
    produtoProcurado = input("Insira o ID do produto: ")
    
    for linha in produtos:
        if produtoProcurado == linha[0]:
            atualizar = input("Qual a quantidade desejada?: ")
            linha[2] = atualizar ## Altera diretamente na coluna de índice 2 da linha atual
            print(f"Quantidade alterada: {linha}")
            break ## Interrompe o loop já que o produto foi encontrado

def estoque_Mínimo(): ##ESsa função serve para avisar ao gerente que quando uma peça está com estoque mínimo é enviado uma mensagem de alerta
    for linha in produtos:
        if linha[2] < 5:
            print(f"Alerta! A {linha} está com baixa quantidade {linha[2]}")
            break
        else:
            print("Prossiga!")
            
    
                
           
  ##Menu Interativo do estoque     
print("\n------- Sistema de Controle de Estoque Simplificado (SCES) -------")

while True:       
    print("\n1- Adicionar novo produto | 2- Listar todos os produtos | 3- Buscar produto por ID | 4- Atualizar estoque | 5- Verificar estoque mínimo | 6- Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        adicionarprodutos()
    elif (opcao == "2"):
        listar_produtos()
        
    elif (opcao == "3"):
        busca_ID()
       
    elif (opcao == "4"):
        atualizar_Estoque()

    elif (opcao == "5"):
        estoque_Mínimo()
    
    elif (opcao == "6"):
        print("Saída do Estoque!")
        break