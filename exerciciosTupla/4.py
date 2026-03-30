#  Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.

fila = ['Ana', 'Bruno']
print(fila)
nome: str = input('Digite um nome : ')
nome2: str = input('Digite outro nome : ')
fila.extend([nome, nome2])
print(fila)
prioritario: str = input('Digite um cliente prioritário : ')
fila.insert(1, prioritario)
print(fila)
atendido: str = fila.pop(0)
print(f'Cliente atendido: {atendido}')
print(fila)