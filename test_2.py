import pyotp
import time
# 生成一个密钥（base32 编码）
secret_key = ""

# 使用密钥和时间间隔（默认为 30 秒）创建一个 TOTP 对象
totp = pyotp.TOTP(secret_key)

# 生成当前的 OTP
current_otp = totp.now()
print(f"当前 OTP: {current_otp}")

# 验证 OTP（为演示目的，我们使用刚生成的 OTP）
is_valid = totp.verify(current_otp)
print(f"OTP 是否有效？ {is_valid}")

# 为了演示 OTP 有效性窗口，等待下一个时间间隔
time.sleep(31)

# 再次尝试验证 OTP（由于时间窗口已过，应该无效）
is_valid = totp.verify(current_otp)
print(f"OTP 仍然有效吗？ {is_valid}")
