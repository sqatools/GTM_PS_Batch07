import  openpyxl

def readexel_file(filepath):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb['Sheet1']
    cell = sheet['A2']
    print(cell.value)

readexel_file("testdata.xlsx")


def readexcel1_file(filepath,cell_name):
    wb = openpyxl.load_workbook(filepath,cell_name)
    sheet =wb['Sheet1']
    cell = sheet[cell_name]
    print(cell.value)

readexcel1_file("Testdata.xlsx", "A3")


read_excel_file_with_cellname("test_data.xlsx", "A2")
("test_data.xlsx", "G4")

for i in range(1, 6):
    read_excel_file_with_cellname("test_data.xlsx", f"A{i}")
