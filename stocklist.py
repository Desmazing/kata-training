#  categories and quantities. find the total quantity for each category


def stock_list(l_Art, l_Cat):
    qty_dict =  {}
    survey_dict = {}
    output = ''
    for i in l_Art:
        total = 0
        x = i.split(' ')
        if i[0] in survey_dict.keys():
            survey_dict[i[0]] += int(x[-1])
        else:
            survey_dict[i[0]] = int(x[-1])
        
    for i in l_Cat:
        if i in survey_dict.keys():
            output += f'({i} : {survey_dict[i]}) - '
        else:
            output += f"({i} : 0) - "
    return output.rstrip(' - ')


test1 = print(stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"]))
#  should return "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"

test2 = print(stock_list(["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"]))
# should return "(A : 200) - (B : 1140)"
