# 엑셀 파일 생성
from openpyxl import Workbook
wb = Workbook()     # 새 워크북 생성
ws = wb.active      # 현재 활성화된 sheet를 가져온다.
ws.title = "NadoSheet"  # sheet 의 이름을 변경
wb.save("sample.xlsx")  # 엑셀로 저장
wb.close()