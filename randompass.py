from secrets import SystemRandom
random = SystemRandom()
pass_ = []
for i in range(8):
    valor = random.randint(1, 10)
    pass_.append(valor)

print(pass_)