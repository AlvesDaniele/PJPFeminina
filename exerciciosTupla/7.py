# Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
produto = {"nome": "Camiseta", "preco": 29.99, "quantidade": 10}
aumento_percentual = 10  # Exemplo de aumento de 10%
produto["preco"] += produto["preco"] * (aumento_percentual / 100)
produto["quantidade"] += 2
total = produto["preco"] * produto["quantidade"]
print(f"Produto: {produto['nome']}")
print(f"Preço atualizado: {produto['preco']:.2f}")
print(f"Quantidade atualizada: {produto['quantidade']}")
print(f"Total: {total:.2f}")
