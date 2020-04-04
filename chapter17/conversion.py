oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
oct21st.strftime('%I:%M %p')
oct21st.strftime("%B of '%y")

datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime.strptime("October of '19", "%B of '%y")
datetime.datetime.strptime("November of '63", "%B of '%y")