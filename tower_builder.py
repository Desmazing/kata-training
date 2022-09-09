# Build a star pyramid tower


def tower_builder(n_floors):
    tower = []
    stars = []
    count = 1
    while n_floors > 0:
        stars.append('*' * count)
        count += 2
        n_floors -= 1
    for i in stars:
        tower.append(i.center(len(stars[-1])))
    return tower

test1 = print(tower_builder(5))
