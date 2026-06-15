d = float(input("Digite a quantidade de Km rodados: "))
t = int(input("Digite por quantos dias ele foi alugado: "))
p = (60*t+0.15*d)
print(f"O preço total a pagar e de R$ {p:.2f}")