import re


def validate_user(username):
    """validate username using regex
    use match method where: the username contains 4-16 characters in [a-z0-9_]"""
    return bool(re.match("^[a-z0-9_]{4,16}$",username)) != None


test1 = print(validate_user("hallo2"))
test2 = print(validate_user('1234'))
test3 = print(validate_user('nic'))
