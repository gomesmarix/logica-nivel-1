#7) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número total de votos brancos: "))
votos_nulos = int(input("Digite o números total de votos nulos: "))
votos_validos = int(input("digite o número total de votos validos:"))


porcentagem_validos = (votos_validos / total_eleitores) * 100 
porcentagem_nulos = (votos_nulos / total_eleitores) * 100
porcentagem_brancos = (votos_brancos / total_eleitores) * 100

print("quantidade de votos validos; ", porcentagem_validos, "%")
print("quantidade de votos nulos; ", porcentagem_nulos, "%"  )
print("quantidade de votos brancos;" , porcentagem_brancos, "%" )
