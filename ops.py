# arithmetic operators


def ops():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    op = input("Enter operator")
    op_list = ['+', '-', '/', '*', '%', '//']
    
    return a+b if op=='+' else a-b if op=='-' else a*b if op=='*' else a/b if op=='/' else a%b if op=='%' else a//b if op=='//' else 'Try again'


test1 = print(ops())
