from face import Face


class Cube:
    """
    Here is a concept of what the cube looks like, and how it's laid out
            Y|Y|Y
            Y|Y|Y
            Y|Y|Y
            -----
    B|B|B | R|R|R | G|G|G | O|O|O
    B|B|B | R|R|R | G|G|G | O|O|O
    B|B|B | R|R|R | G|G|G | O|O|O
            -----
            W|W|W
            W|W|W
            W|W|W
    """

    def __init__(self):
        self.top   = Face('Y')
        self.left  = Face('B')
        self.right = Face('G')
        self.front = Face('R')
        self.down  = Face('W')
        self.back  = Face('O')

    def reset_cube(self):
        self.top.reset()
        self.left.reset()
        self.right.reset()
        self.front.reset()
        self.down.reset()
        self.back.reset()

    # To execute a "turn" most of this is simple and intuitive
    # For example a "r" consists of rotating the right face, and swapping around the right slices of the faces affected
    # Most of these are straight forward, as the "right" slice makes sense
    # Based on how you turn the cube to look at that side
    # The only exception is the back face, there are two ways to turn the cube, logically, to see the back face
    # So that we can imagine which one the right slice is.
    # Due to this, we need to set a precedent for this, and we'll use the example cube shown above.
    # This means to see the back face, we ONLY turn on the y axis 180 degrees
    # Therefore the right slice of the back face, is directly in line with the left slice of the front face

    def r(self, inverted=False):
        """Spins the right face, clockwise if inverted is passed, counter-clockwise otherwise"""
        if not inverted:
            self.right.clockwise()
            temp = self.front.right
            self.front.right = self.down.right
            self.down.right = self.back.left[::-1]
            self.back.left = self.top.right[::-1]
            self.top.right = temp
        else:
            self.right.counter_clockwise()
            temp = self.front.right
            self.front.right = self.top.right
            self.top.right = self.back.left[::-1]
            self.back.left = self.down.right[::-1]
            self.down.right = temp

    def l(self, inverted=False):
        """Spins the left face, clockwise if inverted is passed, counter-clockwise otherwise"""
        if not inverted:
            self.left.clockwise()
            temp = self.front.left
            self.front.left = self.top.left
            self.top.left = self.back.right[::-1]
            self.back.right = self.down.left[::-1]
            self.down.left = temp
        else:
            self.left.clockwise()
            temp = self.front.left
            self.front.left = self.down.left
            self.down.left = self.back.right[::-1]
            self.back.right = self.top.left[::-1]
            self.top.left = temp

    def d(self, inverted=False):
        """Spins the down face, clockwise if inverted is passed, counter-clockwise otherwise"""
        if not inverted:
            self.down.clockwise()
            temp = self.front.bottom
            self.front.bottom = self.left.bottom
            self.left.bottom = self.back.bottom
            self.back.bottom = self.right.bottom
            self.right.bottom = temp
        else:
            self.down.counter_clockwise()
            temp = self.front.bottom
            self.front.bottom = self.right.bottom
            self.right.bottom = self.back.bottom
            self.back.bottom = self.left.bottom
            self.left.bottom = temp

    def u(self, inverted=False):
        """Spins the up face, clockwise if inverted is passed, counter-clockwise otherwise"""
        if not inverted:
            self.down.clockwise()
            temp = self.front.bottom
            self.front.top = self.right.top
            self.right.top = self.back.top
            self.back.top = self.left.top
            self.left.top = temp
        else:
            self.down.counter_clockwise()
            temp = self.front.top
            self.front.top = self.left.top
            self.left.top = self.back.top
            self.back.top = self.right.top
            self.right.top = temp

    def f(self, inverted=False):
        """Spins the up face, clockwise if inverted is passed, counter-clockwise otherwise"""
        if not inverted:
            self.front.clockwise()
            temp = self.top.bottom
            self.top.bottom = self.left.right[::-1]
            self.left.right = self.down.top
            self.down.top = self.right.left[::-1]
            self.right.left = temp
        else:
            self.front.counter_clockwise()
            temp = self.top.bottom
            self.top.bottom = self.right.left
            self.right.left = self.down.top[::-1]
            self.down.top = self.left.right
            self.left.right = temp[::-1]

    def b(self, inverted=False):
        """Spins the back face, clockwise if inverted is passed, counter-clockwise otherwise"""
        if not inverted:
            self.back.clockwise()
            temp = self.top.top
            self.top.top = self.right.right
            self.right.right = self.down.bottom[::-1]
            self.down.bottom = self.left.left
            self.left.left = temp[::-1]
        else:
            self.back.counter_clockwise()
            temp = self.top.top
            self.top.top = self.left.left[::-1]
            self.left.left = self.down.bottom
            self.down.bottom = self.right.right[::-1]
            self.right.right = temp
