# Dùng gói python alpine có sẵn để build ứng dụng
FROM python:3.8-alpine

# Copy nội dụng của file requirement vào container
COPY ./requirements.txt /app/requirements.txt

# Thư mục gốc của Dockerfile
WORKDIR /app

# Chạy các gói cài đặt trong file requirement
RUN pip install -r requirements.txt

# Cho phép sao chép nội dung của tất cả các file vào trong thư mục app của ứng dụng
COPY . /app



EXPOSE 8080
# Lệnh chạy ứng dụng trong vùng chứa
ENTRYPOINT [ "python" ]

# Nối thêm danh sách lệnh để chạy trong ứng dụng: (ENTRYPOINT + CMD = python + view.py)
CMD ["view.py" ]




# Cách build ứng dụng
# docker image build -t flask_docker .


#Lệnh để chạy ứng dụng
# docker run -p 5000:5000 -d flask_docker


# Các bước deploy lên docker hub
# B1: Tạo 1 repo trên docker hub
# B2: docker login
# B3: docker tag flask_docker <your-docker-hub-username>/flask-docker
# B4: docker push <your-docker-hub-username>/flask-docker