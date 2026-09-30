#list: la 1 chuoi cac phan tu duoc sap xep co the bao gom cac chuoi so hoac tham chi casc danh sach khac. chi mic dau tien co chi so 0
cities = ['Los Angeles', 'London', 'Tokyo']
cities[1] #London
cities[-1] #Tokyo

#list(): chuyen doi iterable thanh 1 danh sach
developer = 'Jessica'
list(developer) #['J', 'e', 's', 's', 'i', 'c', 'a']

#len(): lay do dai cua list
number =[1, 2, 3, 4, 5]
len(number)#5

#update_list
prgm_l = ['Python', 'Java', 'C++', 'Rust']
prgm_l[1] #Java
print(prgm_l)#Python, Java, C++, Rust
#Cap nhat bat ki 1 phan tu nao cung duoc nhung vuot qua danh sach thi gap loi IndexError

#remove_elements_list: del_variable[value]
developerr = ['Jane Doe', 21, 'Tom Le']
del developerr[1]
print(developerr)#Jane Doe, Tom Le

#checking_list: in
prgm_le = ['Python', 'Java', 'C++', 'Rust']
'Rust' in prgm_le #True
'Pythoe' in prgm_le #False

#Working with nested lists
dev = ['Alice', 25,['Python', 'Java', 'C++', 'Rust']]
dev[2]#['Python', 'Java', 'C++', 'Rust']
dev[2][1]# 'Java'

#Giai nen cac gia tri tu danh sach
deve = ['Alice', 34, 'Devops Engineers']
name, age, job = deve
print(name)#Alice
print(age) #34
print(job)#Devops Engineers

#Thu thap bat ki phan tu con lai cua danh sach: *
name, *tom = deve
print(name)# 'Alice'
print(tom)#34, 'Devops Engineers'

#Note: Neu so luong bien o ben trai khong khop voi tong so muc trong danh sach thi ban se nhan duoc Value Errors
#name, age, job, city = deve#ValueErrors

#Slicing_Lists : : similar strings
desserts = ['Cake', 'Cookies', 'Ice  Cream', 'Pie', 'Brownies']
desserts[1:4]# 'Cookies', 'Ice Cream', 'Pie'

#Another thing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[1::2] # 2, 4, 6, 8, 10 #::2 la buoc nhay 2 lan

#Add_in_List: append()
num = [1, 2, 3, 4, 5]
num.append(6)# chi them duoc 1 gia tri
print(num)
#Add in list in list
numb = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numb.append(even_numbers)
print(numb)#1, 2, 3, 4, 5, [6, 8, 10]

#Add list de khong long nhau: extend()
numb.extend(even_numbers)
print(numb)#[1, 2, 3, 4, 5, 6, 8, 10] khong con long nhau nua

#Chen vao 1 phan tu vao 1 chi muc cu the trong list: insert()
numbe = [1, 2, 3, 4, 5]
numbe.insert(2, 2.5) # chen tu so 2 trong list sau 2 la 2.5

#Remove list : remove()
numbe.remove(2)
print(numbe)#[1, 3, 4, 5]
#Note: chi xoa lan xuat hien dau tien cua 1 muc, vi du 50 50 50 thi xoa 1 lan 50 thoi

#de xoa 1 phan tu tai 1 chi muc cu the trong danh sach: pop()
numm = [1, 2, 3, 4, 5]
numm.pop(1)
print(numm)#1,3,4,5
#Note: neu khong them phan tu vao pop thi phan tu cuoi cung se bi xoa

#Lam trong danh sach: clear()
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num1.clear()
print(num1)# []

#Sap xep cac phan tu tai cho : sort()
num2 = [19, 25, 1, 35, 13, 26, 34]
num2.sort()
print(num2)# 1, 13, 19, 25, 26, 34, 35

#1 cach sap xep khac hoat dong voi moi lan lap va tra ve 1 danh sach duoc sap xep moi thay vi sua doi danh sach ban dau
sorted_number = sorted(num2)
print(num2)#[19, 25, 1, 35, 13, 26, 34]
print(sorted_number)# 1, 13, 19, 25, 26, 34, 35

#reverse() : giup dao nguoc danh sach
num2.reverse()
print(num2)# dao nguoc lai cua num2

#index(): tim chi muc dau tien noi co the tim thay 1 phan tu trong danh sach
desserts = ['Cake', 'Cookies', 'Ice  Cream', 'Pie', 'Brownies']
desserts.index('Cookies')
print(desserts)#1
#Neu khong thay phan tu phu hop thi se dua ra ValueErrors

