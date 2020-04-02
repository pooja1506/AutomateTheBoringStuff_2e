import ezsheets
ss = ezsheets.createSpreadsheet('Multiple Sheets')
ss.sheetTitles
ss.createSheet('Spam') # Create a new sheet at the end of the list of
ss.createSheet('Eggs') # Create another new sheet.
ss.sheetTitles
ss.createSheet('Bacon', 0) code># Create a sheet at index 0 in the list of
ss.sheetTitles

ss.sheetTitles
ss[0].delete()      # Delete the sheet at index 0: the "Bacon" sheet.
ss.sheetTitles
ss['Spam'].delete() # Delete the "Spam" sheet.
ss.sheetTitles
sheet = ss['Eggs']  # Assign a variable to the "Eggs" sheet.
sheet.delete()      # Delete the "Eggs" sheet.
ss.sheetTitles
ss[0].clear()       # Clear all the cells on the "Sheet1" sheet.
ss.sheetTitles      # The "Sheet1" sheet is empty but still exists.