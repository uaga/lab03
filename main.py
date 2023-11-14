def bubbleSort(mass):
    n = len(mass)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if mass[j] > mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]


def reverseBubbleSort(mass):
    bubbleSort(mass)
    for i in range(int(len(mass) / 2)):
        mass[i], mass[len(mass) - i - 1] = mass[len(mass) - i - 1], mass[i]


n = int(input("n = "))

numbers = []

for i in range(n):
    numbers.append(int(input("Введите число: ")))

print(numbers)

var = int(input("Вариант сортировки:\n1 - по возрастанию\n2 - по убыванию\nВаш выбор: "))

if var == 1:
    bubbleSort(numbers)
elif var == 2:
    reverseBubbleSort(numbers)
else:
    print("ERROR")

print(numbers)