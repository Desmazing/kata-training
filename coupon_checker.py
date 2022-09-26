# assert that an entered coupon is valid


import string
from datetime import date, datetime


months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
            'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    """this is a longer version...not best practices"""
    if entered_code  != correct_code: return False
    x = current_date.translate(str.maketrans('','',string.punctuation)).split()
    y = expiration_date.translate(str.maketrans('','',string.punctuation)).split()

    x = datetime(int(x[-1]), int(months[x[0]]), int(x[1]))
    y = datetime(int(y[-1]), int(months[y[0]]), int(y[1]))

    if x > y: return False

    return True




test1 = print(check_coupon('123','123','September 5, 2022','September 5, 2023'))
test2 = print(check_coupon('123','123a', 'October 10, 2022', 'May 5, 2022'))
