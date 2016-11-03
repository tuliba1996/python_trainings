#Mục lục
[1.Ý tưởng](#1)
[2.Cách làm](#2)

<a name="1"></a>

#1.Ý tưởng

Với yêu cầu là: **"One small letter, surrounded by EXACTLY three big bodyguards on each of its sides"**. Nghĩa là tìm tất cả các kí tự thường trong chuỗi với điều kiện là 1 kí tự thường phải đứng giữa 3 kí tự in hoa (đúng 3 kí tự in hoa). 

Ví dụ

    AAAbDDDvvvDIIoMMM

Kết quả in ra sẽ được

    'b','o'

<a name="2" =""></a>

#2.Cách làm

- Sử dụng **request** trong thư viện `re` 
- Gửi 1 request là muốn mở cái file `equality.html` và đọc nó. với đường dẫn http://www.pythonchallenge.com/pc/def/equality.html
- sử dụng thêm 1 thư viện `re`.
- khi mình mở đọc file `equality.html` thì trong file đó có code `html`,`css`,`javascript` và cả đoạn text chúng ta cần. Nhưng chúng ta chỉ cần đoạn text.
- Sử dụng hàm **re.findall()** để tìm và lọc ra đoạn text cần.
- Tiếp tục sử dụng hàm **re.findall()** để lọc ra nhưng kí tự thường thoả mãn điều kiện.
























