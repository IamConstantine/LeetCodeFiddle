# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# https://leetcode.com/problems/robot-room-cleaner
# Hard
# T = O(n-m) where n is number of cells and m is number of obstacles
# S = O(n-m)

def cleanRoom(robot):
    """
    :type robot: Robot
    :rtype: None
    """
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def cleanRoomInner(cell, direction):
        visited.add(cell)
        robot.clean()

        # rotate all 4 directions
        for i in range(4):
            new_d = (direction + i) % 4
            new_cell = (cell[0] + directions[new_d][0], \
                        cell[1] + directions[new_d][1])

            if new_cell not in visited and robot.move():
                cleanRoomInner(new_cell, new_d)

                # above turn
                robot.turnRight()
                robot.turnRight()
                robot.move()
                # above turn
                robot.turnRight()
                robot.turnRight()
                # robot reset to the original position for new direction

            robot.turnRight()

    cleanRoomInner((0, 0), 0)
