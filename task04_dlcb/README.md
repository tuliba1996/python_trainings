#Mục lục.

[1.Sử dụng Python như máy tính (Calculator)](#Calculator)

[2.Tìm hiểu kiểu dữ liệu number. Khác với C chỗ nào?](#number)

[3.Tìm hiểu về String: nối chuỗi, cắt lát (slicing)](#string)

[4.Tìm hiểu list 1 chiều và nhiều chiều: nối danh sách, cắt lắt.](#list)

[5.Tìm hiểu Boolean.](#Boolean) 

#1.Sử dụng Python như máy tính (Calculator)

Chúng ta có thể sử dụng `Python` như một máy tính đơn giản. thực hiện các phép toán `+`,`-`,`*`,`/`. ví dụ:


`IMG`
Các toán tử số học cơ bản:

|**Toán tử**|**Miêu tả**|
|-----------|-----------|
| + | phép cộng|
| - | phép trừ|
| * | phép nhân|
| / | phép chia|
| // | phép chia lấy phần nguyên|
| % | phép chia lấy dư|
| ** | phép lấy số mũ|

#2.Tìm hiểu kiểu dữ liệu number. Khác với C chỗ nào?

Kiểu dữ liệu `Number` lưu trữ các giá trị số. Chúng là các kiểu dữ liệu **immutable**, hay là kiểu dữ liệu không thay đổi, nghĩa là các thay đổi về giá trị của kiểu dữ liệu số này sẽ tạo ra một đối tượng được cấp phát mới.

`Python` hỗ trợ 4 kiểu dữ liệu số, đó là:

- Kiểu **int**: kiểu số nguyên không có dấu thập phân.

- Kiểu **long**: là các số nguyên không giới hạn kích cỡ, được theo sau bởi một chữ l hoặc chữ L.

- Kiểu **float**: số thực với dấu thập phân. Kiểu này cũng có thể được viết ở dạng số mũ của 10 với E hoặc e như (2.5e2 = 2.5 x 102 = 250).

- Kiểu **complex**: là trong dạng a + bJ, với a và b là số thực và J (hoặc j) biểu diễn căn bậc hai của -1. Phần thực là a và phần ảo là b. Nói chung, số phức không được sử dụng nhiều trong lập trình Python.

Trong `Python` khác với `C` ở các điểm:

- Trong `C` ta phải khai báo kiểu dữ liệu trước, ví dụ `int a = 5`. còn trong `Python` thì không cần, ta có thể khai báo trực tiếp `a = 5`.
- Trong `Python` có hỗ trợ kiểu dữ liệu **complex** còn `C` thì không. 


#3.Tìm hiểu về String: nối chuỗi, cắt lát (slicing)

Kiểu dữ liệu `String` được xác định khi giá trị được gán cho nó nằm giữa cặp dấu `‘ ‘` hoặc `” “`.

    'lang tu sau'
    "Sầu sô ciu"

`IMG`

Nối chuỗi:

    a = 'Py'
    b = 'thon'
    a + b = 'Python'
    c = 'Hoc' + a + b

`IMG`

Cắt chuỗi:

    text = 'hello world'
    text[0]
    >> 'h'
    text[0:2]
    >> 'he'

`IMG`

#4.Tìm hiểu list 1 chiều và nhiều chiều: nối danh sách, cắt lắt.

**List** trong `Python` là một kiểu dữ liệu phức hợp linh hoạt, **Lists** chứa những phần tử được ngăn cách nhau bởi dấu "," và nằm trong cặp dấu ngoặc vuông "[ ]". Theo một vài đánh giá thì **Lists** trong `Python` gần giống với **Array** trong `C`, sự khác biệt chính là các phần tử của **Lists** có thể tồn tài nhiều kiểu dữ liệu khác nhau.

Ví dụ
- List 1 chiều

    list = ['Sau', 12 , 2 , '5.2']
    fruit = ['apple','grap','orange','lemon']

- List nhiều chiều

    color = ['red',[1,2,3,4,5],'yellow','pink','blue']


Nối list:


    fruit = ['apple','grap','orange','lemon']
    drink = ['coffee','milk','lemonade','wine']
    fruit + drink 
    >> ['apple','grap','orange','lemon','coffee','milk','lemonade','wine']

`IMG`

Cắt danh sách:

    fruit = ['apple','grap','orange','lemon']
    fruit[0]
    >> ['apple']
    fruit[0:3]
    >> ['apple', 'grap', 'orange']
    // list nhiều chiều
    color = ['red',[1,2,3,4,5],'yellow','pink','blue']
    color[1][0:3]
    >> [1,2,3]


`IMG`

#5.Tìm hiểu Boolean.

Kiểu **Boolean** là kiểu chỉ có 2 giá trị **True(đúng)** và **False(sai)**. Trong Python, có hai toán tử cơ bản liên quan đến boolean là **Toán tử so sánh** và **Toán tử logic**.

Toán tử so sánh:

`IMG`

Toán tử logic:

| A | B | And | Or |
|----|-----|----|
| 0 | 0 | 1 | 0 | 
| 0 | 1 | 0 | 1 | 
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Not:

| A | Not A|
|---|---|
| 1 | 0|
| 0 | 1 |
