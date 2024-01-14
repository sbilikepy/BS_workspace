import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img_file = "image_2.jpg"
no_noise = "no_noise.jpg"
img = Image.open(img_file)
ocr_result = pytesseract.image_to_string(img)
x = ocr_result
print("******RESULT*********")
print(x)
print("____________________")
current_index = ""
tempo_index_result = "qwe"
number_list_str = []
number_list_int = []
for i in range(len(x)):
    if x[i] == "$":
        number_list_str += x[i - 1]
for i in number_list_str:
    number_list_int.append(int(i))
print(number_list_int)
