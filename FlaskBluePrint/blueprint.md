# Flask Blueprint là gì ?

- Flask là KHÔNG CỐ ĐỊNH bất cứ một CẤU TRÚC cụ thể nào cho dự án, có thế tùy chỉnh cấu trúc tùy theo ý muốn của mình.
- Tuy nhiên, Flask cung cấp cho người dùng Blueprint(Bản thiết kế) để có thể làm việc này. Blueprint là một tập hợp các bản thiết kế để chia Mã thành các module riêng lẻ, chức năng khác nhau. Có thể tưởng tượng như 1 blueprint là 1 module trong hàng loạt module của 1 ứng dụng.
- 1 BLUEPRINT có thể bao gồm NHIỀU THÀNH PHẦN: Định tuyến(route), hàm hiển thị, form, template, file tĩnh,...Nếu tạo ra một blueprint trong 1 ứng dụng, nghĩa là mình đã đóng gói các yếu tố CẦN THIẾT LIÊN QUAN đến một chức năng nhất định trong ứng dụng.
- 1 blueprint hoạt động như là 1 ứng dụng nhưng được khai báo trong 1 ứng dụng.

#  Tác dụng của Blueprint:

- Cấu trúc thư mục dễ dàng hơn.
- Dễ dàng bảo trì và phát triển code.
