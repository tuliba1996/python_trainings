#Mục lục

[1.Tìm hiểu về Tuples, sets, dict](#1)
[1.1 Tuples](#1.1)
[1.2 Sets](#1.2)
[1.3 Ditionary](#1.3)
[2.Urllib2.open()](#2)
[3.Urllib2.Request()](#3)

<a name="1"></a>

#1.Tìm hiểu về Tuples, sets, dict

<a name="1.1"></a>

###1.1 Tuples

Một **tuple** là một dãy các đối tượng không thay đổi (immutable) trong `Python`, vì thế **tuple** không thể bị thay đổi. Các **tuple** cũng là các dãy giống như **List**.

Không giống **List** mà sử dụng các dấu ngoặc vuông, thì **tuple** sử dụng các dấu ngoặc đơn. Các đối tượng trong **tuple** được phân biệt bởi dấu phảy và được bao quanh bởi dấu ngoặc đơn (). Giống như chỉ mục của chuỗi, chỉ mục của tuple bắt đầu từ 0.

    a = ('a','b','c','d','e')
    b = (1,'a',2,'b')

**Ghi chú**: Nếu các dấu ngoặc đơn không được cung cấp với một dãy, thì nó được coi như là tuple.

    a = 1.2,1.3,1.4,1.5

Để truy cập các giá trị trong **tuple**, bạn sử dụng cách tương tự như khi truy cập các phần tử trong **List**.
    
    a = ('a','b','c','d','e')
    print "a[0]:", a[0]

Kết quả

    a[0]: a

<a name="1.2"></a>

###1.2 Sets
Một tập hợp là một nhóm các phần tử không trùng lặp.

    a= ['b','r','y','b','f','y','h','q','q','z','r']
    set(a)

Kết quả

    set(['b', 'f', 'h', 'q', 'r', 'y', 'z'])

<a name="1.3"></a>

###1.3 Dictionary
**Dictionary** trong `Python` là một tập hợp các cặp key và value không có thứ tự. Nó là một container mà chứa dữ liệu, được bao quanh bởi các dấu ngoặc móc đơn {}. Mỗi cặp key-value được xem như là một item. Key mà đã truyền cho item đó phải là duy nhất, trong khi đó value có thể là bất kỳ kiểu giá trị nào. Key phải là một kiểu dữ liệu không thay đổi (immutable) như chuỗi, số hoặc tuple.

Key và value được phân biệt riêng rẽ bởi một dấu hai chấm (:). Các item phân biệt nhau bởi một dấu phảy (,). Các item khác nhau được bao quanh bên trong một cặp dấu ngoặc móc đơn tạo nên một **Dictionary** trong `Python`.

    dict = {'di':100,'la':200,'ga':300}

**Các thuộc tính của key trong Dictionary**
- không được phép có nhiều hơn một key. nếu có nhiều key giống nhau trong một **Dictionary** thì key cuối cùng sẽ được truy xuất.
- Key phải là immutable. Nghĩa là bạn chỉ có thể sử dụng chuỗi, số hoặc tuple làm key của **Dictionary**.

**Truy cập các giá trị trong Dictionary**

    dict = {'di':100,'la':200,'ga':300}
    print "ket qua la: ", dict['di']

Kết quả 
    
    ket qua la: 100

**Cập nhật Dictionary**

    dict = {'monkey':100,'duck':200,'chicken':300}
    dict['fish']= 50

Kết quả

    dict = {fish':50,'monkey':100,'duck':200,'chicken':300}

**Xóa phần tử từ Dictionary**

Cú pháp:
    
    del dict_name[key]

Ví dụ
    
    dict = {fish':50,'monkey':100,'duck':200,'chicken':300}
    del dict['duck']

Kết quả

    dict = {fish':50,'monkey':100,'chicken':300}

<a name="2"></a>

#2.Urllib2.open()


<a name="3"></a>

#3.Urllib2.Request()
