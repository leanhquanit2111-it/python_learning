#Ôn tập kiến ​​thức cơ bản về Python
#Python là gì?
#Giới thiệu : Python là một ngôn ngữ lập trình đa năng nổi tiếng với sự đơn giản và dễ sử dụng. Python được sử dụng trong nhiều lĩnh vực như khoa học dữ liệu và máy học, phát triển web, lập trình kịch bản và tự động hóa, hệ thống nhúng và IoT, và nhiều lĩnh vực khác nữa.
#Các trường hợp sử dụng phổ biến : Python được sử dụng trong khoa học dữ liệu, học máy, phát triển web, an ninh mạng, tự động hóa và máy tính siêu nhỏ như Raspberry Pi và các bo mạch tương thích MicroPython.
#Biến số
#Khai báo biến : Để khai báo một biến, bạn bắt đầu với tên biến, tiếp theo là toán tử gán ( =) và sau đó là giá trị. Giá trị này có thể là số, chuỗi, boolean, v.v. Dưới đây là một số ví dụ:
name = 'John Doe'
age = 25
#Quy ước đặt tên cho biến : Dưới đây là các quy ước đặt tên bạn nên sử dụng cho biến:

#Tên biến chỉ có thể bắt đầu bằng một chữ cái hoặc dấu gạch dưới (_), không được bắt đầu bằng số.
#Tên biến chỉ được chứa các ký tự chữ và số (az, AZ, 0-9) và dấu gạch dưới (_).
#Tên biến phân biệt chữ hoa chữ thường — age, Age, và AGEđều được coi là duy nhất.
#Tên biến không được trùng với các từ khóa dành riêng của Python như if, class, hoặc def.
#Tên biến có nhiều từ được phân cách bằng dấu gạch dưới. Ví dụ: snake_case.
#Bình luận
#Chú thích một dòng : Loại chú thích này nên được sử dụng cho những ghi chú ngắn mà bạn muốn để lại trong mã nguồn của mình.
# This is a single line comment
#Chú thích nhiều dòng : Bạn có thể sử dụng ký tự #xuống dòng ở đầu mỗi dòng để tạo chú thích trải dài trên nhiều dòng.
# This is a multi-line comment.
# Here is some code commented out.
#
# name = 'John Doe'
# age = 25
print()#Chức năng : Để in dữ liệu ra thiết bị đầu cuối, bạn có thể sử dụng print()hàm như sau:
print('Hello world!') # Hello world!
#Các kiểu dữ liệu phổ biến trong Python
#Giới thiệu : Python là một ngôn ngữ kiểu động, nghĩa là bạn không cần phải khai báo kiểu dữ liệu của biến. Python sẽ tự động xác định kiểu dữ liệu dựa trên giá trị được gán cho biến đó.
#Số nguyên : Một số nguyên không có phần thập phân:
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10
#Số thực (Float) : Một số có phần thập phân:
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5
#Chuỗi ký tự : Một chuỗi các ký tự được đặt trong dấu ngoặc kép:
my_string_var = 'hello'
print('String:', my_string_var) # String: hello
Boolean #: #Một giá trị biểu thị một trong hai Truetrạng thái False:
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
#Python còn có các kiểu dữ liệu khác. Bạn sẽ học từng kiểu khi cần dùng đến chúng lần đầu.

type()#Hàm : Để xem kiểu dữ liệu của một biến, bạn có thể sử dụng type()hàm như sau:
greeting = 'Hello there!'
age = 21

print(type(greeting)) # <class 'str'>
print(type(age)) # <class 'int'>
isinstance()#Hàm : Hàm này được sử dụng để kiểm tra xem một biến có khớp với một kiểu dữ liệu cụ thể hay không:
greeting = 'Hello world'
name = 'John Doe'

