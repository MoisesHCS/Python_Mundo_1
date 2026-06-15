v = float(input("Qual é a velocidade atual do carro em Km/h? "))
if v > 80:
    m = (v - 80)*7
    print(f"VELOCIDADE ACIMA DO LIMITE\nValor da multa: R$ {m:.2f}")
else:
    print("VELOCIDADE DENTRO DO LIMITE")
print("Tenha um bom dia, dirija com segurança!")