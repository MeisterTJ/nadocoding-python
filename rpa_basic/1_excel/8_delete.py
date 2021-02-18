from openpyxl import load_workbook
wb = load_workbook("sample2.xlsx")
ws = wb.active

ws.delete_rows(8)               # 8행 삭제
ws.delete_rows(8, 3)            # 8번째 줄부터 총 3줄 삭제
# ws.delete_cols(2)               # B열 삭제
ws.delete_cols(2, 2)              # B, C 열 삭제

wb.save("sample_delete.xlsx")
