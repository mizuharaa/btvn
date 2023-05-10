import math as m
#Data_input.py
def integer() -> int:
    num = int(input('int: '))
    return num
def floatnum() -> float:
    flo = float(input('float: '))
    return flo

def input_list() -> list:
    myl = []
    n = int(input('Amount: '))
    while len(myl) < n:
        a = input('Enter: ')
        myl.append(a)
    return myl
#Test
print(integer())
print(floatnum())
print(input_list())

#HinhHoc.py

exist = None
def check_triangle(a, b, c):
    global exist
    exist = True if a + b > c and a + c > b and b + c > a else False if a == 0 or b == 0 or c == 0 else False
    return exist
def type_triangle(a , b, c):
    is_right = a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2
    is_equilateral = a == b == c
    if exist:
        if is_right and is_equilateral:
            return 'Right angle isosceles'
        elif is_equilateral:
            return 'Equilateral'
        elif is_right:
            return 'Right'
        elif a == b or a == c or b == c:
            return 'Isosceles'
def area(a, b ,c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

#Kiemtra.py
def email() -> bool:
    mail = input('Enter: ')
    listmail = ['@yahoo', '@gmail', '@lsts', '@inbox', '@outlook', '@office', '@yandex',] #v.v...
    check = mail.split('@')
    if len(check[0]) == 0:
        return False
    for i in listmail:
        if i in mail:
            return True
    return False

def check_phone():
    phone = input('sdt: ')
    vnf_regex = ['09', '03', '07', '08', '05']
    if phone[0:2] not in vnf_regex:
        return False
    return True if len(str(phone)) == 10 else False
print(check_phone())

def check_prime():
    n = int(input('Num: '))
    if n < 2:
        return 'Not a prime'
    for i in range(2, (n+1)//2, 1):
        if n % i == 0:
            return 'Not a prime'
    return 'Prime'
print(check_prime())
