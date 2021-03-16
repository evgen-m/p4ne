#!/usr/local/bin/python3

from matplotlib import pyplot
from openpyxl import load_workbook

wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']

col_a=sheet['A'][1:]
col_c=sheet['C'][1:]
col_d=sheet['D'][1:]

def getvalue(x): return x.value

val_a=map(getvalue, col_a)
val_c=map(getvalue, col_c)
val_d=map(getvalue, col_d)

list_a=list(val_a)
list_c=list(val_c)
list_d=list(val_d)

pyplot.plot(list_a, list_c, label="Temp")
pyplot.plot(list_a, list_d, label="Sun Activity")

pyplot.legend()
pyplot.show()
