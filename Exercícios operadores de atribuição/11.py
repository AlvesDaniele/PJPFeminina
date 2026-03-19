# Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, guarde os metros restantes utilizando %= (utilize outra variável).  
distancia_metros = int(input("Digite a distância em metros: "))
distancia_metros //= 1000
metros_restantes = distancia_metros % 1000
print("A distância em km inteiros é:", distancia_metros)
print("A distância em metros restantes é:", metros_restantes)