print(isinstance(greeting, str)) # True
print(isinstance(name, int)) # False
#Làm việc với chuỗi ký tự
#Định nghĩa : Chuỗi ký tự là bất biến, nghĩa là bạn không thể thay đổi chúng sau khi đã tạo ra. Trong Python, bạn có thể sử dụng dấu ngoặc đơn hoặc dấu ngoặc kép. Hãy chọn một kiểu và sử dụng nó một cách nhất quán:
developer = 'Jessica'
city = "Los Angeles"
#Truy cập ký tự từ chuỗi : Bạn có thể truy cập các ký tự từ chuỗi bằng cách sử dụng cú pháp ngoặc vuông như sau:
my_str = 'Hello world'

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l
#Thoát khỏi chuỗi ký tự đặc biệt : Bạn có thể sử dụng dấu gạch chéo ngược ( \\) nếu chuỗi của bạn chứa dấu ngoặc kép như thế này:
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
#Nối chuỗi : Để nối các chuỗi, bạn có thể sử dụng +toán tử như sau:
developer = 'Jessica'
print('My name is ' + developer + '.') # My name is Jessica.
#Một cách khác để nối chuỗi là sử dụng +=toán tử. Toán tử này được dùng để thực hiện cả phép nối và phép gán trong cùng một bước như sau:

greeting = 'My name is '
developer = 'Jessica.'

greeting += developer
print(greeting) # My name is Jessica.
#f-stringsĐây là viết tắt của chuỗi ký tự định dạng (formatted string literals). Nó cho phép bạn xử lý nội suy và thực hiện một số phép nối chuỗi với cú pháp ngắn gọn và dễ đọc:
developer = 'Jessica'
greeting = f'My name is {developer}.'
print(greeting) # My name is Jessica.
#Cắt chuỗi : Đây là thao tác trích xuất các phần của một chuỗi. Cú pháp cơ bản như sau:
str[start:stop:step]
#Vị trí bắt đầu biểu thị chỉ số mà quá trình trích xuất nên bắt đầu. Vị trí kết thúc là nơi mà lát cắt nên kết thúc. Vị trí này không bao gồm cả hai đầu. Vị trí bước biểu thị khoảng tăng dần cho việc cắt lát. Dưới đây là một số ví dụ:

message = 'Python is fun!'

print(message[0:6])  # Python
print(message[7:])  # is fun!
print(message[::2])  # Pto sfn
#Lấy độ dài của chuỗi : len()Hàm này được sử dụng để trả về số lượng ký tự trong chuỗi:
developer = 'Jessica'

print(len(developer)) # 7
#Làm việc với inngười vận hành
#in Toán tử : Toán tử này trả về giá trị boolean cho biết ký tự hoặc các ký tự đó có tồn tại trong chuỗi hay không.
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
#Các phương thức chuỗi thông dụng
str.upper()#: #Hàm này trả về một chuỗi mới với tất cả các ký tự được chuyển đổi thành chữ hoa:
developer = 'Jessica'

print(developer.upper()) # JESSICA
str.lower()#: #Hàm này trả về một chuỗi mới với tất cả các ký tự được chuyển đổi thành chữ thường:
developer = 'Jessica'

print(developer.lower()) # jessica
str.strip()#: #Phương thức này trả về một bản sao của chuỗi đã loại bỏ các ký tự đầu và cuối được chỉ định (nếu không có đối số nào được truyền cho phương thức, nó sẽ loại bỏ khoảng trắng ở đầu và cuối).
greeting = '  hello world  '

trimmed_my_str = greeting.strip()
print(trimmed_my_str)  # 'hello world'
replace()#Hàm này trả về một chuỗi mới trong đó tất cả các lần xuất hiện của chuỗi cũ được thay thế bằng chuỗi mới.
greeting = 'hello world'

replaced_my_str = greeting.replace('hello', 'hi')
print(replaced_my_str)  # 'hi world'
split()#Chức năng này được sử dụng để tách một chuỗi thành một danh sách bằng cách sử dụng một dấu phân cách được chỉ định. Dấu phân cách là một chuỗi xác định vị trí tách chuỗi.
dashed_name = 'example-dashed-name'

split_words = dashed_name.split('-')
print(split_words)  # ['example', 'dashed', 'name']
join()#Chức năng này được sử dụng để nối một tập hợp các chuỗi thành một chuỗi duy nhất có dấu phân cách.
example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # example dashed name
str.startswith(prefix)#Hàm này trả về giá trị boolean cho biết liệu một chuỗi có bắt đầu bằng tiền tố được chỉ định hay không:
developer = 'Naomi'

