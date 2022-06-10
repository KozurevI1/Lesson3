count = input ("Введите количество элементов списка: ")
if count.isdigit():
    count=int(count)

vector=[]
for i in range(count):
    number=input("Введите {} элемент: ".format(i+1))
    while True:
        if number.isdigit():
            vector.append(int(number))
            break
        else:
            number=input("Введите {} элемент как цифру: ".format(i+1))
vector.sort()
print("Отсортированный список: ", vector )