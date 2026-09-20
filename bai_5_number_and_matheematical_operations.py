my_int_1 = 566
my_int_2 = -94
sum_int = my_int_1 + my_int_2
print('Total sum: ', sum_int)
diff_int = my_int_1 - my_int_2
print('Integer Subtraction', diff_int)
multip_int = my_int_1 * my_int_2
print('Integer Multiplication: ', multip_int)
div_int = my_int_1 + my_int_2
print('Integer Devision: ', div_int)
#Float tuong tu: 5.6, 3.0
my_int = 57
my_float = 13.5
sum_both = my_float + my_int
print('Sum: ', sum_both)
print(type(sum_both))

#Modulo (%)
modulo_a = my_int % my_float
print(modulo_a)

#Slas oprerator(//)
sl_infl = my_int // my_float
print(sl_infl)

#asterisk operator(**) : toan tu luy thua vi du 3**4= 3*3*3*3
atr_ifl = my_float ** my_int
print(atr_ifl)

#float()function: doi int thanh float
my_int_3 = 56
my_floats = float(my_int)
print(my_float)#56.00

#int() function
my_float1 = 12.984124
my_intt = int(my_float1)
print(my_intt)#12

#String convert into either a float or int
my_string_cv = '94'
#my_string_cv1 = 'HE' khong duoc chuyen doi tu string sang float voi chu~
my_string_cv=int(my_string_cv)
#my_string_cv1 = float(my_string_cv1)
print(my_string_cv)
#print(my_string_cv1)

#round(): lam tron chu so thap phan
my_r = 4.254
my_r = round(my_r)
print(my_r)

#abs(): tra ve gia tri cua 1 so
my_abs = -20
my_abs = abs(my_abs)
print(my_abs)

#pow(): nang mot so len luy thua cua 1 so khac hoac thuc hien phep luy thua module
result1 = pow(2,3)# 2**3
result2 = pow(2, 3, 5) #(2**3)%5
print(result2)

#augmented assignment: phep gan tang cuong
count = 14
count += 3
print(count)
count -= 3
print(count)
count *= 3
print(count)
count /= 3
print(count)
count //= 3
print(count)
count %= 3
print(count)
count **= 3
print(count)
#Or Strings
greet = "Hello"
greet += 'World'
print(greet)
greet *= 3
print(greet)
#Type Error for string if use -= /=
