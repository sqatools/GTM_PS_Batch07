import openpyxl

def read_excel_file(filepath):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb['Sheet1']
    cell = sheet['A1']
    print(cell.value)


read_excel_file("test_data.xlsx")