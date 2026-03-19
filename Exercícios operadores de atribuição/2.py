# Solicite ao usuário que informe um orçamento (float) e um gasto (float). Utilize atribuição -= para descontar o gasto do orçamento. Leia um contador (int) e um passo (int). Faça contador += passo duas vezes. Mostre o resultado
orcamento = float(input("Digite o orçamento: "))
gasto = float(input("Digite o gasto: "))
orcamento -= gasto
print("O orcamento restante é:", orcamento)