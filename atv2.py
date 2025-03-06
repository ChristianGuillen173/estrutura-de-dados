opcao = input('O que deseja? 1 Inserir / 2 Consultar / 3 Alterar / 4 Deletar / 5 Sair: ')
cadastro = []
while opcao != '5':
    if opcao == '1':
        
        condicao = input('Deseja cadastrar um novo usuário?: S/N ')
        while condicao != 'N':
            if (condicao == 'S' or condicao == 'N'):
                while condicao == 'S':
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
    if opcao == '2':
        texto_consulta = input('Entre com o texto a ser consultado: ')
        total_cadastros = 0
        for i in range(len(cadastro)):
            for j in range(3):
                ocorrencia = (cadastro[i][j].lower()).count(texto_consulta)
                if ocorrencia > 0:
                    print(cadastro[i])
                    total_cadastros = total_cadastros + 1
        if total_cadastros == 0:
            print('Usuário não encontrado.')

    if opcao == '3':
        RA_alteracao = input('Entre com o RA do estudante: ')
        total_cadastros = 0
        for i in range(len(cadastro)):
            if cadastro[i][2] == RA_alteracao:
                total_cadastros = total_cadastros + 1
                print('Usuário Encontrado')
                opcao_alteracao = input('Qual dado deseja alterar? A Alterar o nome / B Alterar o E-mail')
                if opcao_alteracao == 'A':
                    cadastro[i][0] = input('Entre com o nome Correto')
                    print('Nome alterado com Sucesso.')
                    print(cadastro)
                if opcao_alteracao == 'B':
                    cadastro[i][0] = input('Entre com o E-mail Correto')
                    print('E-mail alterado com Sucesso.')
                    print(cadastro)
                if opcao_alteracao != 'A' and opcao_alteracao != 'B':
                    print('opção inválida')
        if total_cadastros == 0:               
            print('Usuário não encontrado. ')

    if opcao == '4':
        RA_exclusao = input('Qual é o RA do usuário a ser deletado? ')
        total_cadastros = 0
        for i in range(len(cadastro)):
            if cadastro[i][2] == RA_exclusao:
                total_cadastros = total_cadastros + 1
                print('Usuário encontrado.')
                print('Nome:' +cadastro[i][0])
                print('E-mail:' +cadastro[i][1])
                print('RA:' +cadastro[i][2])
                opcao_exclusao = input('Deseja MESMO fazer isso? S/N ')
                if opcao_exclusao == 'S':
                    cadastro.pop(i)
                    print(cadastro)
                    break
                if opcao_exclusao == 'N':
                    print('Bom Senso!')
                if opcao_exclusao != 'S' or opcao_exclusao != 'N':
                    print('Opção inválida')
        if total_cadastros == 0:
            print('Usuário não encontrado. ')
                
    
    if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
        print('Comando inválido.')
    opcao = input('O que deseja? 1 Inserir 2 Consulta 3 Alterar 4 Deletar')

if opcao == 5:
    print('Deseja sair do sistema.')