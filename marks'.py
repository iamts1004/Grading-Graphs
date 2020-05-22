import xlrd     # for reading excel worksheets using python.   (installed using pip install xlrd.)

marks = ('C:\Desktop Icons\PESU\python assignment\studentdataset.xls')     # giving file location.
wb = xlrd.open_workbook(marks)    # opening workbook file.
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)   # for row 0 and column 0.
print(sheet.row_values(2))   # printing column heading

for j in range(3, 12, 2):   # iterating through columns.
    m = 100.0
    for i in range(4, 30, 1):   # iterating through rows.
        value = sheet.cell_value(i,j)
        if(value ==0.0):     # those students which do not appear for examination.
            continue
        elif value < m:      # for finding minimum marks in each assignment.
            m = value
            a = i; b = j
    print(sheet.row_values(a))  # printing row details with minimum marks in each assignment.