# Solicite um valor de estoque (int), subtraia as vendas utilizando -= e depois a reposição do estoque utilizando +=, por fim, aplique %= 6.
estoque = int(input("Digite o  valor do estoque: "))
vendas = int(input("Digite o valor das vendas:"))
estoque -= vendas
reposição = int(input("Digite o valor da reposição do estoque: "))
estoque += reposição
estoque %=6
print("O valor final do estoque é:", estoque)