result = developer.startswith('N')
print(result)  # True
str.endswith(suffix)#Hàm này trả về giá trị boolean cho biết liệu một chuỗi có kết thúc bằng hậu tố được chỉ định hay không:
developer = 'Naomi'

result = developer.endswith('N')
print(result)  # False
str.find()#: #Hàm này trả về chỉ mục của lần xuất hiện đầu tiên của một chuỗi con. Nếu không tìm thấy, thì -1sẽ trả về:
developer = 'Naomi'

result = developer.find('N')
print(result)  # 0

city = 'Los Angeles'
print(city.find('New')) # -1
#str.count(substring)#:# Hàm này đếm số lần một chuỗi con xuất hiện trong một chuỗi:
city = 'Los Angeles'
print(city.count('e')) # 2
str.capitalize()#Hàm này trả về một chuỗi mới với ký tự đầu tiên được viết hoa và các ký tự còn lại được viết thường:
dessert = 'chocolate cake'
print(dessert.capitalize()) # Chocolate cake
str.isupper()#Hàm này trả về true Truenếu tất cả các chữ cái trong chuỗi đều viết hoa, và false Falsenếu ngược lại:
dessert = 'chocolate cake'
print(dessert.isupper()) # False
str.islower()#Hàm này trả về true Truenếu tất cả các chữ cái trong chuỗi đều là chữ thường, và false Falsenếu ngược lại:
dessert = 'chocolate cake'
print(dessert.islower()) # True
str.title()#: #Hàm này trả về một chuỗi mới với chữ cái đầu tiên của mỗi từ được viết hoa:
city = 'los angeles'
print(city.title()) # Los Angeles
str.maketrans()#Phương pháp này được sử dụng để tạo bảng ánh xạ ký tự 1:1 cho việc dịch. Nó thường được sử dụng cùng với phương translate()pháp áp dụng bảng đó cho một chuỗi và trả về kết quả đã dịch.
trans_table = str.maketrans('abc', '123')
print(trans_table) # {97: 49, 98: 50, 99: 51}

result = 'abcabc'.translate(trans_table)
print(result)  # 123123
#Các phép toán thông dụng với số nguyên và số thực
#Các phép toán cơ bản : Trong Python, bạn có thể thực hiện các phép toán cơ bản với số nguyên và số thực, bao gồm cộng, trừ, nhân và chia.
int_1 = 56
int_2 = 12
float_1 = 5.4
float_2 = 12.0

# Addition

print('Integer Addition:', int_1 + int_2) # Integer Addition: 68
print('Float Addition:', float_1 + float_2) # Float Addition: 17.4

# Subtraction

print('Int Subtraction:', int_1 - int_2) # Int Subtraction: 44
print('Float Subtraction:',  float_2 - float_1) # Float Subtraction: 6.6

# Multiplication

print('Int Multiplication:', int_1 * int_2) # Int Multiplication: 672
print('Float Multiplication:', float_2 * float_1) # Float Multiplication: 64.80000000000001

# Division

print('Division:', int_1 / int_2) # Division: 4.666666666666667
print('Float Division:', float_2 / float_1) # Float Division: 2.222222222222222
#Khi bạn cộng một số thực và một số nguyên, kết quả sẽ được chuyển đổi thành số thực như sau:

int_1 = 56
float_1 = 5.4

print(int_1 + float_1) # 61.4
#Toán tử modulo ( %) : Toán tử này trả về phần dư khi một số được chia cho một số khác:
int_1 = 56
int_2 = 12

print(int_1 % int_2) # 8
#Phép chia lấy phần nguyên (Floor Division //) : Toán tử này được sử dụng để chia hai số và làm tròn kết quả xuống số nguyên gần nhất:
int_1 = 56
int_2 = 12

