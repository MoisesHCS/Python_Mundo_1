from math import hypot
cat1 = float(input("Digite a medida do cateto 1: "))
cat2 = float(input("Digite a medida do cateto 2: "))
print(f"A hipotenusa de um triangulo com catetos medindo {cat1}m e {cat2}m vale {hypot(cat1, cat2):.2f}m")
