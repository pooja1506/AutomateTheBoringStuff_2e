import ezsheets
ezsheets.convertAddress('A2') # Converts addresses...

ezsheets.convertAddress(1, 2) # ...and converts them back, too.

ezsheets.getColumnLetterOf(2)

ezsheets.getColumnNumberOf('B')
ezsheets.getColumnLetterOf(999)
ezsheets.getColumnNumberOf('ZZZ')