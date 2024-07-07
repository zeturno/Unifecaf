# Função que repete a entrada até que seja possível converter para o tipo definido
def repetidor(entrada_de_dado, definicao):
    while True:
        try:
            valor = definicao(input(entrada_de_dado).strip())
            break
        except ValueError:
            print("Opção indisponível, tente novamente")    
    return valor

# Dicionário inicial de estoque com um produto de exemplo
estoque = {"arroz": {"Quantidade": 23, "Valor": 254}}

# Função para obter informações do produto
def obter_produto(adicionar):
    while True:
        if adicionar == True:
            while True:
                quantidade = repetidor("Quantidade Disponível: ", int)
                if quantidade >= 0:
                    break
                else:
                    print("Não é possível adicionar quantidade negativa, tente novamente!")
            while True:
                valor = repetidor("Valor: ", float)
                if valor > 0:
                    return quantidade, valor
                    break
                elif valor == 0:
                    print("O produto não pode ter valor zero, por favor adicione um valor acima de R$ 0")
                else:
                    print("Não é possível adicionar valor negativo, tente novamente!")
        else:
            nome = repetidor("Nome do produto: ", str)
            return nome
            break

# Função para adicionar produto ao estoque
def adicionar_ao_estoque():
    nome = obter_produto(False)
    if nome in estoque:
        print("O produto já está em estoque, caso deseje pode atualizá-lo na opção 3!")
    else:
        quantidade, valor = obter_produto(True)
        estoque[nome] = {"Quantidade": quantidade, "Valor": valor}
        print(f"Item {nome} adicionado com sucesso")
        print(f"Quantidade em estoque: {quantidade}")
        print(f"Valor do produto: R$ {valor}")

# Função para visualizar o estoque atual
def visualizar_estoque():   
    if not estoque:
        print("Não possui produtos em estoque.")
    else:
        print("Estoque atual: ")
        for nome, info in estoque.items():
            print(f"Nome: {nome} | Unidades em estoque: {info['Quantidade']} | Valor: R$ {info['Valor']}")

# Função para atualizar informações do produto no estoque
def atualizar_estoque():
    nome = repetidor("Nome do produto que deseja atualizar: ", str)
    if nome in estoque:
        novo_nome = repetidor("Novo nome do produto: ", str)
        quantidade, valor = obter_produto(True)
        estoque[nome] = {"Quantidade": quantidade, "Valor": valor}
        estoque[novo_nome] = estoque.pop(nome)
        print(f"{nome} atualizado")
    else:
        print("Produto não encontrado no estoque")

# Loop principal do programa
while True:
    opcao = repetidor("Selecione a opção:\nAdicionar produto: 1\nVisualizar estoque: 2\nAtualizar produto: 3\nEncerrar o programa: 4\nSua Escolha: ", int)
    if opcao == 1:
        adicionar_ao_estoque()
    elif opcao == 2:
        visualizar_estoque()   
    elif opcao == 3:
        atualizar_estoque()
    elif opcao == 4:
        print("Obrigado por usar o programa, volte sempre")
        break
    else:
        print("Opção incorreta, selecione novamente")
