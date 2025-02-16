def read_excel_file(filepath):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb['Excel Sheet.xlsx']
    cell = sheet['A1']
    print(cell.value)

