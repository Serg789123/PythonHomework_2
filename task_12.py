# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате 
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите 
# Кате отгадать задуманные Петей числа.

a = int(input("Введите сумму двух натуральных чисел: "))
b = int(input("Введите произведение этих же чисел: "))
for x in range(a):
    for y in range(b):
        if x + y == a and x * y == b:
            print(x, y)
            break

