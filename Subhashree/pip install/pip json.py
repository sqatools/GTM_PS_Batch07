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
