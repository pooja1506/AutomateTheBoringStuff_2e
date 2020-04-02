import ezsheets
ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
ss1[0]
ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
ss1[0].copyTo(ss2) # Copy the ss1's Sheet1 to the ss2 spreadsheet.
ss2.sheetTitles    # ss2 now contains a copy of ss1's Sheet1.