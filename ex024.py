nome = str(input("Digite o nome de uma cidade: ")).strip()
print(f"Começa com 'Santo'? {nome[:5].upper() == "SANTO"}")