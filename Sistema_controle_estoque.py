produtos = [
    [001, "Martelo", 100, "M-01-01"],
    [002, "Chave de Fenda", 150, "C-01-01"],
    [003, "Chave Philips", 200, "C-01-02"]
    ]

def adicionarprodutos():
    novoProduto = input("Adicione os dados do novo produto: ") 
    produtos.append(novoProduto) 
    print("Produto inserido com sucesso! 📦")

def listar_produtos():
    for lista in produtos:
        print(f"Os produtos disponíveis são: {lista}")

def busca_ID():
    for ID in produtos:
        print(f"Os IDs dos produtos são: {ID}")
    

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
        adicionarprodutos()
    elif (opcao == "5"):
        print("Saída do Estoque!")
        break