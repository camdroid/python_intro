class Shape(object):
    # Class members can be declared like this
    title = "Circle"

    # Constructor method
    def __init__(self, x, y):
        # Class members can also be declared like this
        self.x = x
        self.y = y

    def set_title(self, title):
        # Or changed like this
        self.title = title

    def get_title(self):
        # Or retrieved like this
        return self.title

shape = Shape(1, 2)
shape.set_title('Square')
print(shape.get_title())
