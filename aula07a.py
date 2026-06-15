n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print("A soma vale {}, o produto vale {}, e a divisao vale {:.2f}".format(s, m, d), end = " >>> ")
print(f"A divisao inteira vale {di}, e a potencia vale {e}")