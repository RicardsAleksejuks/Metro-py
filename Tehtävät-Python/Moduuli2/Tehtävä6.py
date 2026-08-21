import random

numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)

numero4 = random.randint(1, 6)
numero5 = random.randint(1, 6)
numero6 = random.randint(1, 6)
numero7 = random.randint(1, 6)

koodi3 = numero1, numero2, numero3
koodi4 = numero4, numero5, numero6, numero7

print(f"Kolmen numeron koodi:{koodi3}")
print(f"Neljän numeron koodi:{koodi4}")