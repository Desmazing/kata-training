# create a class
# when an object of the class is instantiated, you can assign a ball type or leave it at default


class Ball(object):
    def __init__(self, type = 'regular'):
        self.type = type


ball1 = Ball()
print(ball1.type)

ball2 = Ball("super")
print(ball2.type)
