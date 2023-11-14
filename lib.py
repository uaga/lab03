def bubbleSort(mass):
    n = len(mass)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if mass[j] > mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]
    return mass


def reverseBubbleSort(mass):
    bubbleSort(mass)
    for i in range(int(len(mass) / 2)):
        mass[i], mass[len(mass) - i - 1] = mass[len(mass) - i - 1], mass[i]
    return mass
