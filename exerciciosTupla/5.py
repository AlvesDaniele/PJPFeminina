#  Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.

nome: str = input('Digite um nome : ')
idade: int = int(input('Digite uma idade : '))
aluno = {"nome": nome, "idade": idade}
print(aluno)
print(type(aluno))

# Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
nota: float = float(input('Digite uma nota : '))
aluno["nota"] = nota
print(aluno)

