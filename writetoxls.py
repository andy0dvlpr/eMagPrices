import emagpricesget
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime

rb = xlrd.open_workbook('prices.xls')
r_sheet = rb.sheet_by_index(0)
r = r_sheet.nrows
wb = copy(rb) 
sheet = wb.get_sheet(0) 
sheet.write(r, 0, emagpricesget.output)
sheet.write(r, 1, datetime.now(), xlwt.easyxf(num_format_str='D-MMM-YY'))
wb.save('prices.xls')