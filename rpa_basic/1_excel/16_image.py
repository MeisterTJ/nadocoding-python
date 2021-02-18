from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("image1.png")

# C3 위치에 image1.png 파일의 이미지를 삽입
ws.add_image(img, "C3")
wb.save("sample_image.xlsx")
