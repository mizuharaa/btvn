import datetime
ngay = None
thang = int(input("Nhap vao thang: "))
nam = int(input("Nhap vao nam: "))
def countDay(thang, nam):
    global ngay
    if (nam % 4 == 0 and thang == 2 and nam %100 != 0) or (nam % 400 == 0 and thang == 2):
        ngay = 29
    else:
        if thang < 1 or thang > 12 or nam < 1601:
            ngay = None
            return ngay
        else:
            if thang == 2:
                ngay = 28
            elif thang % 2 != 0 and thang != 2:
                ngay = 31
            else:
                ngay = 30
    return ngay
songay = countDay(thang, nam)
if songay == None:
    print('Vui long nhap lai so thang')
def countOddEvenWeek(thang, nam):
    text = ''
    for i in range(1, songay + 1, 1):
        mydate = datetime.date(nam, thang, i)
        weekdays = mydate.weekday()
        text += str(weekdays)
        if weekdays == 6:
            text += '|'
    textsplit = text.split('|')
    oddWeeks = 0
    evenWeeks = 0
    totalWeeks = 0
    for j in textsplit:
        totalWeeks += 1
        if len(j) == 7:
            evenWeeks += 1
        else:
            oddWeeks += 1
    return totalWeeks, evenWeeks, oddWeeks
tongtuan, tuanchan, tuanle = countOddEvenWeek(thang, nam)
print(f'Thang {thang}, nam {nam}, co tong so tuan la: {tongtuan} \n co tong so tuan chan la: {tuanchan} \n co tong so tuan le la: {tuanle}')


    

