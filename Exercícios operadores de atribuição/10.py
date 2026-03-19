# Solicite ao usuário que informe os tempos em segundos (int). Converta para minutos inteiros com //= e depois use %= para obter segundos restantes.
segundos = int(input("Digite o tempo em segundos: "))
segundos //= 60
print("A quantidade de minutos inteiros é:", segundos)
segundos %= 60
print("A quantidade de segundos restantes é:", segundos)

 