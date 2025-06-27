"""A program that takes an integer and inserts dashes between
consecutive odd numbers"""


def insert_dashes(num):
    """Function to insert dashes between consecutive odd numbers
    Args(1): int
    Returns: str"""
    num = str(num)
    combinations = ["13","31","15","51","17","71","19","91","35","53","37","73",
    "39","93","57","75","59","95","79","97"]
    # new_str = ""

    # for i,j in enumerate(num):
    #     print(i,j)

    print(list(zip(num[::],num[1::])))

insert_dashes(1234795)
