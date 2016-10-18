#Mục lục

[1.Git là gì?](#Git) 

[2.Cài đặt Git trên máy tính.](#setup)

[3.Cách sử dụng Git trên terminal.](#user)

<a name="Git"></a>

#1.Git là gì?	

`Git` là một trong những Hệ thống Quản lý Phiên bản Phân tán, vốn được phát triển nhằm quản lý mã nguồn (source code) của **Linux**. Trên `Git`, ta có thể lưu trạng thái của file dưới dạng lịch sử cập nhật. Vì thế, có thể đưa file đã chỉnh sửa một lần về trạng thái cũ hay có thể biết được file đã được chỉnh sửa chỗ nào.

<a name="setup"></a>

#2.Cài đặt Git trên máy tính.

Vào trang http://rogerdudler.github.io/git-guide/ để tải `Git` với phiên bản phù hợp.

![](Image/setup1)

Sau khi tải về xong mở lên ta được:

![]()

Click phải vào icon `git-1.8.4.2-intel-universal-snow-leopard.pkg` chọn **Open**
Như vậy là đã cài đặt thành công `Git`.

<a name="user"></a>

#3.Cách sử dụng Git trên terminal.

**Clone Github về máy tính**

Vào trang `Github` cá nhân, nhấn vào `Clone or download` -> **Copy** *link*.

Sau đó mở `Terminal` lên và nhấn vào dòng lệnh:
    
    Git clone https://github.com/tuliba1996/python_trainings.git

![]()

Xong, máy của bạn và Github đã được đồng bộ.

**Add và commit**

Thêm file vào **index**

    git add <file>.. 
    git add *       // để thêm nhiều tất cả các file

![]()

Commit file

    git commit -m "<commit>"

![]()

**Push file lên Github**
    
    git push origin master

![]()















