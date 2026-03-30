#  Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.

nota1 = float(input('Digite uma nota : ' ))
nota2 = float(input('Digite uma nota : ' ))
nota3 = float(input('Digite uma nota : ' ))

lista = [nota1, nota2, nota3]

print(lista)

media = [nota1 + nota2 + nota3 /3 ]
print(media)

nota4 = float(input('Digite uma nota : ' ))
menor = min (lista)
if nota4 < menor:
    lista. remove(menor)
    lista.append(nota4)
    print(lista)
else:  print('A nota informada é maior que a nota menor da lista')
lista.sort()
print(lista)



