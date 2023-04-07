def sumExponent(limit = 200000, count = 8, power = 5):
    '''
Hàm tìm 'count' số nhỏ hơn 'limit' để tổng lũy thừa power các chữ số trong số đó bằng chính số đó
Parameters: limit(giới hạn muốn tìm từ 0 đến n); count(các số muốn tìm); power(số mũ)
    '''
    numbs = ''
    sum = 0
    found = 0
    for num in range(0, limit):
        if found == count or num == limit:
            break
        for i in str(num):
            sum += int(i) ** power
        if sum == num:
            found += 1
            numbs += str(num) + '|'
        sum = 0
    return numbs, found
sumExpo = sumExponent(200000,5,4)
print(sumExpo)
print(sumExponent.__doc__)


