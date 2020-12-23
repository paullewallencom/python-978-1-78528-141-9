"""Convert a spreadsheet to a shapefile"""
import xlrd
import shapefile

# Open the spreadsheet reader
xls = xlrd.open_workbook("NYC_MUSEUMS_GEO.xls")
sheet = xls.sheet_by_index(0)

# Open the shapefile writer
w = shapefile.Writer(shapefile.POINT)

# Move data from spreadsheet to shapefile
for i in range(sheet.ncols):
  w.field(str(sheet.cell(0,i).value), "C", 40)
for i in range(1, sheet.nrows):
  values = []
  for j in range(sheet.ncols):
    values.append(sheet.cell(i,j).value)
  w.record(*values)
  w.point(float(values[-2]),float(values[-1]))
w.save("NYC_MUSEUMS_XLS2SHP")
