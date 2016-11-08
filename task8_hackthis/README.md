# Mục lục
[1.Live HTTP header](#1)

[2.Đăng kí account trên hackthissite.org](#2)

[3.Nêu ý tưởng giải Challenge](#3)


<a name="1"></a>

#1.Live HTTP header
Mở trình duyệt Firefox và addon Live HTTP Header.

![](http://i.imgur.com/F0LDx9O.png)

Sau đó vào **Tools** bật **Live HTTP Header** lên. và thử vào `google.com` ta được:

![](http://i.imgur.com/eMDZWcz.png)

Đây là header mà máy ta gửi truy vấn GET đến  `google.com` trên cổng 80 và trình duyệt hiện tại là **Mozilla/5.0 - Gecko/20100101 Firefox/49.0**:

    GET /?gfe_rd=cr&ei=O2IYWLfDJ6nY8geJvo-oDA HTTP/1.1
    Host: www.google.com.vn
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Cookie: NID=90=GtdCZSwkyOoRoQorbeIeU1yExXUQyVLOo2WgqSusYXtcVnhnwHcqxvHyd5VVFZyWN664bI-rlc3f19AGNoV7EXWr9iqr5XXdgWcW1eRjlEkVNGObAf9FBeSs2N-vduUMZGiN; OGPC=5061821-2:; OGP=-5061821:
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1

Kết quả `google` trả về:

    HTTP/2.0 200 OK
    Vary: Accept-Encoding
    Content-Encoding: gzip
    Content-Type: text/javascript; charset=UTF-8
    Date: Mon, 07 Nov 2016 23:56:51 GMT
    Expires: Tue, 07 Nov 2017 23:56:51 GMT
    Last-Modified: Mon, 07 Nov 2016 23:36:04 GMT
    x-content-type-options: nosniff
    Server: sffe
    Content-Length: 137774
    X-XSS-Protection: 1; mode=block
    Cache-Control: public, max-age=31536000
    Age: 58295
    Alt-Svc: quic=":443"; ma=2592000; v="36,35,34"
    X-Firefox-Spdy: h2

Đọc header:
- **HTTP/2.0** : có nghĩa là `www.google.com` đang sử dụng giao thức HTTP phiên bản 2.0 để truyền tín hiệu.
- **200 OK** HTTP status 200 và thông báo là OK => `www.google.com` đang tồn tại và sẵn sàng trả lời truy vấn.
- **Server: sffe => cho biết server mà gg đang sử dụng.
 
<a name="2"></a>

#2.Đăng kí account trên hackthissite.org

<a name="3"></a>

#3.Nêu ý tưởng giải Challenge
- copy 10 word trên hack this site lưu vào file `data.txt`
- tải file `wordlist` về.
- Đọc dữ liệu từ 2 file trên và sử dụng phương thức slpit để cắt từng word ra lưu vào trong list.
- sử dụng phương thức list sort() để sắp xếp lại các từ trong 2 list theo thứ tự alphabet. sau đó đem đi so sánh.
- nếu giống nhau thì in word ban đầu của file `wordlist`.



