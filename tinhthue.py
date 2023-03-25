tn = int(input("Nhap vao thu nhap ca nhan: "))
dpdnt = int(input("Nhap vao so nguoi phu thuoc: "))
if tn < 0:
    print("Loi cu phap, vui long nhap lai")
tntt = tn - 11000000 - (dpdnt*4400000)
if tntt <= 0:
    print("Voi thu nhap nay ban chua can phai nop thue tncn")
elif tntt <= 5000000:
    tienthue = tntt/100 * 5
elif tntt <= 10000000:
    tienthue = ((tntt-5000000)/100)*10 + (5000000/100)*5
elif tntt <= 18000000:
    tienthue = ((tntt-10000000)/100)*15 + (5000000/100)*5 + (5000000/100)*10
elif tntt <= 32000000:
    tienthue = ((tntt-18000000)/100)*20 + (5000000/100)*5 + (5000000/100)*10 + (8000000/100)*15
elif tntt <= 52000000:
    tienthue = ((tntt-32000000)/100)*25 + (5000000/100)*5 + (5000000/100)*10 + (8000000/100)*15 + (14000000/100)*20
elif tntt <= 80000000:
    tienthue = ((tntt-52000000)/100)*30 + (5000000/100)*5 + (5000000/100)*10 + (8000000/100)*15 + (14000000/100)*20 + (20000000/100)*25
else:
    tienthue = ((tntt-80000000)/100)*35 + (5000000/100)*5 + (5000000/100)*10 + (8000000/100)*15 + (14000000/100)*20 + (20000000/100)*25 + (28000000/100)*30
print(f'Tien thue thu nhap ca nhan phai tra la: {tienthue}')

    