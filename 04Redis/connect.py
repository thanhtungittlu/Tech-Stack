
import redis

r = redis.Redis(
    host='127.0.0.1',
    port="6379", 
    )

# Thiết lập giá trị cho key 'mykey'
r.set('mykey', 'hello')

# Lấy giá trị của key 'mykey'
value = r.get('mykey')
print(value)  # Kết quả: b'hello'

# Tăng giá trị của key 'counter' lên 1
r.incr('counter')

# Giảm giá trị của key 'counter' xuống 1
r.decr('counter')

# Thêm nội dung vào cuối giá trị của key 'mykey'
r.append('mykey', 'world')

# Lấy độ dài của giá trị của key 'mykey'
length = r.strlen('mykey')
print(length)  # Kết quả: 10


print(type (value))
