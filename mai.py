char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
qt = int(input("digite a quantidade de carecteres"))
senha = ""

for i in range(qt):
    senha += random.choice(char)

print(senha)
