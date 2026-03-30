#  Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
produto = {"nome": "Camiseta", "preco": 29.99}
print("Antes:", produto)
produto.pop("desconto", None)
print("Depois:", produto)
