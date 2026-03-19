# LeSolicite ao usuário que informe o estoque no início do dia (int) e a quantidade vendida ao final do dia (int). Atualize a quantidade utilizando atribuição -= para mostrar o estoque final.
estoque = int(input("Digite o estoque no início do dia: "))
vendido = int(input("Digite a quantidade vendida ao final do dia: "))
estoque -= vendido
print("O estoque final é:", estoque)