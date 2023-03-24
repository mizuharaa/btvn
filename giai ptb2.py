import math
print("Giai phuong trinh bac 2. ax^2 + bx + c = 0")
a = float(input("Nhap vao so a: "))
b = float(input("Nhap vao so b: "))
while True:
    if a == 0 and b == 0:
        print ("a va b khong duoc dong thoi = 0")
        a = float(input("Hay nhap lai so a: "))
        b = float(input("Hay nhap lai so b: "))
    else:
        break 
c = float(input("Nhap vao so c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phuong trinh bac 2 nay vo nghiem")
elif delta == 0:
    nghiem_kep = -(b/(a*2))
    print("Phuong trinh nay co nghiem kep la: x = " + nghiem_kep)
elif delta > 0:
    nghiempb_1 = (-(b) + math.sqrt(delta))/(a*2)
    nghiempb_2 = (-(b) - math.sqrt(delta))/(a*2)
    print(f"Phuong trinh co 2 nghiem phan biet la: x1, x2 lan luot la: {nghiempb_1} va {nghiempb_2} ")
    