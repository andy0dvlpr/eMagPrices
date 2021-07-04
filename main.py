# Utility to get the price of a specific product from Romanian e-commerce
# website eMag and put it in an Excel spreadsheet.
# Modify the program to fit your necessities; you can use Task Scheduler
# to make the script run automatically.

import getprice
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime

try:
    rb = xlrd.open_workbook('prices.xls')
except FileNotFoundError:
    print("You must make a 'prices.xls' file!")
r_sheet = rb.sheet_by_index(0)
r = r_sheet.nrows
wb = copy(rb) 
sheet = wb.get_sheet(0) 
sheet.write(r, 0, getprice.output)
sheet.write(r, 1, datetime.now(), xlwt.easyxf(num_format_str='D-MMM-YY'))
wb.save('prices.xls')