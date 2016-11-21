#Challenge 6
Đầu tiên khi chúng ta sẽ thấy được tấm hình chụp cái quần jean. Nhìn tấm hình chả thấy mẹ gì. Thôi thì thử vận may mở source lên xem coi có quái gì không.

![](http://imgur.com/cC0BhU4)

Mở source html lên thì đọc comment nó đánh lạc hướng mình kích dô Paypal điền một cái giá gì đó. làm thấy bà cũng méo được.

![](http://imgur.com/ymxyMme)

Ô hay là nhìn lại source một hồi thì thấy bên trên có để chữ `<-- zip -->` thế là thử đổi đường link trên url thành:

    http://www.pythonchallenge.com/pc/def/channel.zip

Thế là nó tải 1 file `channel.zip` về máy. Xong cũng chả biết làm gì với nó, thử giải nén ra xem thì trong đó có 1 đống file **txt** cuối cùng thì thấy file `readme.txt` thử mở file đó lên và thấy:

![](http://imgur.com/GC2mtv5)

Chúng ta sẽ sử dụng thư viện zipfile để giải challenge này.
Để đọc file trong file zip ta sử dụng method:
    
    ZipFile.read('file_name')

Nhìn thì nó có phần tương tự challenge trước. Bắt đầu mở file `90052.txt` trong file đó sẽ có chứa con số, đó là tên file tiếp theo ta cần mở. cứ như vậy mở lần lượt thì sẽ cho ra kết quả.

![](http://imgur.com/2CPx5pQ)

Kết quả đọc file cuối cùng là: **Collect the comments** (thu thập comment). Đây vẫn chưa phải là kết quả cuối cùng.
Để thu thập comments trong các file txt trong file zip ta sử dụng:

    Zipfile.getinfo("file_name").comment

ta được kết quả: **Hockey**.

![](http://imgur.com/CY6crFY)

Nhìn có vẻ như là kết quả cuối cùng, thử lên browser gõ thử vào url:
    
    http://www.pythonchallenge.com/pc/def/hockey.html

Kết quả là xuất hiện thêm 1 dòng chữ: **it's in the air. look at the letters.**

![](http://imgur.com/AK6EtMz)

Gợi ý là *nó ở trong không khí, hãy nhìn vào nhưng chữ cái*. Bây giờ chúng ta xem lại ảnh **hockey** lúc nảy.

![](http://imgur.com/CY6crFY)

Kết quả là: **OXYGEN**.

**Đó là kết quả cuối cùng**






