import random
minimum=input()
maximum=input()

for i in range(5):
    num=random.randint(int(minimum), int(maximum))
    print("Liczba",i+1,": ",num, sep="")
