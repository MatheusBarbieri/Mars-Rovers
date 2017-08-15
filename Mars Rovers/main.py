import sys
from rover import Rover
from plateau import Plateau

def main():
    right_x, top_y = map(int, sys.stdin.readline().strip().split())
    plateau = Plateau(right_x, top_y)

    while (True):
        """ Parsing Rovers information """

        rover_info = sys.stdin.readline()

        #Cheks if end of file (no rovers left)
        if rover_info == "":
            break

        rover_x, rover_y, rover_direction = rover_info.strip().split()
        rover_x = int(rover_x)
        rover_y = int(rover_y)
        rover_instructions = sys.stdin.readline()
        rover_instructions = rover_instructions.strip()
        new_rover = Rover(rover_x, rover_y, rover_direction, rover_instructions)
        plateau.deploy_rover(new_rover)

    plateau.run_rovers()
    plateau.print_rovers()

if __name__ == '__main__':
    main()
