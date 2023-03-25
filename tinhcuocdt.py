sophut = int(input("Nhap vao so phut dien thoai: "))
if sophut < 0:
    print("Vui long nhap lai")
else:
    sotien = 25000 + 600*sophut if sophut <= 50 and sophut >= 0 else 25000 + (sophut-50)*400 + 50*600 if sophut <= 200 else 25000 + (sophut-200)*200 + 50*600 + 150*400
    print(f"So tien can phai tra la: {sotien}")