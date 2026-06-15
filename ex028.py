from random import randint
from time import sleep
num = randint(0, 5)
print("-=-"*20)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
n = int(input("Em qual número eu estou pensando? "))
print("PROCESSANDO...")
sleep(3)
if num == n:
    print("PARABÉNS! Você acertou o número")
else:
    print(f"ERROU. Eu pensei no número {num}")