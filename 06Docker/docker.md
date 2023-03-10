# Docker là gì ?
- Docker là nền tảng phần mềm cho phép dựng, kiểm thử và triển khai ứng dụng một cách nhanh chóng. 
- Docker đóng gói phần mềm vào các đơn vị tiêu chuẩn hóa được gọi là container có mọi thứ mà phần mềm cần để chạy, trong đó có thư viện, công cụ hệ thống, mã và thời gian chạy. 
- Nhanh chóng triển khai và thay đổi quy mô ứng dụng vào bất kỳ môi trường nào và biết chắc rằng mã của sẽ chạy được.


# Container Docker ?
- Là 1 phương tiện để đóng gói ứng dụng, chứa tất cả những gì cần thiết để chạy 1 ứng dụng bao gồm các thư viện, hệ điều hành, tệp tin,...

# Docker image?
- Là tập hợp các file của hệ thống để tạo ra 1 container docker, nó bao gồm một hệ điều hành, mã nguồn ứng dụng, và các tài nguyên khác.
- Docker image được tạo ra bởi 1 tệp tên là Dockerfile, chứa những chỉ thị để xây dựng một Docker image.
 
- Sự khác biệt giữa RUN, CMD, ENTRYPOINT:
    + RUN: Sử dụng khi tạo một image mới, khi cài 1 package mới.
        vd: RUN apt-get update && apt-get install -y python3-pip 



    + CMD: Chỉ thị CMD được sử dụng để chỉ định lệnh mặc định mà container sẽ chạy khi nó được khởi động. Ví dụ, để chỉ định container chạy ứng dụng Python Flask trên cổng 5000, bạn có thể sử dụng chỉ thị CMD như sau:
        vd: CMD ["python", "app.py"]



    + ENTRYPOINT được sử dụng để chỉ định chương trình hoặc tệp thực thi sẽ được chạy khi container được khởi động và cho phép truyền tham số bổ sung vào lệnh này.

- Sự khác biệt giữa COPY và ADD:
    + Chức năng chung: Sử dụng để sao chép các tệp từ một vị trí trong host vào image Docker
    + COPY: COPY có thể chạy nhanh hơn ADD, bởi vì COPY chỉ sao chép các tệp đã được xác định trước
    + ADD: Có thêm các tính năng bổ sung ví dụ như tự giải nén tệp, sao chép tệp từ URL.

        Ví dụ, để sao chép tệp index.html từ thư mục hiện tại vào thư mục /var/www/html trong image Docker, bạn có thể sử dụng chỉ thị ADD như sau: ADD index.html /var/www/html/

- EXPOSE