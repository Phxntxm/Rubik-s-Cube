
class Face:
    """This class holds the information for a single face on a cube
    The idea behind this class is a middle piece, and four slices
    The slices are top, left, bottom, and right
    There will be pieces that overlap, such as the first element
    in the left slice will be the same as the last one in the bottom
    To keep this simple, slices start from top, and left
    So the left slice starts at the top-left corner, and goes down to the bottom-left corner

    A rotation simply consists of shifting around these slices, and leaving the middle piece the same
    Our middle colour will NEVER change, this is not how the cube works.
    Therefore we know what "our" colour is based on the middle piece
    """
    def __init__(self, colour):
        self.middle = colour

        # This class will consist of slices, a left, right, bottom, and top slice
        self._top    = [colour, colour, colour]
        self._left   = [colour, colour, colour]
        self._right  = [colour, colour, colour]
        self._bottom = [colour, colour, colour]

    @property
    def top(self):
        return self._top

    @property
    def left(self):
        return self._left

    @property
    def bottom(self):
        return self._bottom

    @property
    def right(self):
        return self._right

    # The following setters are due to how the slices work
    # If a slice is changed, the neighboring slices *should* change as well
    @top.setter
    def top(self, value):
        self._top = value
        self._left[0]  = value[0]
        self._right[0] = value[2]

    @left.setter
    def left(self, value):
        self._left = value
        self._top[0] = value[0]
        self._bottom[0] = value[2]

    @bottom.setter
    def bottom(self, value):
        self._bottom = value
        self._left[2] = value[0]
        self._right[2] = value[2]

    @right.setter
    def right(self, value):
        self._right = value
        self._top[2] = value[0]
        self._bottom[2] = value[2]

    def clockwise(self):
        """Rotates our face clockwise"""
        temp         = self._top
        self._top    = self._left
        self._left   = self._bottom
        self._bottom = self._right
        self._right  = temp

    def counter_clockwise(self):
        """Rotates our face counter-clockwise"""
        temp          = self._top
        self._top     = self._right
        self._right   = self._bottom
        self._bottom  = self._left
        self._left    = temp

    def reset(self):
        """Resets all slices back to the default middle colour"""
        self._top    = [self.middle, self.middle, self.middle]
        self._left   = [self.middle, self.middle, self.middle]
        self._right  = [self.middle, self.middle, self.middle]
        self._bottom = [self.middle, self.middle, self.middle]
