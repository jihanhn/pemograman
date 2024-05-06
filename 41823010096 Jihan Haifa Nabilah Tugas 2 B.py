# Problem B
n = input("Input Angka Positif: ")
for i in range(int(n)):
    if (i % 2 != 0 or i == 0):
        result = i ** 2
        print(result)