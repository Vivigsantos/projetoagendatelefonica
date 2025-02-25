agenda = []


def menu():
    """Exibe o menu de opções da agenda."""
    print(f'*'*50)
    print('                    Agenda                        ')
    print(f'-'*50)
    print('                 Escolha uma opção:                ')
    print(f'-'*50)
    print('1 - Cadastrar Contato;')
    print('2 - Visualizar contato em ordem alfabética;')
    print('3 - Pesquisar Contato;')
    print('4 - Atualizar Contato;')
    print('5 - Remover Contato;')
    print('0 - Sair;')
    print(f'.'*50)


def formatar_telefone(numero):
    """Formata um número de telefone para o padrão (XX)XXXXX-XXXX ou (XX)XXXX-XXXX.

    Args:
        numero (str): Uma string contendo o número de telefone informado pelo usuário,
                      com 10 ou 11 dígitos.

    Returns:
        str: O número formatado no padrão correto ou a mensagem "Número inválido"
             caso não tenha o tamanho esperado.
    """
    if len(numero) == 10:
        return f"({numero[:2]}){numero[2:6]}-{numero[6:]}"  # Fixo
    elif len(numero) == 11:
        return f"({numero[:2]}){numero[2:7]}-{numero[7:]}"  # Celular
    return "Número inválido"


def criar_contato():
    """Solicita os dados do contato e tenta adicioná-lo à agenda.

    O usuário deve fornecer nome, sobrenome, telefone (somente números) e email.
    Após coletar os dados, a função chama `verificar_contato()` para verificar
    se o contato já existe antes de adicioná-lo. O processo pode ser repetido
    até que o usuário escolha encerrar.

    Returns:
        None: A função não retorna valores, apenas solicita entradas do usuário
              e adiciona contatos à agenda se necessário.
    """
    while True:
        contato = {}
        contato['nome'] = input('Nome: ')
        contato['sobrenome'] = input('Sobrenome: ')
        contato['telefone'] = input('Telefone - digite somente os números: ')
        contato['email'] = input('Email: ')

        verificar_contato(contato)

        continuar = input(
            'Deseja realizar novo cadastro [S/N]: ').strip().lower()
        if continuar == 'n':
            break


def verificar_contato(contato):
    """Verifica se o contato já existe na agenda antes de adicioná-lo.

    Args:
        contato (dict): Um dicionário contendo as informações do contato,
                        com as chaves 'nome', 'telefone' e 'email'.

    Returns:
        None: Exibe uma mensagem informando se o contato foi cadastrado
              ou se já existia na agenda.
    """
    if not agenda:
        agenda.append(contato)
        print('Usuário cadastrado!')
    else:
        for indice in range(len(agenda)):
            if contato['telefone'] == agenda[indice]['telefone']:
                if contato['email'] == agenda[indice]['email']:
                    print('Contato já existente!')
                    return

        agenda.append(contato)
        print('Usuário cadastrado!')


def criterio_ordenacao(contato):
    """Define o critério de ordenação pelo sobrenome em minúsculas.

    A função retorna uma tupla contendo o sobrenome e o nome, ambos convertidos
    para letras minúsculas, garantindo uma ordenação sem diferenciação de maiúsculas
    e minúsculas.

    Args:
        contato (dict): Um dicionário contendo as informações do contato,
                        com pelo menos as chaves 'nome' e 'sobrenome'.

    Returns:
        tuple: Uma tupla (sobrenome, nome), ambos em letras minúsculas,
               para ser usada como critério de ordenação.
    """
    return (contato["sobrenome"].lower(), contato["nome"].lower())


def agenda_ordenada_nome():
    """Ordena e exibe os contatos alfabeticamente pelo sobrenome e nome.

    A função verifica se a agenda contém contatos. Caso contrário, exibe uma mensagem
    informando que a agenda está vazia. Se houver contatos, eles são ordenados
    alfabeticamente pelo sobrenome e nome, exibindo os detalhes do contato, incluindo
    o telefone formatado e o email.

    Returns:
        None: A função apenas exibe os contatos ordenados e não retorna valores.
    """
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("\nLista de contatos ordenada por nome :")
        contatos_ordenados = sorted(agenda, key=criterio_ordenacao)
        for contato in contatos_ordenados:
            telefone_formatado = formatar_telefone(contato['telefone'])
            print(
                f"{contato['nome']} {contato['sobrenome']} - {telefone_formatado} - {contato['email']}")
        print("\nLista de contatos ordenada por Sobrenome :")

        contatos_ordenados = sorted(agenda, key=criterio_ordenacao)
        for contato in contatos_ordenados:
            print(
                f"{contato['sobrenome']} - {contato['nome']} - {telefone_formatado} - {contato['email']}")


