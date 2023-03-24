maths = float(input("Nhap vao diem Toan: "))
phys = float(input("Nhap vao diem Ly: "))
chems = float(input("Nhap vao diem Hoa: "))
dtk = (maths * 2 + phys + chems)/4
print(f"Diem tong ket la {dtk}")
hocluc = "Loi du lieu" if dtk < 0 or dtk > 10 else "A: Gioi" if dtk >= 8.5 else "B+: Kha gioi" if dtk >= 8.0 else "B: Kha" if dtk >= 7.0 else "C+: Trung binh kha" if dtk >= 6.5 else "C: Trung binh" if dtk >= 5.5 else "D+: Trung binh yeu" if dtk >= 5.0 else "D: Yeu" if dtk >= 4.0 else "F: Kem"
print(hocluc)