"""Create a function to return all rotations of a string"""


def contain_all_rotations(str, strarr):
    lst1 = []
    for i in len(str):
        


contain_all_rotations("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) #should return True
contain_all_rotations("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]) #should return False
contain_all_rotations("QJAhQmS", ["hQmSQJA", "QJAhQmS", "QmSQJAh", "yUgUXoQE", "AhQmSQJ", "mSQJAhQ", "SQJAhQm", "JAhQmSQ"]) #should return True
contain_all_rotations("Etsshp", ["nVOETcaxdvuk", "shpEts", "hpEtss", "Etsshp", "OuIiQ", "sXrDdPXIaW", "tsshpE", "pEtssh"]) #should return False
contain_all_rotations("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl"]), #should return False
contain_all_rotations("MqhWvHF", ["numMfygcH", "HFMqhWv", "qhWvHFM", "ZJKKxM", "hWvHFMq", "MqhWvHF", "hfZWYSqk", "BTcSoEdchPlL", "WvHFMqh", "vHFMqhW", "FMqhWvH"]) #should return True
contain_all_rotations("UDvG", ["vGUD", "UDvG", "GUDv", "DvGU"]) #should return True
