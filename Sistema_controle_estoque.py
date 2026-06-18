produtos = [
    [100, "Martelo", 10, "M-01-01"],
    [200, "Chave de Fenda", 5, "C-01-01"]
    [210, "Chave"]
]

def adicionarprodutos():
    novoProduto = input("Adicione os dados do novo produto: ") 
    produtos.append(novoProduto) 
    print("Produto inserido com sucesso! 📦")

def listar_produtos():
    for lista in produtos:
        print(f"Os produtos disponíveis são: {lista}")



        


print("\nSistema de Controle de Estoque Simplificado (SCES)")

while True:       
    print("\n1- Adicionar novo produto | 2- Listar todos os produtos | 3- Buscar produto por ID | 4- Atualizar estoque | 5- Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        adicionarprodutos()
    elif (opcao == "2"):
        
    elif (opcao == "3"):
       
    elif (opcao == "4"):
        adicionarprodutos()
    elif (opcao == "5"):
        print("Viagem encerrada!")
        break