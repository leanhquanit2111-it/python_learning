my_str_1 = 'Hello' 
my_str_2 = 'World!'

#multi line backspace
my_str_3 = """Multiline
 string"""
my_str_4 = '''Another
 multiline 
 string '''
print(my_str_3,my_str_4)

#wrap "" or ''
msg = "It's a sunny day"
quote = 'She said, "Hello, World!"'
print(msg, quote)

#Escape "" ''
msg1 = 'It\'s a sunny day'#Bo truoc dau '
msg2 = "She said,\"Hello, World\""#Bo truoc dau "
print(msg1,msg2)

#<in> specifies exist or not
my_str = 'Hello World'
print('Hello' in my_str)
print('jf' in my_str)
print('lo' in my_str)

#get length in function strings with len()
str_length = 'Mot tram tu'
print(len(str_length))

#use [] to character u want to acess inside
my_str0 = "Hello World"
print(my_str0[8])
print(my_str0[-1])#La lay chu cuoi cung cua no la d

#ressign string immutable
greeting = 'hi'
greeting = 'hello'
print(greeting)

# not allow
#greeting[0] = 'H'#khong duoc phep sua doi truc tiep trong chuoi


#Concatenating Strings
my_stri1 = 'Hello'
my_stri2 = 'World'
stri1_plus_stri2 = my_stri1 + ' ' + my_stri2#Ghep 2 chuoi lai voi nhau bang dau cong
print(stri1_plus_stri2)
#Repeating Strings = *
sound = 'ha'
repeat_sound = sound * 3 # * giup lap lai so lan minh muon
print(repeat_sound)

#Concatenating with number
namee = 'John Doe'
agee = 26
#concat_name_and_age = namee + agee#Type Error
#print(concat_name_and_age)#Type Error

#use str() to int -> string
name1 = 'John Doe'
age1 = 26
name_plus_age1 = name1 + ' ' + str(age1)
print(name_plus_age1)

#use += to concatenate(like +)
name2 = 'Tom Le'
age2 = 21
name_and_age2 = name2 + ' '
name_and_age2 += str(age2) #+= nhu cach dung + coi nhu co 2 cach
print(name_and_age2)

#String Interpolation
name3 = 'Tom Le'
age3 = 21
name_and_age_3 = f'Hello, my name is {name3} and I {age3} years old.'#dung f'' va P{} de lam nhanh hon voi chuoi khi ket hop chuoi dai voi nhau
print(name_and_age_3)
score3 = 9
score4 = 10
total_score = f'My score Math is {score3} and English is {score4},Total both is {score3 + score4}'#Khi dung cach nao chung ta khong can dung str() vi no da duoc chuyen doi sang noi suy nhung van phai cung 1 data types
print(total_score)