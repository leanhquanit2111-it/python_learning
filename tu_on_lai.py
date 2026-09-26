"""print('====Máy tính====')
choose = int(input('Chọn phép tính: '))
a = float(input('Nhập số thứ nhất :'))
b = float(input('Nhập số thứ hai: '))

if choose == 1:
    print('1. Cộng', a + b)
elif choose == 2:
    print('2. Trừ', a - b)
elif choose == 3:
    print('3. Nhân', a*b)
elif choose == 4:
    if b == 0:
        print("Không thể chia cho 0")
    else:
        print("4. Chia", a / b)
else:
    print("Lựa chọn không hợp lệ")"""

#Bài 2:
"""diem_py = float(input())
diem_eng = float(input())
diem_math = float(input())
diem_tb = (diem_py + diem_eng + diem_math) / 3
if diem_py < 0 or diem_py > 10:
    print("Điểm không hợp lệ")
elif diem_eng < 0 or diem_eng > 10:
    print("Điểm không hợp lệ")
elif diem_math < 0 or diem_math > 10:
    print("Điểm không hợp lệ")
elif diem_py < 4 or diem_eng < 4 or diem_math < 4:
    print("trượt")
elif diem_tb >= 8:
    print("giỏi")
elif diem_tb >= 6.5:
    print("khá")
elif diem_tb >= 5:
    print("trung bình")
else:
    print("yếu")"""
#Câu 3
so_du = 5000000
while True:
    check = int(input())

    if check == 1:
        print(so_du)
        
    elif check == 2:
        out1 = int(input("nhập số tiền muốn rút"))
        if out1 > so_du:
            print('Không đủ số dư')
        elif out1 <= 0:
            print('Số tiền không hợp lệ')
        else:
            so_du -= out1
            print("Rút thành công",so_du)
      
            
            
    elif check == 3:
        in1 = int(input('Nhập tiền nạp '))
        if in1 <= 0:
            print("Không hợp lệ")
        else:
            so_du += in1
            print("Cộng vào số dư",so_du)
       
    elif check == 4:
        print("Cảm ơn bạn đã sử dụng")  
        break      
    else:
        print("Lựa chọn không hợp lệ")
    


