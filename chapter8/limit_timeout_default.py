import pyinputplus as pyip
response = pyip.inputNum(limit=2)
response1 = pyip.inputNum(timeout=5)
response2 = pyip.inputNum(limit=2,default='NA')