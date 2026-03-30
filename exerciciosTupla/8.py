# Comece com agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}. 
# Adicionar um novo contato (nome→telefone)
# Atualizar o telefone de um contato informado (se existir)
# Exibir a lista ordenada de nomes de contatos
agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
print("Agenda inicial:", agenda)
# Adicionar um novo contato
novo_nome = input("Digite o nome do novo contato: ")
novo_telefone = input("Digite o telefone do novo contato: ")
agenda[novo_nome] = novo_telefone
print("Agenda após adicionar novo contato:", agenda)
# Atualizar o telefone de um contato informado
contato_atualizar = input("Digite o nome do contato para atualizar o telefone: ")
if contato_atualizar in agenda:
    novo_telefone_atualizado = input("Digite o novo telefone: ")
    agenda[contato_atualizar] = novo_telefone_atualizado
    print("Agenda após atualizar telefone:", agenda)
else:
    print("Contato não encontrado para atualização.")
# Remover um contato pelo nome
contato_remover = input("Digite o nome do contato para remover: ")

if contato_remover in agenda:
    del agenda[contato_remover]
    print("Agenda após remover contato:", agenda)
else:
    print("Contato não encontrado para remoção.")
# Exibir a lista ordenada de nomes de contatos
nomes_ordenados = sorted(agenda.keys())
print("Lista ordenada de nomes de contatos:", nomes_ordenados)


    