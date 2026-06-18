proxID = 3
produtos = [
    ["1", "Martelo", 100, "M-01-01"],
    ["2", "Chave de Fenda", 150, "C-01-01"],
    ["3", "Chave Philips", 200, "C-01-02"]
    ]
def adicionarprodutos():
    global proxID
    novoProduto = input("Adicione o nome do novo produto: ")
    localizacao = input("Qual a localização do produto?: ")
    quantidade = input("Digite a quantidade do produto: ")
    proxID = proxID + 1
    produtos.append([proxID, novoProduto, quantidade, localizacao])
    print("Produto inserido com sucesso! 📦")

def listar_produtos():
    for lista in produtos:
        print(f"Os produtos disponíveis são: {lista}")

def busca_ID():
    produtoProcurado = input("Insira o ID do produto: ")
    for linha in produtos:
            if produtoProcurado == linha[0]:
                print(f"Produto encontrado: {linha}")
                break
    else:
        print("Produto não encontrado!")

def atualizar_Estoque():
    produtoProcurado = input("Insira o ID do produto: ")
    for linha in produtos:
        if produtoProcurado == linha[0]:
            atualizar = input("Qual a quantidade desejada?: ")
            linha[2] = atualizar
            print(f"Quantidade alterada: {linha}")
            break
                
           
       
print("\n------- Sistema de Controle de Estoque Simplificado (SCES) -------")

while True:       
    print("\n1- Adicionar novo produto | 2- Listar todos os produtos | 3- Buscar produto por ID | 4- Atualizar estoque | 5- Sair")
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
        print("Saída do Estoque!")
        break