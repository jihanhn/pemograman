# problem A
n = input("Input Angka Positif: ")
if (int(n)>=1 and int(n)<=20):
    for i in range(int(n)):
        result = i ** 2
        print(result)
else :
    print ("Input Angka 1-20")

