#input function
name = input('What is your name ?')
print('My name is:', name)
#ham int co the chuyen doi so,boolean,string thanh so nguyen
#example
print(int(3.14))
print(int('52'))
print(int(True))
print(int(False))


#dung ham def (variable_()_:)
def hello():
    print('Hello World')

hello()

def caculation_sum(a, b):
    return a + b
# goi ham calculate_sum phai cung cap tham so neu khong se bao la TypeError
print(caculation_sum(9, 12))
#Nhung luc print ra lai bao gia tri la None vay lam sao?


# bien toan cuc va bien cuc bo
# bien duoc ao ben ngoai def co pham vi toan cuc va co the su dung no car ben trong va ben ngoai ham

#bien duoc tao ben trong ham duoc goi la bien cuc bo ban chi co the su dung no ben trong ham do tham so cua ham cung la bien cuc bo
#example
tax_race = 0.1

def calculation_sum1(price):
    tax = price* tax_race
    return tax

print(calculation_sum1(29)) #bien cuc bo
print(tax_race)# no duoc tao ngoai ham nen co the goi
#print(tax) la bien cuc bo ben khong the goi ben ngoai ham duoc
