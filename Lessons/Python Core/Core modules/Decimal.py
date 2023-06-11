import decimal

print(0.1 + 0.1 + 0.1)

x = 0.1 + 0.1 + 0.1

print(x)
y = 0.30000000000000004
print(x == y)

custom_dec_num_name = decimal.Decimal("0.1")
print(type(custom_dec_num_name))
x = custom_dec_num_name * 3
print(x)
print(x == 0.3)
asd = float(0.1)
dsa = decimal.Decimal("0.1")
import sys

print("_")
print(sys.getsizeof(asd))  # 24 bytes *8 = bit
print(sys.getsizeof(dsa))  # 24 bytes *8 = bit
