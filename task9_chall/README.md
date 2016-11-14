#Mục lục

[1.Challenge 4](#1)

[2.Challenge 5](#2)

[3.Pickle](#3)

<a name="1" =""></a>

#1.Challenge 4
Dễ thấy khi show page source chúng ta sẽ thấy được một gợi ý nhỏ `urllib may help`, cho ta biết Lib Urllib2 sẽ giúp đc cho chúng ta.

![](http://i.imgur.com/SevSQ7L.png)

Chúng ta sẽ thấy một link: `linkedlist.php?nothing=12345` khi click vào đó, nó sẽ xuất hiện 1 dòng chữ: **and the next nothing is 44827**.
Để ý thấy rằng *linkedlist.php?nothing=**12345*** khi link có số **12345** thì sẽ cho ta một số mới, **44827**.
Như vậy bài này có nghĩa là lấy số đưa vào link, nó sẽ cho ta một số mới, quá trình này được lập đi lập lại khoảng 400 lần (có thể ít hoặc nhiều hơn), cho đến khi cho ta kết quả cuối cùng.

    import urllib2
    import re
    ul = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    pat = re.compile("and the next nothing is (\d+)")
    number= str(16044/2)
    while True :
        data = urllib2.urlopen(ul % number).read()
        print data
        reg = pat.search(data)
        if reg == None:
            break
        number = reg.group(1)


<a name="2" =""></a>


#2.Challenge 5
Thật sự thì chall này khó trời đánh, nói chung khi chúng ta show page source lên thì nhìn kỹ sẽ thấy một file `banner.p` nhưng khi click vào mở nó ra thì thấy chỉ toàn chữ và ký hiệu đặc biệt. 

![](http://i.imgur.com/8xHEAHe.png)

Theo kinh nghiệm thì chắc chắn chúng ta phải làm một cái gì đó với file đó để tìm ra key. Nhưng nhìn mãi chả hiểu gì.
Thế là có một sự gợi ý đó là sử dụng Lib `Pickle`. Đọc thì cũng chả hiểu gì, nhưng biết có Method **dump** và **load**. Thử sử dụng lần lượt 2 cái đó. may là **load** cho ta kết quả một cái list 2 chiều.
Sau nhiều lần suy nghĩ thì cũng hiểu list 2 chiều đó, nó nghĩa là kí tự đầu sẽ được in 1 số lần giá trị thứ 2. ví dụ [(" ",95)], có nghĩa là in ký tự space 95 lần. sau đó chúng ta được kết quả.

    import pickle
    import urllib2
    f = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p",'rb')
    result = ''
    pick = pickle.load(f)
    for i in pick:  
        for j,k in i:
            result = result + j*k
    print result


![](http://i.imgur.com/uriFDKE.png)

<a name="3" =""></a>


#3.Pickle
Các chuỗi có thể được ghi hoặc đọc dễ dàng từ một tập tin. Các số cần một ít cố gắng hơn, vì phương thức read() chỉ trả về chuỗi, và cần được truyền vào một hàm như int(), nó sẽ nhận một chuỗi như '123' và trả về giá trị số 123 của nó. Tuy nhiên, khi bạn muốn lưu các kiểu dữ liệu phức tạp hơn như danh sách, từ điển, hoặc các đối tượng, việc này trở nên rắc rối hơn nhiều.

Thay vì để người dùng luôn viết và gỡ rối mã để lưu các kiểu dữ liệu phức tạp, Python cung cấp một mô-đun chuẩn gọi là pickle. Đây là một mô-đun tuyệt diệu có thể nhận hầu hết mọi đối tượng Python (ngay cả một vài dạng mã Python!), và chuyển nó thành một chuỗi; quá trình này được gọi là giầm (pickling). Tạo lại đối tượng từ một chuỗi được gọi là vớt (unpickling). Giữa việc giầm và vớt, biểu diễn dạng chuỗi của đối tượng có thể được lưu vào tập tin, hoặc gửi qua mạng đến một máy ở xa.

Có 2 phương thức trong Lib `Pickle` cần chú ý:

**pickle.dump(obj, file, protocol=None, *, fix_imports=True)**

Hàm này có thể hiểu như là một hàm write() nhưng không bị gò bó mà có thể sử dụng với nhiều đối tượng obj khác nhau.

**pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict")**

Hàm này có thể hiểu như là một hàm read() có 2 cách đọc là đọc theo errors còn nếu để trống thì sẽ đọng theo line-từng dòng

Thật sự thì mình cũng chưa hiểu thư viện này cho lắm!!!



