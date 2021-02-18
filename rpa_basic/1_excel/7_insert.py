from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8)                       # 8행에서 삽입을 한 것과 같은 효과를 준다.
ws.insert_rows(8, 5)                      # 8번째 행 위치에 5줄을 추가
ws.insert_cols(2, 3)                      # B번째 열에 3열 추가
wb.save("sample_insert.xlsx")
