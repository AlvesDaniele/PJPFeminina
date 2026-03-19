frutas = ["maçã", "banana", "uva"]
numeros = [1,2,3,4]

# Acessando elementos
print("Primeira fruta:", frutas[0])                 # "maçã"
print("Última fruta:") , frutas [-1]                # "uva"

# Alterando elementos 
frutas[1] = "banana nanica"
print("Após alterar:" frutas)

# Adicionando elementos
frutas.append("morango")
frutas.insert(1, "pera")
print("Após adicionar:", frutas)

# Removendo elementos
frutas.remove("uva")
ultima = frutas.pop()
print("Após remover 'uva' e pop():", frutas, "| última removida:" , ultima)