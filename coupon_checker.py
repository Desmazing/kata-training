# assert that an entered coupon is valid


import string
from datetime import date, datetime
from dateutil import parser


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


def check_coupon2(entered_code, correct_code, current_date, expiration_date):
    """this is a refactored version using strptime() to create a date-time object from the given dates
    it is more comprehensive"""
    if entered_code != correct_code: return False
    date1 = datetime.strptime(current_date, '%B %d, %Y')
    date2 = datetime.strptime(expiration_date, '%B %d, %Y')
    if date1 > date2: return False
    return True


def check_coupon3(entered_code, correct_code, current_date, expiration_date):
    """an even more refactored version...still using strptime() method"""
    date1 = datetime.strptime(current_date, '%B %d, %Y')
    date2 = datetime.strptime(expiration_date, '%B %d, %Y')
    return entered_code is correct_code and date2 > date1


def check_coupon4(entered_code, correct_code, current_date, expiration_date):
    """Parse the dates using dateutil module parser"""
    date1 = parser.parse(current_date)
    date2 = parser.parse(expiration_date)
    return entered_code is correct_code and date1 < date2


test1 = print(check_coupon('123','123','September 5, 2022','September 5, 2023'))
test2 = print(check_coupon('123','123a', 'October 10, 2022', 'May 5, 2022'))
print('\n')
test3 = print(check_coupon2('123','123','September 5, 2022','September 5, 2023'))
test4 = print(check_coupon2('123','123a', 'October 10, 2022', 'May 5, 2022'))
print('\n')
test5 = print(check_coupon3('123','123','September 5, 2022','September 5, 2023'))
test6 = print(check_coupon3('123','123a', 'October 10, 2022', 'May 5, 2022'))
print('\n')
test7 = print(check_coupon4('123','123','September 5, 2022','September 5, 2023'))
test8 = print(check_coupon4('123','123a', 'October 10, 2022', 'May 5, 2022'))
