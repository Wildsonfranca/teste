dados_pessoais={}


#adiciona chave 
dados_pessoais['Nome'] = input('Informe o nome: ')
dados_pessoais['CPF'] = input('Informe o CPF: ')
dados_pessoais['RG'] = input('Informe o RG: ')
dados_pessoais['Data de Nascimento'] = input('Informe a Data de Nascimento: ')
dados_pessoais['Sexo'] = input('Informe o Sexo: ')
dados_pessoais['Signo'] = input('Informe o Signo: ')
dados_pessoais['Filiação'] = input('Informe o nome da mãe e do pai: ')
dados_pessoais['E-mail'] = input('Informe o E-mail: ')
dados_pessoais['Senha'] = input('Informe o Senha: ')
dados_pessoais['CEP'] = input('Informe o CEP: ')
dados_pessoais['Endereço'] = input('Informe o Endereço: ')
dados_pessoais['Número'] = input('Informe o Número: ')
dados_pessoais['Bairro'] = input('Informe o Bairro: ')
dados_pessoais['Cidade'] = input('Informe a Cidade: ')
dados_pessoais['Estado'] = input('Informe o Estado: ')
dados_pessoais['Telefone'] = input('Informe o Telefone: ')
dados_pessoais['Altura'] = str(input('Informe a Altura : ')).replace(',','.')
dados_pessoais['Peso'] =str(input('Informe o Peso: ')).replace(',','.')
dados_pessoais['Tipo Sanguineo'] = input('Informe o Tipo Sanguino: ')
dados_pessoais['Cor Favorita'] = input('Informe o Cor Favorita : ')
dados_pessoais['Cor Favorita'] = input('Informe o Cor Favorita : ')



for chave in dados_pessoais:
     print(f'{chave}:{dados_pessoais.get(chave)}')
    