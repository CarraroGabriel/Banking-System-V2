import textwrap

menu = """
============== MENU ==============
      
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Novo Usuário
[5] - Nova Conta
[6] - Listagem de Contas
[0] - Sair

===================================
            Bem vindo(a)!

=> """

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nValor depositado com sucesso!")
    else:
        print("\nOperação não pode ser concluída, o valor que desejou depositar é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, lim_saques, num_saques):
    if valor > saldo:
        print("\nOperação inválida, você não tem saldo suficiente!")
    elif valor > limite:
        print("\nOperação inválida, valor desejado excede o limite!")
    elif num_saques >= lim_saques:
        print("\nOperação inválida, limite de saques excedido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque: R$ {valor:.2f}\n"
        num_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação não pode ser concluída, o valor que desejou sacar é inválido.")
        
    return saldo, extrato

def exibe_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def cria_usuario(usuarios):
    cpf = input("Informe o seu CPF (APENAS números): ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF já cadastrado!")
        return
     
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
        
def cria_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": usuario}
    else:
        print("\nUsuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta Corrente:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    lim_saques = 3
    usuarios = []
    contas = []
    count_contas = 1
    AGENCIA = "0001"

    while True:

        opcao = int(input(menu))

        if opcao == 1:
            valor = float(input("\nInforme o valor que deseja depositar: "))
            
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("\nInforme o valor que deseja sacar: "))
            
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                lim_saques=lim_saques,
            )
        
        elif opcao == 3:
            exibe_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            cria_usuario(usuarios)
        
        elif opcao == 5:
            conta = cria_conta(AGENCIA, count_contas, usuarios)

            if conta:
                contas.append(conta)
                count_contas += 1

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            print("\nObrigado por utilizar nosso sistema!!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()