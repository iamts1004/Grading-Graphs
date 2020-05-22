import matplotlib.pyplot as graph   # for making graphs using python  (installed using pip install matplotlib.)
import xlrd     # for reading excel worksheets using python.   (installed using pip install xlrd.)

marks = ('C:\Desktop Icons\PESU\python assignment\studentdataset.xls')     # giving file location.
wb = xlrd.open_workbook(marks)    # opening workbook file.
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)   # for row 0 and column 0.

# for Mid-term marks
x1=[]; y1=[]
for i in range(4,30,1):
    value = float(sheet.cell_value(i,9))*100
    y1.append(value)
for j in range(1, 27, 1):
    x1.append(j)
# plotting the Mid-term marks points
graph.plot(x1, y1, label="Mid-term marks", marker='o', markerfacecolor='blue', markersize=5)

# for Final term marks
x2=[]; y2=[]
for i in range(4, 30, 1):
    value = float(sheet.cell_value(i,11))*100
    y2.append(value)
for j in range(1, 27, 1):
    x2.append(j)
# plotting the Final term marks points
graph.plot(x2, y2, label="Final term marks", marker='o', markerfacecolor='orange', markersize=5)

# naming the x axis
graph.xlabel('Students')
# naming the y axis
graph.ylabel('Percentage Marks')
# giving a title to my graph
graph.title('Comparison between Mid-term and Final term marks')
# show a legend on the plot
graph.legend()
# function to show the plot
graph.show()