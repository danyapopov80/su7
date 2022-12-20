# №1
a = True
b = False
print(a and b)
print((a and b) or b)
print((a and b) or not (a and b))
print(a and b or not (a or b) or b)
print(b and b or not a and (a or b or a) or not (a or b))
print(1 << 2)
print(1 & 0 | 1>> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111^0b111 | 0b010)

# №2
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
if a<b:
    print(a, " - это наименьшее из двух данных")
elif a>b:
    print(b, " - это наименьшее из двух данных")
elif a==b:
    print(a or b, " - числа одинаковы")

# №3
a=int(input("Введите 1-е число: "))
b=int(input("Введите 2-е число: "))
c=int(input("Введите 3-е число: "))
if a>b:
    if a>c:
        print(a, " - это наибольшее из введёных чисел")
    else:
        print(c, " - это наибольшее из введёных чисел")
elif b>c:
        print(b, " - это наибольшее из введёных чисел")
elif a==b==c:
    print(a or b or c, " - все числа одинаковы")
else:
    print(c, " - это наибольшее из введёных чисел")

# №4
a=int(input("Введите 1-е число: "))
b=int(input("Введите 2-е число: "))
c=int(input("Введите 3-е число: "))
if a!=b and b!=c and a!=c:
    print(3, " - все числа уникальны")
elif (a==b and b!=c) or (a==c and a!=b) or (b==c and c!=a):
    print(1, " - только одно число уникально")
elif a==b==c:
    print(0, " - все числа одинаковы")
