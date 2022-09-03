#  this function takes and input of two ipv4 addresses(strings) eg. 10.0.0.0and 
# returns the no. of ip addresses between them excluding the last one
# the latter is always larger than the former

def no_of_ips(ip1, ip2):
    ip1, ip2 = ip1.split('.'), ip2.split('.')
    total_1 = (int(ip1[0]) * 16777216) + (int(ip1[1]) * 65536) + (int(ip1[2]) * 256) + (int(ip1[3]) * 1)
    total_2 = (int(ip2[0]) * 16777216) + (int(ip2[1]) * 65536) + (int(ip2[2]) * 256) + (int(ip2[3]) * 1)
    return total_2 - total_1


test1 = print(no_of_ips('10.0.0.0', '10.0.1.0'))
test2 = print(no_of_ips('10.0.0.0', '10.0.0.50'))
test2 = print(no_of_ips('20.0.0.0', '20.2.0.0'))
