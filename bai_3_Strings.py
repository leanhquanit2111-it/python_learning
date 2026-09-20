my_str_1 = 'Hello' 
my_str_2 = 'World!'

#multi line backspace
my_str_3 = """Multiline
 string"""
my_str_4 = '''Another
 multiline 
 string '''
print(my_str_3,my_str_4)#multiline (xuong dong) string

#wrap "" or ''
msg = "It's a sunny day"
quote = 'She said, "Hello, World!"'
print(msg, quote) # It's a sunny day

#Escape "" ''
msg1 = 'It\'s a sunny day'#Bo truoc dau '
msg2 = "She said,\"Hello, World\""#Bo truoc dau "
print(msg1,msg2) #It's a sunny day

#<in> specifies exist or not
my_str = 'Hello World'
print('Hello' in my_str)#True
print('jf' in my_str)#False
print('lo' in my_str)#True

#get length in function strings with len()
str_length = 'Mot tram tu'
print(len(str_length))#11

#use [] to character u want to acess inside
my_str0 = "Hello World"
print(my_str0[8])#r
print(my_str0[-1])#La lay chu cuoi cung cua no la d #d

#ressign string immutable
greeting = 'hi'
greeting = 'hello'
print(greeting)#hello

# not allow
#greeting[0] = 'H'#khong duoc phep sua doi truc tiep trong chuoi


#Concatenating Strings
my_stri1 = 'Hello'
my_stri2 = 'World'
stri1_plus_stri2 = my_stri1 + ' ' + my_stri2#Ghep 2 chuoi lai voi nhau bang dau cong
print(stri1_plus_stri2)#Hello World
#Repeating Strings = *
sound = 'ha'
repeat_sound = sound * 3 # * giup lap lai so lan minh muon
print(repeat_sound)#hahaha

#Concatenating with number
namee = 'John Doe'
agee = 26
#concat_name_and_age = namee + agee#Type Error
#print(concat_name_and_age)#Type Error

#use str() to int -> string
name1 = 'John Doe'
age1 = 26
name_plus_age1 = name1 + ' ' + str(age1)
print(name_plus_age1) #John Doe 26

#use += to concatenate(like +)
name2 = 'Tom Le'
age2 = 21
name_and_age2 = name2 + ' '
name_and_age2 += str(age2) #+= nhu cach dung + coi nhu co 2 cach
print(name_and_age2) #Tom Le 21

#String Interpolation
name3 = 'Tom Le'
age3 = 21
name_and_age_3 = f'Hello, my name is {name3} and I {age3} years old.'#dung f'' va P{} de lam nhanh hon voi chuoi khi ket hop chuoi dai voi nhau
print(name_and_age_3)#Hello, my name is Tom Le and I 21 years old.
score3 = 9
score4 = 10
total_score = f'My score Math is {score3} and English is {score4},Total both is {score3 + score4}'#Khi dung cach nao chung ta khong can dung str() vi no da duoc chuyen doi sang noi suy nhung van phai cung 1 data types
print(total_score)#My score Math is 9 and English is 10,Total both is 19

#Slicing Strings
#Use variable[start:stop]
#Example
my_str5 = 'Hello World'
print(my_str5[0:4])# Xuat ra Hell
#Đối với stop thì nó sẽ dừng sau chính nó chứ không dừng ở chính nso
print(my_str5[:7])#Neu khong ghi o start thì nó sẽ bắt đầu từ đầu #Hello W

print(my_str5[5:])#Neu khong ghi o stop thi no se chay tu start den toi da # World
#Note:Slicing Strings not modify the original string
print(my_str5[:])#Chay toan bo chuoi #Hello World

#Next,is var[start:stop:step]
#step duoc goi la buoc nhay?
print(my_str5[0:9:2])#2 tuc la nó nhảy 2 lần #Hlowr
#Trick parameter step
print(my_str5[::-1])#Chay nguoc lai dlrow olleH


#Method on Strings
#Upper
my_str6 = " le anh quan "
print(my_str6.upper())
upper_case_my_string = my_str6.upper()#Viet hoa tat ca cac chu co trong chuoi
print(upper_case_my_string) #LE ANH QUAN

#Lower
lowercase_my_str = my_str6.lower()#Viet thuong tat ca cac  ki tu co trong chuoi
lowercase_my_str = my_str6.lower()
print(lowercase_my_str)#le anh quan

#Strip()
stripcase_my_str = my_str6.strip()
print(stripcase_my_str)
strip1 = "\t Hello World \r"#Xoa ki tu dau va cuoi
print(strip1.strip())#Hello World
strip2 = "--hello--"
print(strip2.strip("-"))#hello
strip3=("xxhelloxx")
print(strip3.strip("x"))#hello
strip4 = "abcHELLOcba"
print(strip4.strip("abc"))#hello

#Replace(old, new)
string_1 = 'Xin chao Tom'
print(string_1.replace('Tom', 'Quân'))#Thay the chuoi cu tu 1 chuoi thanh 1 chuoi moi #Xin chao Quân


#Split()
split1 = "le anh quan"
print(split1.split())#khong co gia tri trong chuoi no se tu tach khoang trang#['le','anh','quan']
print(split1.split("le "))#tach chuoi trong no['','anh quan']

#join()
my_list = ['hello', 'world']
join_list = ' '.join(my_list)#noi 1 chuoi trong danh sach
print(join_list)#hello world

#startswith(prefix): tra ve 1 boolean true or false
my_str = 'hello world'

starts_with_hello = my_str.startswith('h')#tra ve 1 bolean co bat dau bang tien to da chi dinh hay khong
print(starts_with_hello)#true

#endswitch(suffix)
esw = 'maradona isen'
print(esw.endswith('isen'))#Tra ve 1 bolean cho biet lieu 1 chuoi co ket thuc bang hau to da chi dinh hay khong


#find(substring)
fs = 'hello world'
print(fs.find('rld'))#neu nam o so 8 thi bat dau bang chinh r
#con neu khong co chuoi con trong chuoi thi tat nhien no se bao -1


#count(substring)
cs = 'heloooo world'
print(cs.count('o'))#tra ve so lan chuoi con xuat hien trong chuoi #5


#capitalize():in chu dau cau va con lai viet thuong
cl = 'hello world'
upper_cl = cl.capitalize()
print(upper_cl)

#isupper(): tra ve true or false neu tat ca viet hoa thi true false thi viet thuong
isp = 'HELLO WORLD'
print(isp.isupper())#true


#islower(): tra ve true neu viet thuong tat ca con false neu viet hoa tat ca
ilw = 'hello world'
print(ilw.islower())#true

#title: tra ve 1 chuoi moi co chu cai dau tien cua moi tu duoc viet hoa
my_str_title = 'hello world'
print(my_str_title.title())