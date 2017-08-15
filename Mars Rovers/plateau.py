class Plateau(object):
    """ This class defines plateau.

    A plateau is a rectangular area in which rovers can move.
    The rectangular area is created as a matrix of size_x per size_y, in which
    every element is an int representing the id of a Rover in that position or 0
    if there is no Rover.
    """

    def __init__(self, plateau_right_x, plateau_top_y):
        self.size_x = plateau_right_x
        self.size_y = plateau_top_y
        self.rectangle = [[0]*(self.size_y+1) for x in range(self.size_x+1)]
        self.rovers = []

    def contains_rover(self, position):
        """ This method checks if there is a rover in the given position.

        args: position: a tuple containing the position to be checked.

        returns: a bool indicating if there is or not a Rover in the given
        position.
        """

        if self.rectangle[position[0]][position[1]] == 0:
            return False
        else:
            return True

    def deploy_rover(self, rover):
        """ This method inserts a rover in the plateau if there is no rover in
        the current position

        args: rover: the object Rover wich is going to be inserted in the plateau
        """

        if not self.contains_rover((rover.x, rover.y)):
            rover.plateau = self
            self.rovers.append(rover)
            self.rectangle[rover.x][rover.y] = rover.id

    def run_rovers(self):
        """ Calls each rovers to runs their instructions sequencially """

        for rover in self.rovers:
            rover.run_instructions()

    def print_rovers(self):
        """ Calls each rover in the plateau to print their coordinates """
        for rover in self.rovers:
            rover.show_coordinates()
