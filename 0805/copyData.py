import openpyxl
wb = openpyxl.load_workbook("0805.xlsx")
ws_copy = wb.copy_worksheet(wb["hello"])

wb.save("0805.xlsx")