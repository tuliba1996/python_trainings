#h1.Mục lục
[1.Tìm hiểu cú pháp: if else, for else, while](#1)
    [1.1 If...Else](#1.1)
    [1.2 For...Else](1.2)
    [](#1.3)
[2.Tìm hiểu các hàm, câu lệnh: range(), break, continue, pass](#2)
    [2.1 Range()](#2.1)
    [2.2 Break](#2.2)
    [2.3 Continue](#2.3)
    [2.4 Pass](#2.4)
[3.Cách khai báo hàm? Đặt giá trị mặc định cho tham số truyền vào? Viết ví dụ minh họa](#3)
[4.Tìm hiểu biến toàn cục `__name__` . Và cú pháp `__name__ = '__main__'`](#4)
[5.Đọc thêm về cú pháp Lambda. Ví dụ minh họa](#5)

<a name="1"></a>

#h1 1.Tìm hiểu cú pháp: if else, for else, while

<a name="1.1"></a>

#h3 1.1 If...Else
Một lệnh **else** có thể được sử dụng kết hợp với lệnh **if**. Một lệnh **else** chứa khối code mà thực thi nếu biểu thức điều kiện trong lệnh **if** được ước lượng là 0 hoặc một giá trị *false*. Lệnh **else** là lệnh tùy ý và chỉ có duy nhất một lệnh else sau lệnh **if**.

    if bieu_thuc:
        cac_lenh
    else:
        cac_lenh

**Ví dụ**

    if a>b:
        print 'tao thich m'
    else: 
        print 'tao chich m'

<a name="1.2"></a>

#h3 1.2 For...Else
`Python` cho phép bạn có một lệnh **else** để liên hợp với một lệnh vòng lặp. Với vòng lặp **for**, lệnh **else** được thực thi khi vòng lặp đã lặp qua hết các phần tử trong list.

    a= [1,2,3,4,5,6,7]
    for i in a
        if i<4
        d=d+1
    else:
        print "cac so nho hon 4 la",d

<a name="1.3"></a>

#h3 1.3 While
Vòng lặp **While** sẽ thực hiện lặp đi lặp lại khối lệnh trong nó khi điều kiện của nó là **True**. Khi điều kiện là **False** thì sẽ thoát ra khỏi vòng lặp.

    while (biểu_thức_điều_kiện):
        #khối lệnh

**Ví dụ**

    i = 10
    S = 1
    while (i != 0):
        S *=i
        i -=1
    print "Tong day so la",S

<a name="2"></a>

#h1 2.Tìm hiểu các hàm, câu lệnh: range(), break, continue, pass

<a name="2.1"></a>

#h3 2.1 Range()
Range() để tạo ra một list kiểu int. 


    a = Range(10)

Kết quả

    a = [0,1,2,3,4,5,6,7,8,9] 

Cú pháp range(start,stop,step)
    Trong đó:
        start: số phần tử của list.
        stop: số bắt đầu của dãy số.
        step: độ sai lệch của mỗi phần tử trong list.
**Ví dụ**

    a = range(2,10,2)

Kết quả
    
    a = [2,4,6,8]

<a name="2.2"></a>

#h3 2.2 Break
Lệnh **break** trong `Python` là giống như lệnh **break** trong `C`. Lệnh này kết thúc vòng lặp hiện tại và truyền điều khiển tới cuối vòng lặp. Lệnh **break** này có thể được sử dụng trong vòng lặp **while** và vòng lặp **for**. Nếu bạn đang sử dụng lồng vòng lặp, thì lệnh **break** kết thúc sự thực thi của vòng lặp bên trong và bắt đầu thực thi dòng code tiếp theo của khối.

    #Tim so le dau tien
    for i in range(20):
        if i % 2 != 0:
            print i,'la so le dau tien'
            break

<a name="2.3"></a>

#h3 2.3 Continue
Lệnh **continue** trả về điều khiển tới phần ban đầu của vòng lặp. Lệnh này bỏ qua lần lặp hiện tại và bắt buộc lần lặp tiếp theo của vòng lặp diễn ra. Lệnh **continue** có thể được sử dụng trong vòng lặp **while** hoặc vòng lặp **for**.

**Ví dụ**

    for letter in 'DSau dep trai':    
        if letter == 'D':
            continue
        print 'Chu cai hien tai :', letter
   
Kết quả

    Chu cai hien tai : S
    Chu cai hien tai : a
    Chu cai hien tai : u
    Chu cai hien tai :  
    Chu cai hien tai : d
    Chu cai hien tai : e
    Chu cai hien tai : p
    Chu cai hien tai :  
    Chu cai hien tai : t
    Chu cai hien tai : r
    Chu cai hien tai : a
    Chu cai hien tai : i


<a name="2.4"></a>

#h3 2.4 Pass
Lệnh **pass**, giống như tên của nó, được sử dụng khi một lệnh là cần thiết theo cú pháp nhưng bạn không muốn bất cứ lệnh hoặc khối code nào được thực thi. Lệnh **pass** là một hoạt động **null** và không có gì xảy ra khi nó thực thi.

**Ví dụ**
    
    for letter in 'Sau Ddep trai':    
        if letter == 'D':
            pass
            print "SAU RAT DEP TRAI"
        print 'Chu cai hien tai :', letter

Kết quả

    chu cai hien tai S
    chu cai hien tai a
    chu cai hien tai u
    chu cai hien tai  
    SAU RAT DEP TRAI
    chu cai hien tai D
    chu cai hien tai d
    chu cai hien tai e
    chu cai hien tai p
    chu cai hien tai  
    chu cai hien tai t
    chu cai hien tai r
    chu cai hien tai a
    chu cai hien tai i


 <a name="3"></a>

#h1 3.Cách khai báo hàm? Đặt giá trị mặc định cho tham số truyền vào? Viết ví dụ minh họa
**Cách khai báo hàm**

    def ten_ham( cac_tham_so ):
        #Khoi_lenh
        return [bieu_thuc]
    

**Ví dụ**

    def Checkhandsome (string):
        print string
        return

**Gọi hàm**

    ten_ham(tham so)

**Ví dụ**
    
    checkhandsome("SAU DEP TRAI")

Kết quả 
    
    SAU DEP TRAI

<a name="4"></a>

#h1 4.Tìm hiểu biến toàn cục `__name__` . Và cú pháp `__name__ = '__main__'`



<a name="5"></a>

#h1 5.Đọc thêm về cú pháp Lambda. Ví dụ minh họa
Hàm nặc danh (hàm vô danh), hiểu theo cách đơn giản, là hàm không có tên và chúng không được khai báo theo cách chính thức bởi từ khóa **def**. Để khai báo hàm này, bạn sử dụng từ khóa **lambda**. **Lambda** nhận bất kỳ lượng tham số nào và chỉ trả về một giá trị trong dạng một biểu thức đã được ước lượng. Bạn không thể gọi trực tiếp gọi hàm nặc danh để in bởi vì labda cần một biểu thức. Ngoài ra, các hàm **lambda** có **namespace** cục bộ của chúng.

Cú pháp

    lambda [arg1 [,arg2,.....argn]]:bieu_thuc

**Ví dụ**

    Add = lambda x: x+x
    print "Gia tri cua x la: ", Add(10)

Kết quả 
    
    Gia tri cua x la: 20




