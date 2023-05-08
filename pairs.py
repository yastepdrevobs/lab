import random

def find_pairs(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                print(numbers[i], numbers[j], "  пари")
                i=0
                j=0
            #якщо не хочете бачити сміття закоентуйте else
            else:
                print(numbers[i], numbers[j], " не пари")

# Генеруємо випадковий масив чисел
numbers = [random.randint(1, 10) for _ in range(random.randint(5, 15))]

#
# Викликаю функцію
find_pairs(numbers)