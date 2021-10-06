def Cadastrar():
    contatos = []                                               #Abrindo uma lista vazia para adiacionar os dados
    contatos.append('nome: ' + input("Informe o nome: "))
    contatos.append('numero: ' + input("Informe o Numero: "))
    contatos.append('Email: ' +  input("Informe o Email: "))
    with open('contatos.txt', "a") as clientes:                 #mesmo que clientes = open('contatos.txt', "a") só que mais bonito.
        for valor in contatos:                                  #para pegar cada elemento de dentro da lista, já que a lista inteira ele não consegue ler.
            clientes.write(valor + "\n")                        #escrevendo os dados de cada elemento da lista no arquico txt

def leitura():
    with open('contatos.txt', "r") as clientes:
        listar = clientes.read()
        print(listar)
        clientes.close()

def pesquisar():
    with open('contatos.txt', "r") as clientes:
        contatos = (clientes.readlines())
        quantidade_de_dados = len(contatos) - 1
        clientes.close()
    pesquisa_por = input("Você deseja pesquisar por: \n1: nome \n2: numero \n3: Email \n")
    if pesquisa_por == '1':
        pesquisa = ('nome: ' + input('Digite o nome que você deseja pesquisar: '))
        str_pesquisa = len(pesquisa)
        pesquisa_encontrada = False
        while quantidade_de_dados >= 0:
            if contatos[quantidade_de_dados][:str_pesquisa] == pesquisa:
                print(contatos[quantidade_de_dados] + contatos[quantidade_de_dados + 1] + contatos[quantidade_de_dados + 2])
                pesquisa_encontrada = True
            quantidade_de_dados = quantidade_de_dados - 1
        if pesquisa_encontrada == False:
            print('Nada foi encontrado no banco de dados.')
    if pesquisa_por == '2':
        pesquisa = ('numero: ' + input('Digite o numero que você deseja pesquisar: '))
        str_pesquisa = len(pesquisa)
        pesquisa_encontrada = False
        while quantidade_de_dados >= 0:
            if contatos[quantidade_de_dados][:str_pesquisa] == pesquisa:
                print(contatos[quantidade_de_dados - 1] + contatos[quantidade_de_dados] + contatos[quantidade_de_dados + 1])
                pesquisa_encontrada = True
            quantidade_de_dados = quantidade_de_dados - 1
        if pesquisa_encontrada == False:
            print('Nada foi encontrado no banco de dados.')
    if pesquisa_por == '3':
        pesquisa = ('Email: ' + input('Digite o Email que você deseja pesquisar: '))
        str_pesquisa = len(pesquisa)
        pesquisa_encontrada = False
        while quantidade_de_dados >= 0:
            if contatos[quantidade_de_dados][:str_pesquisa] == pesquisa:
                print(contatos[quantidade_de_dados - 2] + contatos[quantidade_de_dados - 1] + contatos[quantidade_de_dados])
                pesquisa_encontrada = True
            quantidade_de_dados = quantidade_de_dados - 1
        if pesquisa_encontrada == False:
            print('Nada foi encontrado no banco de dados.')

def editar():
    with open('contatos.txt', "r") as clientes:
        contatos = (clientes.readlines())
        clientes.close()
        quantidade_de_dados = len(contatos)
        contador = 0
        while contador < quantidade_de_dados:
            print(contador, ": ", contatos[contador])
            contador = contador + 1
        contador = 0
        editor = int(input("Digite o numero correspondente a linha que você deseja editar: "))
        if contatos[editor][:4] == "nome": #para que o sitema interprete que é um nome que está sendo mudado e o usuario não precise digitar "nome: "
            contatos[editor] = ('nome: ' + (input('Digite o novo termo: ' ) + '\n'))
            with open('contatos.txt', "w") as editar:
                for valor in contatos:
                    editar.write(valor)
                editar.close()
        elif contatos[editor][:4] == "nume":
            contatos[editor] = ('numero: ' + (input('Digite o novo termo: ' ) + '\n'))
            with open('contatos.txt', "w") as editar:
                for valor in contatos:
                    editar.write(valor)
                editar.close()
        else:
            contatos[editor] = ('Email: ' + (input('Digite o novo termo: ' ) + '\n'))
            with open('contatos.txt', "w") as editar:
                for valor in contatos:
                    editar.write(valor)
                editar.close()

def excluir():
    with open('contatos.txt', "r") as clientes:
        contatos = (clientes.readlines())
        clientes.close()
        quantidade_de_dados = len(contatos)
        contador = 0
        while contador < quantidade_de_dados:
            print(contador, ": ", contatos[contador])
            contador = contador + 1
        contador = 0
        editor = int(input("Digite o numero correspondente a linha que você deseja excluir: "))
        if contatos[editor][:4] == "nome": 
            
            contatos[editor] = ('nome: \n')
            with open('contatos.txt', "w") as editar:
                for valor in contatos:
                    editar.write(valor)
                editar.close()
        elif contatos[editor][:4] == "nume":
            contatos[editor] = ('numero: \n')
            with open('contatos.txt', "w") as editar:
                for valor in contatos:
                    editar.write(valor)
                editar.close()
        else:
            contatos[editor] = ('Email: \n')
            with open('contatos.txt', "w") as editar:
                for valor in contatos:
                    editar.write(valor)
                editar.close()

def main():
    opcao = ""
    while opcao != "Sair":
        print(" -*-*-*-*-*-* Agenda de contatos *-*-*-*-*-*- \n")
        print(" Escolha uma das opcoes:\n ")
        opcao = input("Cadastrar - Pesquisar - Listar - Editar -Excluir - Sair: ")
        if opcao == "Cadastrar":
            Cadastrar()
        elif opcao == "Listar":
            leitura()
        elif opcao == "Editar":
            editar()
        elif opcao == "Pesquisar":
            pesquisar()
        elif opcao == "Excluir":
            excluir()
        elif opcao == "Sair":
            print ("Obrigado por Usar o aplicativo de contatos da Deivid's Lta. \n")
        else: 
            print('Comando não existe ou foi digitado de forma incorreta. Tente Novamente digitando extamente o comando apresentado, respeitando as letras maiusculas \n')

main()
