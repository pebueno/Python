def weeklyPayment(hours, hour_value):
    hours = float(hours)
    fee = float(hour_value)
    if hours <= 40:
        salary=hours*fee
    else:
        extra_hour = hours - 40
        salary = 40*fee+(extra_hour*(1.3*fee))
    return salary

def monthlyPayment(hours, hourValue):
    monthlyPayment = weeklyPayment(hours, hourValue)*4
    return monthlyPayment

print(monthlyPayment(50, 50))
