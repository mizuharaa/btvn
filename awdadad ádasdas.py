import random
SoNguoi = int(input("Nhap vao so nguoi: "))
list_id = []
for i in range(SoNguoi):
    a = random.randint(1000000,9999999)
    if a not in list_id:
        list_id.append(a)
#list cua nam
list_first_name_male = ['Khang', 'Quan', 'Khoa', 'Manh', 'Quoc', 'Tuan', 'Huy', 'Bao', 'Minh']
list_last_name_male = ['Tran', 'Nguyen', 'Vo', 'Phu', 'Le', 'Pham', 'Hoang', 'Huynh', 'Phan']
list_middle_name_male = ['Van', 'Nguyen', 'Minh', 'Quoc']
#list nu
list_first_name_female = ['Ngoc', 'Linh', 'Thu', 'Nghi', 'My', 'Nhi']
list_last_name_female = ['Tran', 'Nguyen', 'Phan', 'Truong', 'Pham', 'Le', 'Ha']
list_middle_name_female = ['Bao', 'Thanh', 'Gia', 'Bao', 'Thuy', 'Dieu', 'Minh', 'Hoai']
for n in range(SoNguoi):
    HovaTenNam = random.choice(list_last_name_male) + " " + random.choice(list_middle_name_male) + " " + random.choice(list_first_name_male)
    HovaTenNu = random.choice(list_last_name_female) + " " + random.choice(list_middle_name_female) + " " + random.choice(list_first_name_female) 
    print(HovaTenNam)
    print(HovaTenNu)