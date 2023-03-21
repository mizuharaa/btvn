check_na = input("Nhap vao mot chuoi bat ky: ")
check_na = check_na.lower()
ktra = "u" in check_na or "e" in check_na or "o" in check_na or "a" in check_na or "i" in check_na
print("Chuoi ban vua nhap co nguyen am: ", ktra)
soNguyenAm = check_na.count("u") + check_na.count("e") + check_na.count("o") + check_na.count("a") + check_na.count("i")
print(f"So nguyen am trong chuoi la: {soNguyenAm}")
chuSo = check_na.count("1") + check_na.count("2") + check_na.count("3") + check_na.count("4") + check_na.count("5") + check_na.count("6") + check_na.count("7") + check_na.count("8") + check_na.count("9") + check_na.count("0")
print(f"So chu so trong chuoi la: {chuSo}")