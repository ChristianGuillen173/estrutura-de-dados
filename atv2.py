opcao = input('O que deseja? 1 Inserir 2 Consultar 3Sair: ')
cadastro = []
while(opcao != '3'):
    if (opcao == '1'):
        
        condicao = input('Deseja cadastrar um novo usuário?: S/N ')
        while (condicao != 'N'):
            if (condicao == 'S' or condicao == 'N'):
                while(condicao == 'S'):
                    cadastro_individual = []
                    nome = input('Entre com seu nome Completo: ')
                    email = input('Entre com seu e-mail: ')
                    RA = input('Entre com seu Registro acadêmico: ')
                    cadastro_individual.append(nome)
                    cadastro_individual.append(email)
                    cadastro_individual.append(RA)
                    print(cadastro_individual)
                    cadastro.append(cadastro_individual) 
                    condicao = input('Deseja cadastrar um novo usuário?: S/N ')
            else:
                print('Comando inválido')
                condicao = input('Deseja cadastrar um novo usuário?: S/N ')
        
        print(cadastro)
        print('Deseja inserir usuário.')
    if (opcao == '2'):
        print('Deseja consultar usuário.')
    opcao = input('O que deseja? 1 Inserir 2 Consultar 3Sair: ')

    if (opcao == '3'):
        print('Deseja sair do sistema.')