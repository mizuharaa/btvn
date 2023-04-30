class Student:
    def __init__(self, identify, fullname, dob, hometown):
        self.identify = identify
        self.fullname = fullname
        self.dob = dob
        self.hometown = hometown
    def info(self):
        print(f'ID: {self.identify}\nHọ và tên: {self.fullname}\nNgày sinh: {self.dob}\nQuê quán: {self.hometown}\n=================================================')

class Student_List():
    def __init__(self, list_student):
        self.list_student = list_student
    def display_info(self):
        for i in self.list_student:
            i.info()
    def add(self, student):
        self.list_student.append(student)
    def update(self,identify, newid, newname, newdob, newhometown):
        ''' 
    Function that replace an existing student with new information passed into the parameters. Parameters(ID, newID, newName, newDOB, newHometown )
        '''
        for stud in self.list_student:
            if stud.identify == identify:
                self.identify = newid
                self.newname = newname
                self.dob = newdob
                self.hometown = newhometown
    def remove(self, student):
        self.list_student.remove(student)
    def search(self, identifykey):
        for j in self.list_student:
            if j.identify == identifykey:
                j.info()
    def sort(self):
        ''' sort_list = sorted(self.list_student, key = lambda stud:stud., reverse = False) '''
        pass

class Runtime:
    def __init__(self, stud_list):
        self.stud_list = stud_list
    def run(self):
        while True:
            self.runTime()
            choice = int(input('Vui long nhap vao lua chon: '))
            print('=' * 20)
            if choice == 1:
                self.stud_list.display_info()
                input('Enter de quay lai')
            elif choice == 2:
                code = int(input('Nhap ma sinh vien: '))
                name = input('Nhap vao ho va ten: ')
                birth = input('Nhap vao ngay thang nam sinh: ')
                hometown = input('Nhap vao que quan')
                newstud = Student(code, name, birth, hometown)
                
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 0:
                exit = input('Ban co chac muon thoat chuong trinh, y/n? ')
                if exit.lower().strip() == 'y':
                    break
            else:
                print('Lua chon nhap vao khong dung')
                ans = input('Vui long enter de thu lai')    
    def runTime(self):
        print('======MANAGE SINH VIEN======')
        print('1. Hien thi danh sach sinh vien')
        print('2. Them sinh vien')
        print('3. Cap nhat sinh vien')
        print('4. Xoa sinh vien')
        print('5. Sap xep danh sach')
        print('0. Thoat chuong trinh')

empty = []
student1 = Student(1806113, 'Trần Nguyên Khang Daniel', '09/08/2007', 'Hà Nội')
student2 = Student(1902938, 'Châu Hải Minh', '28/1/1991', 'TP HCM')
student3 = Student(1289093, 'Kimm', '31/3/2009', 'Hai Phong')
student4 = Student(1832993, 'Hùng Kim Mỹ', '28/9/2007', 'Cần Thơ')
database = Student_List(empty)
database.add(student1)
database.add(student2)
database.add(student3)
database.add(student4)
demo = Runtime(database)
demo.run()