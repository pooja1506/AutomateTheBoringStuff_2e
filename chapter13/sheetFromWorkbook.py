import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
wb.sheetnames # The workbook's sheets' names.
sheet = wb['Sheet3'] # Get a sheet from the workbook.
sheet
type(sheet)
sheet.title # Get the sheet's title as a string.
anotherSheet = wb.active # Get the active sheet.
anotherSheet