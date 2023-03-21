a = input("Nhap vao mot chuoi gom chu cai va so: ")
tongchusochan = a.count("2")*2 + a.count("4")*4 + a.count("6")*6 + a.count("8")*8
tongchusole = a.count("1") + a.count("3")*3 + a.count("5")*5 + a.count("7")*7 + a.count("9")*9
print(f"Tong cac chu so chan la: {tongchusochan} \n Tong cac chu so le la: {tongchusole}")
