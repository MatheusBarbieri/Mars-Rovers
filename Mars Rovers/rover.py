class Rover(object):
    """ This class defines the Rover objects. It contains the methods used
    by the rover to move.
    """

    rover_count = 0

    def __init__(self, starting_x, starting_y, starting_direction, rover_instructions):
        self.x = starting_x
        self.y = starting_y
        self.direction = starting_direction
        #Increment to count each rover
        Rover.rover_count += 1
        self.id = Rover.rover_count
        self.rover_instructions = rover_instructions

        #Non initialized information
        self.plateau = None

    def move_forward(self):
        """ This method moves the rover foward if its inside the plateau and
        there is no rover currently in front of it in front of it """

        front_pos = self._front()

        if (front_pos[0] <= self.plateau.size_x and front_pos[0] >= 0 and front_pos[1] <= self.plateau.size_y and front_pos[1] >= 0):
            if not self.plateau.contains_rover(front_pos):
                self.plateau.rectangle[front_pos[0]][front_pos[1]] = self.plateau.rectangle[self.x][self.y]
                self.plateau.rectangle[self.x][self.y] = 0
                self.x, self.y = front_pos

    def rotate_left(self):
        """ This method rotates the rover left """

        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'W':
            self.direction = 'S'
        else:
            self.direction = 'N'

    def rotate_right(self):
        """ This method rotates the rover right """

        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'
        else:
            self.direction = 'S'

    def run_instructions(self):
        """ This method executes the instructions given to a single rover """

        for instruction in self.rover_instructions:
            if instruction == 'L':
                self.rotate_left()
            elif instruction == 'R':
                self.rotate_right()
            elif instruction == 'M':
                self.move_forward()

    def show_coordinates(self):
        """ This method prints the current coordinates of the rover to stdout """

        print(str(self.x) + " " + str(self.y) + " " + self.direction)

    def _front(self):
        """ Computes the position in front of the rover
        return: A tuple containing the front position (x,y) """

        if self.direction == 'N':
            return (self.x, self.y+1)
        elif self.direction == 'S':
            return (self.x, self.y-1)
        elif self.direction == 'W':
            return (self.x-1, self.y)
        else:
            return (self.x+1, self.y)
