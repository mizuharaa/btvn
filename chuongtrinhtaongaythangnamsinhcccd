import random
SoNguoi = int(input("Nhap vao so nguoi: "))
decision = input("Nam hay nu? ")
list_id = []
list_ngaysinh = []
list_thangsinh = []
list_namsinh = []
for i in range(SoNguoi):
    a = random.randint(1000000,9999999)
    ngaySinh = random.randint(1, 31)
    list_ngaysinh.append(ngaySinh)
    thangSinh = random.randint(1,12)
    list_thangsinh.append(thangSinh)
    namSinh = random.randint(1970, 2008)
    list_namsinh.append(namSinh)
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
    if decision == "Nam" or decision == "nam":
        print(HovaTenNam)
        ns = str(random.choice(list_ngaysinh)) + '/' + str(random.choice(list_thangsinh)) + '/' + str(random.choice(list_namsinh))
        print(f'Ngay sinh la: {ns}')
        cccd = random.choice(list_id)
        print(f"CCCD: {cccd}")
    elif decision == "Nu" or decision == "nu":
        print(HovaTenNu)
        nd = str(random.choice(list_ngaysinh)) + '/' + str(random.choice(list_thangsinh)) +'/' + str(random.choice(list_namsinh))
        print(f'Ngay sinh la: {nd}')
        cccd1 = random.choice(list_id)
        print(f"CCCD: {cccd1}")
    else:
        print('Vui long nhap dung cu phap!')
        
