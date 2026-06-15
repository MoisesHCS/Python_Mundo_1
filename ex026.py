frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra 'A' aparece {frase.count("A")} vezes")
print(f"Primeira posição da letra 'A': {frase.find("A") + 1}")
print(f"Ultima posição da letra 'A': {frase.rfind("A") + 1}")
