import openpyxl
"""
pip install openpyxl
"""

def read_excel_file(filepath):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb['Sheet1']
    cell = sheet['A1']
    print(cell.value)

read_excel_file("test_data.xlsx")

def read_excel_file_with_cellname(filepath, cell_name):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb['Sheet1']
    cell = sheet[cell_name]
    print(cell.value)


#read_excel_file_with_cellname("test_data.xlsx", "A2")
#("test_data.xlsx", "G4")

# for i in range(1, 6):
#     read_excel_file_with_cellname("test_data.xlsx", f"A{i}")
