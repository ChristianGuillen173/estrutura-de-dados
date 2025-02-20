cadastro = []
for i in range(5):
    cadastro_individual = []
    nome = input('Entre com seu nome Completo: ')
    email = input('Entre com seu e-mail: ')
    RA = input('Entre com seu Registro acadêmico: ')
    cadastro_individual.append(nome)
    cadastro_individual.append(email)
    cadastro_individual.append(RA)
    cadastro.append(cadastro_individual) 
    print(cadastro_individual)

print(cadastro)
