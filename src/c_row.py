class Row:
    """
    Defines a row object according to bookshelf format
    """

    counter = -1

    def __init__(self):
        Row.counter += 1
        self.id = Row.counter

        self.corerow = None  # low-y
        self.higher_y = None  # high-y
        self.subroworigin = None  # left-x
        self.height = None
        self.sitespacing = None  # absolute distance between placement sites in a row
        self.numsites = None  # number of placements in row
        self.right_x = None  # = subroworigin + numsites * sitespacing
        self.area = None

    def calculate_remaining_coordinates(self):
        self.right_x = self.subroworigin + self.numsites * self.sitespacing
        self.higher_y = self.corerow + self.height

    def calculate_area(self):
        self.area = self.higher_y - self.corerow * self.right_x - self.subroworigin

    def generate_row(self, tmp: list):
        """
        Custom row constructor compatible to info given by file-parsing
        :param tmp:
        :return:
        """

        self.corerow = tmp[0]
        self.subroworigin = tmp[3]
        self.height = tmp[1]
        self.sitespacing = tmp[2]
        self.numsites = tmp[4]

        self.calculate_remaining_coordinates()
        self.calculate_area()
