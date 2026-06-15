s = float(input("Digite seu salário: "))
if s > 1250:
    print(f"Novo salário com um aumento de 10%: R$ {s*1.1:.2f}")
else:
    print(f"Novo salário com um aumento de 15%: R$ {s*1.15:.2f}")