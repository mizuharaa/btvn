sotd = int(input("Vui long nhap vao so dien: "))
if sotd < 0:
    print("Vui long nhap chinh xac so tien dien")
elif sotd <= 50:
    print(f"So tien dien la: {sotd*1678}")
elif sotd <= 100:
    print(f"So tien dien la: {50*1678 + (sotd - 50)*1734 }")
elif sotd <= 200:
    print(f"So tien dien la: {50*1678 + 50*1734 + ((sotd - 100)*2014)}")
elif sotd <= 300:
    print(f"So tien dien la: {50*1678 + 50*1734 + 100*2014 + ((sotd - 200)*2536)}")
elif sotd <= 400:
    print(f"So tien dien la: {50*1678 + 50*1734 + 100*2014 + 100*2536 + ((sotd-300)*2834)}")
else:
    print(f"So tien dien la: {50*1678 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + ((sotd-400)*2927)}")

