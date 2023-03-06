# SQL là gì? MySQL là gì?

- SQl là ngôn ngữ truy vấn dữ liệu trong CSDL quan hệ. 
- MySQL là một hệ quản trị cơ sở dữ liệu được sử dụng rất phổ biến. 

# Các loại dữ liệu phổ biến trong SQL

1. INT: Các số nguyên
2. FLOAT(M, D): Các số thập phân. (M: Độ dài, D: Số thập phân sau dấu phẩy. Ví dụ: 3.14 => M = 3, D = 2)
3. DECIMAL(M, D): Các số thập phân nhưng có độ dài và các chữ số thập phân sau dấu phẩy cố định.
4. CHAR(N): Có độ dài N cố định.
5. VARCHAR(N): Có độ dài lớn nhất là N.
6. ENUM(x,y,z,...): Liệt kê 1 danh sách có thể có, các giá trị sẽ nằm trong danh sách đấy.
7. BOOLEAN: True hoặc False.
8. DATE:YYYY-MM-DD
9. DATETIME: YYYY-MM-DD HH-MM-SS
10. TIME:HHH-MM-SS
11. YEAR: YYYY

# Khóa chính - Khóa ngoại

- Khóa chính(primary key) là 1 trường hoặc một tập hợp các trường dùng để định danh duy nhất cho 1 bản ghi trong 1 bảng. 
- Khóa chính không có giá trị null, giá trị của khóa chính phải là duy nhất trong bảng. Khóa chính cho phép các bảng khác tham chiếu tới bản hiện tại thông qua chính mình.

- Khóa ngoại(foreign key) là 1 trường trong bảng tham chiếu tới khóa chính của bảng khác.

# Các ràng buộc trong 1 trường
1. NOT NULL: Luôn phải có giá trị
2. UNIQUE: Các giá trị không được trùng nhau.
3. PRIMARY KEY: 1 bảng chỉ duy nhất 1 khóa chính
4. FOREIGN KEY: khóa phụ phải liên kết tới 1 khóa chính của bảng khác.
5. CHECK: Kiểm soát được các giá trị có thể được thêm vào column. 
   + vd CHECK(ratings BETWEEN 0 and 100)
6. DEFAULT: Cho phép chèn giá trị mặc định khi thêm.


