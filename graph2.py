import matplotlib.pyplot as graph   # for making graphs using python  (installed using pip install matplotlib.)
import xlrd     # for reading excel worksheets using python.   (installed using pip install xlrd.)

marks = ('C:\Desktop Icons\PESU\python assignment\studentdataset.xls')     # giving file location.
wb = xlrd.open_workbook(marks)    # opening workbook file.
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)   # for row 0 and column 0.

x= []; y= []
# y-coordinates of sides of bars
for i in range(4,30,1):
    value = float(sheet.cell_value(i,9))*100
    y.append(value)
# x-coordinates of sides of bars
for j in range(4,30,1):
    value = sheet.cell_value(j,0)
    x.append(value)

# labelling x-axis with names of students
label = []
for i in range(4,30,1):
    value = sheet.cell_value(i,0)
    label.append(value)

# plotting a bar chart
x_pos = range(len(x))
graph.bar(x, y, tick_label=label, width=0.3, color=['yellow', 'purple'])
# Rotation of the bars names
graph.xticks(x_pos, x, rotation=90)

# naming the x-axis
graph.xlabel('Student name')
# naming the y-axis
graph.ylabel('Mid-term marks')
# plot title
graph.title('Comparison of students marks in Mid-terms.')
# function to show the plot
graph.show()