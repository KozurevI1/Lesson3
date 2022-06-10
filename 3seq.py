string = input ("Массив 1  - Введите любые цифры через разделитель ',' '/' или ';' :")
string = string.replace(",","/")
string = string.replace(";","/")
string = string.split("/")
mass=[]
for i in string:
    if i.isdigit():
        mass.append(int(i))
    else:
        mass.append(i)
mass1=set(mass)

string = input ("Массив 2  - Введите любые цифры через разделитель ',' '/' или ';' :")
string = string.replace(",","/")
string = string.replace(";","/")
string = string.split("/")
mass=[]
for i in string:
    if i.isdigit():
        mass.append(int(i))
    else:
        mass.append(i)
mass2=set(mass)

print (mass1-mass2)