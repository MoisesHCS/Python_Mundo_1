d = float(input("Digite a distância da viagem em Km: "))
p = 0.5*d if d <= 200 else 0.45*d
print(f"Preço da passagem: R$ {p:.2f}")