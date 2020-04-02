import ezsheets
ss = ezsheets.createSpreadsheet('Multiple Sheets')
ss.sheetTitles
ss.createSheet('Spam') # Create a new sheet at the end of the list of
ss.createSheet('Eggs') # Create another new sheet.
ss.sheetTitles
ss.createSheet('Bacon', 0) code># Create a sheet at index 0 in the list of
ss.sheetTitles