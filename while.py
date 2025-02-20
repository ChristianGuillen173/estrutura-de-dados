cadastro = []
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