def buscar_contato():
    """Busca contatos pelo nome, sobrenome ou telefone.

    O usuário informa um dado (nome, sobrenome ou telefone) e a função busca
    correspondências na agenda. Se encontrar contatos compatíveis, exibe os detalhes,
    incluindo o telefone formatado. Caso contrário, informa que nenhum contato foi encontrado.

    Returns:
        None: A função apenas exibe os contatos encontrados e não retorna valores.
    """
    resultados = []
    dado = input("Digite o dado para busca: ")
    index = 0
    for contato in agenda:
        if (dado.lower() in contato['nome'].lower() or
                dado.lower() in contato['sobrenome'].lower() or
                dado in contato['telefone']):
            resultados.append(contato)

    if resultados:
        print("\nContatos encontrados:")
        for c in resultados:
            telefone_formatado = formatar_telefone(c['telefone'])
            print(
                f"{c['nome']} {c['sobrenome']} - {telefone_formatado} - {c['email']}")
    else:
        print('Nenhum contato encontrato')

    index = +1


def atualizar_contato():
    """Atualiza o nome de um contato existente na agenda.

    O usuário informa o nome do contato que deseja atualizar. Se o nome for encontrado
    na agenda, a função solicita um novo nome e o atualiza. Caso contrário, a função
    não realiza nenhuma alteração.

    Returns:
        None: A função apenas modifica a agenda e exibe mensagens para o usuário.
    """
    nome = input("Digite o nome do contato que deseja atualizar: ").strip()

    for indice in range(len(agenda)):
        if (agenda[indice]['nome'] == nome):
            novo_nome = input("Digite o novo nome: ")
            agenda[indice]['nome'] = novo_nome
            print(
                f"{nome} seu nome foi atualizado para {agenda[indice]['nome']}!")


def remover_contato():
    """Remove um contato da agenda caso ele exista.

    O usuário informa o nome do contato que deseja atualizar. Se o nome for encontrado
    na agenda, a função solicita um novo nome e o atualiza. Caso contrário, a função
    não realiza nenhuma alteração.

    Returns:
        None: A função apenas modifica a agenda e exibe mensagens para o usuário.
    """
    remover = input(
        "Deseja remover algum contato na agenda [S/N]:").strip().lower()
    if remover == 'n':
        print("Operação cancelada.")
        return
    else:
        nome_remover = input(
            'Digite o nome do contato que deseja remover: ').strip().lower()
        contato_removido = None
        for contato in agenda:
            if contato["nome"].lower() == nome_remover:
                contato_removido = contato
                break
        if contato_removido:
            confirmacao = input(
                f"Tem certeza que deseja remover o contato '{contato_removido['nome']}'? [S/N]: ").strip().lower()
            if confirmacao == 's':
                agenda.remove(contato_removido)
                print(
                    f"Contato '{contato_removido['nome']}' removido com sucesso!")
            else:
                print("Remoção cancelada.")
        else:
            print("Contato não encontrado.")


while True:
    menu()
    opcao = int(input('Opção : '))

    if opcao == 1:
        print('Cadastrar Contato:')
        criar_contato()
    elif opcao == 2:
        print('Visualizando Agenda Ordenada:')
        agenda_ordenada_nome()
    elif opcao == 3:
        print('Pesquisar contato:')
        buscar_contato()
    elif opcao == 4:
        print('Atualizar contato:')
        atualizar_contato()
    elif opcao == 5:
        print('Remover contato:')
        remover_contato()
    else:
        print('Saindo da Agenda')
        break

    continuar = (input('Deseja realizar outra operação? [S/N]: ')).lower()
    if continuar == 'n':
        print('Encerrando o Programa')
        break
