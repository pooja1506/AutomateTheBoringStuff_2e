import ezsheets
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss.title         # The title of the spreadsheet.
ss.title = 'Class Data' # Change the title.
ss.spreadsheetId # The unique ID (this is a read-only attribute).
ss.url           # The original URL (this is a read-only attribute).
ss.sheetTitles     # The titles of all the Sheet objects
ss.sheets          # The Sheet objects in this Spreadsheet, in order.
ss[0]              # The first Sheet object in this Spreadsheet.
ss['Students']     # Sheets can also be accessed by title.
>>> del ss[0]          # Delete the first Sheet object in this Spreadsheet.
>>> ss.sheetTitles     # The "Students" Sheet object has been deleted: