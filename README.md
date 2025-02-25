🚀 Projeto de Desenvolvimento de uma Agenda de Contatos em Python 🚀

Objetivo do Projeto

O objetivo principal era criar uma solução digital eficiente para substituir uma agenda de contatos em papel, facilitando a gestão de informações de clientes e fornecedores de uma pequena empresa. O sistema é muito intuitivo, organizado e seguro, garantindo a integridade dos dados e a praticidade no dia a dia dos usuários.
Funcionalidades Implementadas

O sistema desenvolvido atendeu aos seguintes requisitos:
1. Cadastrar Contato :
    * O usuário pode inserir nome, sobrenome, telefone e e-mail.
    * O sistema verifica se o contato já existe na agenda para evitar duplicidades.
    * O telefone é formatado automaticamente para os padrões (XX) XXXX-XXXX (fixo) ou (XX) XXXXX-XXXX (celular).
2. Visualizar Contatos em Ordem Alfabética :
    * Os contatos são ordenados alfabeticamente pelo sobrenome e nome, facilitando a organização e a busca.
    * A ordenação não diferencia maiúsculas de minúsculas (não diferenciais de minúsculas).
3. Pesquisar Contato :
    * O usuário pode buscar contatos por nome, sobrenome ou telefone.
    * O sistema exibe todos os contatos que conversamos à busca, mostrando nome, sobrenome, telefone formatado e e-mail.
4. Atualizar Contato :
    * O usuário pode alterar o nome de um contato existente.
    * O sistema solicita confirmação antes de aplicar as alterações.
5. Remover Contato :
    * O usuário pode excluir um contato da agenda.
    * O sistema solicita confirmação antes de realizar a exclusão, evitando remoções acidentais.
6. Sair do Sistema :
    * O programa é encerrado de forma segura, garantindo que nenhum dado seja perdido.
Tecnologias e Técnicas Utilizadas

* Python : Linguagem principal para desenvolvimento do sistema.
* Ordenação Personalizada : Critério de ordenação por nome, utilizando a função sorted()com uma chave personalizada.
* Manipulação de Listas e Dicionários : Armazenamento e gerenciamento de contatos.
