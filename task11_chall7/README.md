#Mục lục

[1.Hàm](#1)

[2.Phương thức](#2)

[3.Thuộc tính](#3)

<a name="1"></a>

#1.Hàm
###1.1 New
Tạo mới một hình ảnh với chế độ và kích thước định sẵn.

    Image.new(mode, size, color)

###1.2 Open
Mở hình ảnh

    Image.open(file, mode) 


###1.3 Blend
Tạo một ảnh mới bằng cách ghép 2 ảnh lại. 2 ảnh phải có cùng kích thước và chế độ.

    Image.blend(image1,image2,alpha)

###1.4 Composite
Tạo một ảnh mới bằng cách ghép 2 ảnh lại, sử dụng các điểm ảnh.

    Image.composite(image1, image2, mask) 

###1.5 Evel

    Image.eval(image, function) 

###1.6 Frombuffer
Tạo ra một bộ nhớ hình ảnh từ dữ liệu điểm ảnh trong một chuỗi hoặc đệm đối tượng.

    Image.frombuffer(mode, size, data)

###1.7 Fromstring
Tạo ra một bộ nhớ hình ảnh từ điểm ảnh dưới dạng chuỗi.

    Image.fromstring(mode, size, data) 

###1.8 Merge

    Image.merge(mode, bands) 

<a name="2"></a>
#2.Phương thức

###2.1 Convert
chuyển đổi ảnh sang chế độ khác.

    im.convert(mode)

###2.2 Copy
Sao chép hình ảnh.

    im.copy()

###2.3 Crop
Cắt hình ảnh.

    im.crop(box)

###2.4 Draft
Cấu hình bộ nạp tập tin ảnh sao cho nó trả về một phiên bản của hình ảnh đó càng sát càng tốt phù hợp với chế độ và kích thước nhất định

    im.draft(mode, size)

###2.5 Filter
Trả về bản sao hình ảnh đã được lọc.

    im.filter(filter)

###2.6 Fromstring

    im.fromstring(data, decoder, parameters)


###2.7 Getbands
Trả về một bộ chứa tên của từng dãy.
    
    im.getbands()

###2.8 Getbox
Tính toán khung giới hạn của các vùng khác không trong các hình ảnh

    im.getbox()

###2.9 Getcolor

    im.getcolor()


###2.10 Getdata
Trả về các nội dung của một hình ảnh như một đối tượng chuỗi có chứa các giá trị pixel.
    
    im.getdata()

###2.10 Getpixel
Trả về pixel tại một vị trí nhất định.

    im.getpixel((x,y))

<a naem="3"></a>

#3.Thuộc tính

###3.1 Format
Định dạng tập tin nguồn.

    im.format

###3.2 Mode
Chế độ của hình ảnh.

    im.mode

###3.2 Size
Kích thước của hình ảnh. (chiều rộng, chiều ngang)

    im.size

###3.3 Palette
Bảng màu

    im.palette

###3.4 Info

    im.info














