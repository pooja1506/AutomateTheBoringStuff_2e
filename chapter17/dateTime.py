import datetime , time
datetime.datetime.now()
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day
dt.hour, dt.minute, dt.second


datetime.datetime.fromtimestamp(1000000)
datetime.datetime.fromtimestamp(time.time())

halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
halloween2019 == oct31_2019
halloween2019 > newyears2020
newyears2020 > halloween2019
newyears2020 != oct31_2019