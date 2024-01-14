import sys

my_utf = sys.getdefaultencoding()
print(my_utf)

print(ord("a"))  # узнать код utf
print(chr(int("97")))  # узнать символ по коду
print(chr(int("198")))
s = "hello"
enc_ascii = s.encode("ascii")
enc_utf8 = s.encode("utf8")
enc_utf16 = s.encode("utf16")

print(type(enc_ascii))
print(enc_ascii)
print(enc_utf8)
print(enc_utf16)

print(len(enc_ascii))
print(len(enc_utf8))
print(len(enc_utf16))
print("_________________________")
str_in_bytes = b"hello"
print(str_in_bytes)
str_in_bytes = s.encode("utf8")

str_in_text = "hello"

print(type(str_in_bytes))
print(type(str_in_text))

print("bytes".encode("utf8"))
print("байты".encode("utf8"))
print("_________________________")
print(str_in_bytes[0])
print(str_in_text[0])

ba = bytearray(b"hello")
ba[0] = 87
print(ba)
print("_________________________")

result = str(str_in_bytes)  # бред
print(result)  # бред
print(len(result))  # бред

print("_________________________")
result = str(str_in_bytes, "utf8")
print(result)
print("_________________________")
result = str_in_bytes.decode("utf8")  # функция не отрботает, если не передать таблицу
print(result)
print("___________qwwqwqwq______")
jpeg = [120, 3, 255, 0, 100]
with open(r"C:\Users\BS_HOME\Desktop\my files\Other\валлпаперс\1.jpg", "w+b") as file:
    file.write(bytes(jpeg))
with open(r"C:\Users\BS_HOME\Desktop\my files\Other\валлпаперс\1.jpg", "rb") as file:
    data = file.read()
    for b in data:
        print(int(b))
