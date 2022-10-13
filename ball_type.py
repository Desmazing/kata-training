# create a class. Basic intro to classes and instances in Python
# when an object of the class is instantiated, you can assign a ball type or leave it at default


class Ball(object):
    def __init__(self, type = 'regular'):
        self.type = type

    def __str__(self):
        """this returns the type of ball 2 as a string"""
        return str(self.type)


ball1 = Ball()
print(ball1.type)

ball2 = Ball("super")
print(ball2.type)
print(ball1)
print(ball2)
