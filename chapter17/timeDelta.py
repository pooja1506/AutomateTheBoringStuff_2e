delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
delta.total_seconds()

dt = datetime.datetime.now()
dt
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st - aboutThirtyYears
oct21st - (2 * aboutThirtyYears)