print(int_1 // int_2) # 4
#Toán tử lũy thừa ( **) : Toán tử này được sử dụng để nâng một số lên lũy thừa của một số khác:
int_1 = 4
int_2 = 2

print(int_1 ** int_2) # 16
float()#Chức năng : Bạn có thể sử dụng chức năng này để chuyển đổi số nguyên sang số thực.
num = 4

print(float(num)) # 4.0
int()#Chức năng : Bạn có thể sử dụng chức năng này để chuyển đổi số thực sang số nguyên.
num = 4.0

print(int(num)) # 4
round()#Chức năng : Chức năng này được sử dụng để làm tròn một số đến số nguyên gần nhất:
num_1 = 3.4
num_2 = 7.7

print(round(num_1)) # 3
print(round(num_2)) # 8
abs()#Hàm : Hàm này được sử dụng để trả về giá trị tuyệt đối của một số:
num = -13

print(abs(num)) # 13
pow()#Hàm : Hàm này được dùng để nâng một số lên lũy thừa một số khác:
result = pow(2, 3) 
print(result)  # 8
#Bài tập bổ sung
#Định nghĩa : Phép gán tăng cường áp dụng một phép toán cho một biến và lưu kết quả trở lại vào chính biến đó, tất cả chỉ trong một bước.
# Addition assignment 
my_var = 10
my_var += 5

print(my_var) # 15

# Subtraction assignment
count = 14
count -= 3

print(count) # 11

# Multiplication assignment 
product = 65
product *= 7

print(product) # 455

# Division assignment 
price = 100
price /= 4

print(price) # 25.0

# Floor Division assignment 
total_pages = 23
total_pages //= 5

print(total_pages) # 4

# Modulo assignment 
bits = 35
bits %= 2

print(bits) # 1

# Exponentiation assignment 
power = 2
power **= 3

print(power) # 8
#Làm việc với các hàm
#Định nghĩa : Hàm là những đoạn mã có thể tái sử dụng, nhận đầu vào (tham số) và trả về đầu ra. Để gọi một hàm, bạn cần tham chiếu đến tên hàm, theo sau là một cặp dấu ngoặc đơn:
# Defining a function

def get_sum(num_1, num_2):
    return num_1 + num_2

result = get_sum(3, 4) # function call
print(result) # 7
#Nếu một hàm không trả về giá trị nào được chỉ định rõ ràng, thì giá trị trả về mặc định là None:

def greet():
    print('hello') 

result = greet() # hello
print(result) # None
#Bạn cũng có thể cung cấp giá trị mặc định cho các tham số như sau:

def get_sum(num_1, num_2=2):
    return num_1 + num_2

result = get_sum(3) 
print(result) # 5
#Nếu bạn gọi hàm mà không cung cấp đủ số lượng tham số, bạn sẽ nhận được lỗi TypeError:

def calculate_sum(a, b):
    print(a + b)

calculate_sum()

# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
#Các chức năng tích hợp thông dụng
input()#Chức năng : Chức năng này được sử dụng để yêu cầu người dùng nhập thông tin:
name = input('What is your name?') # User types 'Kolade' and presses Enter  
print('Hello', name) # Hello Kolade
int()#Hàm : Hàm này được sử dụng để chuyển đổi một số, giá trị boolean hoặc chuỗi số thành số nguyên:
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 
#Phạm vi trong Python
#Python có thêm các quy tắc về phạm vi. Hiện tại, chúng ta hãy tập trung vào phạm vi cục bộ và phạm vi toàn cục.

#Phạm vi cục bộ : Một biến được tạo ra bên trong một hàm chỉ có thể được sử dụng trong phạm vi hàm đó. Tham số của hàm cũng là các biến cục bộ.
def my_func():
    num = 10
    print(num)
#Phạm vi toàn cục : Một biến được tạo bên ngoài hàm có thể được sử dụng cả bên trong và bên ngoài hàm.
tax = 0.70 

def get_total(subtotal):
    total = subtotal + (subtotal * tax)
    return total

print(get_total(100))  # 170.0
#Toán tử so sánh
#Equal( ==)# : Kiểm tra xem hai giá trị có bằng nhau hay không:
print(3 == 4) # False
#Không bằng ( !=)# : Kiểm tra xem hai giá trị có khác nhau hay không:
print(3 != 4) # True
#>Kiểm tra xem một giá trị có lớn hơn giá trị khác hay không :
print(3 > 4) # False
#Nhỏ hơn nghiêm ngặt ( <) : Kiểm tra xem một giá trị có nhỏ hơn giá trị khác hay không:
print(3 < 4) # True
#Lớn hơn hoặc bằng ( >=) : Kiểm tra xem một giá trị có lớn hơn hoặc bằng giá trị khác hay không:
print(3 >= 4) # False
#Nhỏ hơn hoặc bằng ( <=) : Kiểm tra xem một giá trị có nhỏ hơn hoặc bằng giá trị khác hay không:
print(3 <= 4) # True
#Làm việc với if, elifvà elsecác câu lệnh
#ifCâu lệnh : Đây là các điều kiện được sử dụng để xác định xem một điều gì đó có đúng hay không. Nếu điều kiện được đánh giá là đúng True, thì khối mã đó sẽ được thực thi.
age = 18

if age >= 18:
    print('You are an adult') # You are an adult
#elifMệnh đề : Đây là các điều kiện xuất hiện sau một ifcâu lệnh. Một elifmệnh đề chỉ được thực thi nếu tất cả các điều kiện trước đó đều đúng Falsevà điều kiện của chính nó cũng đúng True.
age = 16

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')  # You are a teenager
#elseĐiều khoản : Điều này sẽ được thực thi nếu không có điều kiện nào khác được đánh giá là đúng True.
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')  # You are a child
#Bạn cũng có thể sử dụng ifcác câu lệnh lồng nhau như thế này:

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
#Giá trị đúng và giá trị sai
#Định nghĩa : Trong Python, mỗi giá trị đều có một giá trị boolean vốn có, hay một ý nghĩa tích hợp sẵn về việc nó nên được coi là đúng Truehay sai Falsetrong một ngữ cảnh logic. Nhiều giá trị được coi là đúng (truthy), nghĩa là chúng được đánh giá là đúng Truetrong một ngữ cảnh logic. Những giá trị khác là sai (falsy), nghĩa là chúng được đánh giá là sai (false False). Dưới đây là một số ví dụ về các giá trị sai:
None
False
#Integer 0
#Float 0.0
#Empty strings ''
#Các giá trị khác như số khác 0 và chuỗi không rỗng cũng là giá trị đúng (truthy).

#Làm việc với bool()hàm
#Định nghĩa : Nếu bạn muốn kiểm tra xem một giá trị là đúng hay sai, bạn có thể sử dụng hàm tích hợp sẵn bool(). Hàm này chuyển đổi rõ ràng một giá trị thành giá trị boolean tương ứng và trả Truevề giá trị đúng và Falsegiá trị sai. Dưới đây là một vài ví dụ:
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
#Toán tử Boolean và rút gọn mạch
#Định nghĩa : Đây là các toán tử đặc biệt cho phép bạn kết hợp nhiều biểu thức để tạo ra logic ra quyết định phức tạp hơn trong mã của mình. Có ba toán tử Boolean trong Python: and, or, và not.
#andToán tử : Toán tử này nhận hai toán hạng và trả về toán hạng đầu tiên nếu nó là falsy, ngược lại, nó trả về toán hạng thứ hai. Cả hai toán hạng phải là truthy thì biểu thức mới trả về giá trị truthy.
is_citizen = True
age = 25

print(is_citizen and age) # 25
#Bạn cũng có thể sử dụng andtoán tử này trong các câu điều kiện như sau:

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
#orToán tử : Toán tử này trả về toán hạng đầu tiên nếu nó đúng, ngược lại, nó trả về toán hạng thứ hai. Một orbiểu thức trả về giá trị đúng nếu ít nhất một toán hạng đúng. Sau đây là một ví dụ:
age = 19
is_employed = False

print(age or is_employed) # 19
#Tương tự như với andtoán tử, bạn có thể sử dụng ortoán tử trong các câu điều kiện như sau:

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
#Rút ngắn mạch : Toán tử andAND và orOR được gọi là toán tử rút ngắn mạch. Rút ngắn mạch có nghĩa là Python kiểm tra các giá trị từ trái sang phải và dừng lại ngay khi xác định được kết quả cuối cùng.
#notToán tử : Toán tử này nhận một toán hạng và đảo ngược giá trị boolean của nó. Nó chuyển đổi các giá trị đúng thành Falsevà các giá trị sai thành True. Không giống như các toán tử trước đó mà chúng ta đã xem xét, notluôn trả về Truehoặc False. Dưới đây là một số ví dụ:
print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy
#Dưới đây là một ví dụ về nottoán tử trong câu điều kiện:

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')