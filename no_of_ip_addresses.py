#  this function takes and input of two ipv4 addresses(strings) eg. 10.0.0.0and 
# returns the no. of ip addresses between them excluding the last one
# the latter is always larger than the former


def no_of_ips(ip1, ip2):
    """this version uses manual calculations in each section of the ipv4 
    to compute total no of ip addresses"""
    ip1, ip2 = ip1.split('.'), ip2.split('.')
    total_1 = (int(ip1[0]) * 16777216) + (int(ip1[1]) * 65536) + (int(ip1[2]) * 256) + (int(ip1[3]) * 1)
    total_2 = (int(ip2[0]) * 16777216) + (int(ip2[1]) * 65536) + (int(ip2[2]) * 256) + (int(ip2[3]) * 1)
    return total_2 - total_1


def no_of_ips2(ip1, ip2):
    """this version uses for loops to compute the total no of ip addresses
    in each section of the ipv4 addresses"""
    ip1, ip2 = ip1.split('.'), ip2.split('.')
    total1, total2 = 0, 0
    for ind,num in enumerate(reversed(ip1)):
        total1 += int(num) * (256 ** ind)
    for ind,num in enumerate(reversed(ip2)):
        total2 += int(num) * (256 ** ind)
    return total2-total1


test1 = print(no_of_ips('10.0.0.0', '10.0.1.0'))  # test case for function 1
test2 = print(no_of_ips('10.0.0.0', '10.0.0.50')) # test case for function 2
test2 = print(no_of_ips2('20.0.0.0', '20.2.0.0'))
