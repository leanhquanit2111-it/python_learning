#conditional statement: cau lenh co dieu kien

#comparison operator: toan tu so sanh
print(3>4)#False
print(3==3)#True
print(3!=4)#True
print(3<4)#True     
print(3<=4)#True    
print(3>=4)#False


#if,else,elif statement
if 5<3:
    pass #dung de giu cho cho ma~ trong tuong lai

#example
age = 18
if age <= 18:
    print('You are an adult')#Python khuyen nen thut le tam 4 khoang trang
elif age < 17:
    print('You are out')
elif age < 16:
    print('You so good')
else:
    print("You aren't an adult yet")


#boolean operator
is_citizen = False 
age = 25
if is_citizen:#Cau lenh nay false nen khong chay gi ca
    if age > 19:
        print('You r an adult')
else:# phai de y thut le ca neu nam trong if thu 2 thi neu dieu kien la false o thu nhat thi no se khong hien gi
        print('You are not an adult')


#truthy and falsy
#dung hay sai trong ngu canh logicc
#vi du nhu false, 0, 0.0, ""
#neu  muon kiem tra dung/sai thi co cau lenh bool()
print(bool(False))#false
print(bool(0))#false
print(bool(""))#false
print(bool(True))#true
print(bool(1))#true
print(bool('Hello'))#true

#toan tu logic: and, or, not
#and: xem 2 dieu kien co dung hay khong bat buoc ca 2 dung moi duoc, con 1 trong 2 cai sai thi chac chan la false
#example
is_citizen1 = True
age1 = 25
print(is_citizen1 and age1)#25
if is_citizen1 and age1 > 18:
    print('Correct')
else:
    print('False')


#or: 1 trong 2 dieu kien dung thi true
#dung de kien tra 1 hoac nhieu bieu thuc co dung hay sai
#example
age2 = 19
iss = True
if age2 < 18 or iss:#Dieu kien 2 dung nen if chay khoi lenh 
    print('Correctly')
else:
    print("Wrong")


#not: chuyen tu dung thanh sai, sai thanh dung
#su dung trong cac cau dkien de ktra xem dieu gi do khong dung hay sai
#example
is_admin = False
if not is_admin:
    print('Access denied')
else:
    print('This is admin')



