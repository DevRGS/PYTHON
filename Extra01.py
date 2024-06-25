import json

# Caminho do arquivo onde os dados serão salvos
ARQUIVO_DADOS = 'cadastro_clientes.json'

# Função para carregar os dados do arquivo
def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Função para salvar os dados no arquivo
def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função para adicionar um novo cliente
def adicionar_cliente(dados, nome, nome_completo, idade, cidade, cargo, empresa, telefone, email):
    cliente = {
        'nome': nome,
        'nome_completo': nome_completo,
        'idade': idade,
        'cidade': cidade,
        'cargo': cargo,
        'empresa': empresa,
        'telefone': telefone,
        'email': email
    }
    dados.append(cliente)
    salvar_dados(dados)

# Função para consultar um cliente pelo índice
def consultar_cliente(dados, indice):
    if 0 <= indice < len(dados):
        return dados[indice]
    else:
        return 'Cliente não encontrado'

# Função para remover um cliente pelo índice
def remover_cliente(dados, indice):
    if 0 <= indice < len(dados):
        cliente_removido = dados.pop(indice)
        salvar_dados(dados)
        return cliente_removido
    else:
        return 'Cliente não encontrado'

# Função para exibir a lista de clientes cadastrados
def listar_clientes(dados):
    print("\nClientes cadastrados:")
    print(f"{'Índice':<10}{'Nome':<20}{'Cidade':<20}")
    print("-" * 50)
    for i, cliente in enumerate(dados):
        print(f"{i:<10}{cliente['nome']:<20}{cliente['cidade']:<20}")

# Função principal
def main():
    dados = carregar_dados()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar cliente")
        print("2. Consultar cliente")
        print("3. Remover cliente")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            nome_completo = input("Nome Completo: ")
            idade = input("Idade: ")
            cidade = input("Cidade: ")
            cargo = input("Cargo: ")
            empresa = input("Empresa: ")
            telefone = input("Telefone: ")
            email = input("Email: ")

            adicionar_cliente(dados, nome, nome_completo, idade, cidade, cargo, empresa, telefone, email)
            print("Cliente adicionado com sucesso!")

        elif escolha == '2':
            listar_clientes(dados)
            try:
                indice = int(input("\nDigite o índice do cliente que deseja consultar: "))
                cliente = consultar_cliente(dados, indice)
                for k, v in cliente.items(): # type: ignore
                    print(f'{k}: {v}')
            except ValueError:
                print("Índice inválido! Por favor, digite um número.")

        elif escolha == '3':
            listar_clientes(dados)
            try:
                indice = int(input("\nDigite o índice do cliente que deseja remover: "))
                cliente = remover_cliente(dados, indice)
                if isinstance(cliente, dict):
                    print("Cliente removido com sucesso!")
                else:
                    print(cliente)
            except ValueError:
                print("Índice inválido! Por favor, digite um número.")

        elif escolha == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
