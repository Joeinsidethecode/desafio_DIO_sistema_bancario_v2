clientes = []
contas = []

def cadastro_cliente(nome, data_nascimento, cpf, endereco, /):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print('Erro: CPF já cadastrado para outro usuário.')
            return
    
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    clientes.append(usuario)
    print('Cliente cadastrado com sucesso!')

def cadastro_conta(cpf):
    check_cpf = ''
    for usuario in clientes:
        if usuario['cpf'] == cpf:
            check_cpf = usuario
            break
    
    if not check_cpf:
        print('Erro: Usuário não encontrado')
        return

    check_contas = [conta for conta in contas if conta['cpf'] == cpf]
    if len(check_contas) > 0:
        print('Erro: CPF já cadastrado para outra conta')
        return
    
    conta_numero = len(contas) + 1
    conta = {
        'AGENCIA': '0001',
        'conta_numero': conta_numero,
        'nome_cliente': check_cpf['nome'],
        'cpf': cpf
    }
    contas.append(conta)
    print('Conta-corrente cadastrada com sucesso!')

def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:  R$ {valor:.2f}\n'
    else:
        print('Valor inválido. Informe corretamente o valor.')
    print(f'Depósito: R$ {valor:13.2f}\nSaldo atual: R$ {saldo:10.2f}\n')
    return saldo, extrato

def saque(*, valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato, total_saques_dia):
    if valor <= 0:
        print('Valor inválido. Informe corretamente o valor.\n')
    elif valor > saldo:
        print(f'Saldo atual: R$ {saldo:.2f}\nSeu saldo é insuficiente. A operação não foi realizada.\n')
    elif total_saques_dia + valor > limite:
        print(f'O valor total dos saques diários excede o limite de R$ {limite:.2f}. A operação não foi realizada.\nSaldo atualizado: R$ {saldo:.2f}\n')
    elif numero_saques >= LIMITE_SAQUES:
        print(f'Seu limite de {LIMITE_SAQUES} saques diários foi excedido. A operação não foi realizada.\nSaldo atualizado: R$ {saldo:.2f}\n')
    else:
        saldo -= valor
        extrato += f'Saque:     R$ {valor:.2f}\n'
        numero_saques += 1
        total_saques_dia += valor
        print(f'Saque realizado com sucesso.\nSaldo atualizado: R$ {saldo:.2f}')
    return saldo, extrato, numero_saques, total_saques_dia

def mostrar_extrato(saldo, /, *, extrato=''):
    print('========================================================')
    print('                      EXTRATO')
    print('========================================================')
    print(f'{extrato}\nSaldo:     R$ {saldo:.2f}')
    print('========================================================')

def menu():
    saldo = 0
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    extrato = ''
    total_saques_dia = 0
    
    while True:
        print('\n*** MENU PRINCIPAL ***')
        print('[1] Cadastro de novo cliente')
        print('[2] Cadastro de nova conta-corrente')
        print('[3] Exibir lista de clientes')
        print('[4] Exibir contas')
        print('[5] Fazer depósito')
        print('[6] Efetuar saque')
        print('[7] Ver extrato')
        print('[8] Encerrar')
        opcao = input('Escolha a operação desejada: ')
        
        if opcao == '1':
            nome = input('Nome completo: ')
            data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
            cpf = input('CPF (somente números): ')
            logradouro = input('Logradouro nº(R./Av./Estr., etc.): ')
            complemento = input('Complemento (casa/apto., etc.): ')
            bairro = input('Bairro: ')
            cidade_estado = input('Cidade/Estado: ')
            cep = input('CEP (xxxxx-xxx): ')
            endereco = f'{logradouro} - {complemento}\n{bairro} - {cidade_estado}\n{cep}'
            cadastro_cliente(nome, data_nascimento, cpf, endereco)
        
        elif opcao == '2':
            cpf = input('CPF (somente números): ')
            cadastro_conta(cpf)
        
        elif opcao == '3':
            for usuario in clientes:
                print('\n**** INFORMAÇÕES DO CLIENTE ****')
                print(f"Nome: {usuario['nome'].upper()}\nCPF: {usuario['cpf']}\nData de nascimento: {usuario['data_nascimento']}\nEndereço: {usuario['endereco'].upper()}\n")
        
        elif opcao == '4':
            for conta in contas:
                print('\n**** INFORMAÇÕES DA CONTA ****')
                print(f"Agência: {conta['AGENCIA']}\nConta-corrente: {conta['conta_numero']}\nCliente: {conta['nome_cliente'].upper()}\nCPF: {conta['cpf']}\n")
        
        elif opcao == '5':
            valor = float(input('Valor do depósito: R$'))
            saldo, extrato = deposito(valor, saldo, extrato)
        
        elif opcao == '6':
            valor = float(input('Valor do saque: R$'))
            saldo, extrato, numero_saques, total_saques_dia = saque(valor=valor, saldo=saldo, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, extrato=extrato, total_saques_dia=total_saques_dia)
        
        elif opcao == '7':
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == '8':
            print('Fim dos serviços!\n')
            print('----------------------------------------------------------------------')
            print(f' Obrigado por utilizar nossos serviços, {cliente.upper()}. Tenha um ótimo dia!')
            print('----------------------------------------------------------------------')
            break
            
        else:
            print('Opção inválida. Escolha a operação desejada.\n')

if __name__ == "__main__":
    cliente = input('Olá! como podemos lhe chamar?:')
    print('----------------------------------------------------------------------')
    print(f'  Olá, {cliente.upper()}! O Banco Itander-Bradescaixa lhe dá as boas-vindas.') 
    print('----------------------------------------------------------------------')
    menu()
