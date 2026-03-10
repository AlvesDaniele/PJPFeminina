
nome = input("Daniele")
peso = float(input("peso(Kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2) 
print(f"IMC de {nome}: {imc:.2f}")

#comparação mais lógicos (faixa simplificada)
baixo_peso = imc < 18.5
normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc >=25) and (imc < 30)
obesidade = imc >= 30

print("baixo peso?", baixo_peso)
print("normal?", normal)
print("sobrepeso?", sobrepeso)
print("obesidade?", obesidade)