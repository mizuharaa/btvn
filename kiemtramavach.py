#0000000000000
mavach = input('Nhap vao ma vach co 13 so: ')
while len(mavach) != 13:
    print("Loi cu phap")
    break
c = int(mavach[-1])
a = int(mavach[0]) + int(mavach[2])+ int(mavach[4]) + int(mavach[6])+ int(mavach[8]) + int(mavach[10])
b = int(mavach[1]) + int(mavach[3])+ int(mavach[5]) + int(mavach[7]) + int(mavach[9]) + int(mavach[11])
d = a + b*3
if (d%10) / 10 != 0:
    f = 10 - d%10
else:
    f= 0
if f == c:
    print("Ma vach dung")
else:
    print("Ma vach sai")