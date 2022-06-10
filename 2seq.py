string = input ("Введите любые цифры через запятую :")
string = string.replace(",","/")
string = string.replace(";","/")
string = string.split("/")
number=[]
for i in string:
    if i.isdigit():
        number.append(int(i))
    else:
        number.append(i)
number1=set(number)
print (number1)
