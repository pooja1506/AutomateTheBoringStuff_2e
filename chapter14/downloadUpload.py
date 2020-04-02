import ezsheets
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss.title
ss.downloadAsExcel() # Downloads the spreadsheet as an Excel file.
ss.downloadAsODS() # Downloads the spreadsheet as an OpenOffice file.
ss.downloadAsCSV() # Only downloads the first sheet as a CSV file.
ss.downloadAsTSV() # Only downloads the first sheet as a TSV file.
ss.downloadAsPDF() # Downloads the spreadsheet as a PDF.
ss.downloadAsHTML() # Downloads the spreadsheet as a ZIP of HTML files.

ss.downloadAsExcel('a_different_filename.xlsx')

ss = ezsheets.createSpreadsheet('Delete me') # Create the spreadsheet.
ezsheets.listSpreadsheets() # Confirm that we've created a spreadsheet.
ss.delete() # Delete the spreadsheet.
ezsheets.listSpreadsheets()