import ezsheets
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss
Spreadsheet(spreadsheetId='1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss.title

ss = ezsheets.createSpreadsheet('Title of My New Spreadsheet')
ss.title

ss = ezsheets.upload('my_spreadsheet.xlsx')
ss.title