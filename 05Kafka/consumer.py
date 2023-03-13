from kafka import KafkaConsumer

# Khởi tạo consumer
consumer = KafkaConsumer(
    'test-topic',  # tên topic cần đăng ký nhận tin nhắn
    bootstrap_servers=['localhost:9092']  # địa chỉ của Kafka broker
)

# Lặp và in các tin nhắn đến từ topic
for message in consumer:
    print(f"{message.topic}: {message.value}")