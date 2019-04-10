'''RubikCube.py
    Linlin Yang, Hooley Cheng
'''

import random

UP_SIDE = 0
DOWN_SIDE = 1
FRONT_SIDE = 2
RIGHT_SIDE = 3
BACK_SIDE = 4
LEFT_SIDE = 5


# <COMMON_DATA>
from typing import List, Union

N_layer = 3  # Use default, but override if new value supplied
# by the user on the command line.



# </COMMON_DATA>

# <COMMON_CODE>
class State:
    def __init__(self, c):
        self.c = c

    def __eq__(self, s2):
        for i in range(6):
            for j in range(N_layer):
                for k in range(N_layer):
                    if not self.c[i][j][k] == s2.c[i][j][k]:
                        return False
        return True

    def __str__(self):
        return str(self.c)

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State([])
        for i in range(6):
            row = []
            for j in range(3):
                col = []
                for k in range(3):
                    col.append(self.c[i][j][k])
                row.append(col)
            news.c.append(row)
        return news

    def can_move(self):
        '''Tests whether it's legal to move .'''
        return True

    def move(self, face, dir):
        global UP_SIDE, DOWN_SIDE, FRONT_SIDE, RIGHT_SIDE, BACK_SIDE, LEFT_SIDE
        news = self.copy()  # start with a deep copy.
        # move the upper side in clockwise direction
        if face == 'Up' and dir == 0:
            temp = news.c[LEFT_SIDE][0]
            news.c[LEFT_SIDE][0] = news.c[FRONT_SIDE][0]
            news.c[FRONT_SIDE][0] = news.c[RIGHT_SIDE][0]
            news.c[RIGHT_SIDE][0] = news.c[BACK_SIDE][0]
            news.c[BACK_SIDE][0] = temp
            news.move_clockwise(UP_SIDE)

        # move the upper side in counter-clockwise direction
        if face == 'Up' and dir == 1:
            temp = news.c[LEFT_SIDE][0]
            news.c[LEFT_SIDE][0] = news.c[BACK_SIDE][0]
            news.c[BACK_SIDE][0] = news.c[RIGHT_SIDE][0]
            news.c[RIGHT_SIDE][0] = news.c[FRONT_SIDE][0]
            news.c[FRONT_SIDE][0] = temp
            news.move_counter_clockwise(UP_SIDE)

        # move the down side in clockwise direction
        if face == 'Down' and dir == 0:
            temp = news.c[LEFT_SIDE][2]
            news.c[LEFT_SIDE][2] = news.c[BACK_SIDE][2]
            news.c[BACK_SIDE][2] = news.c[RIGHT_SIDE][2]
            news.c[RIGHT_SIDE][2] = news.c[FRONT_SIDE][2]
            news.c[FRONT_SIDE][2] = temp
            news.move_clockwise(DOWN_SIDE)

        # move the down side in counter-clockwise direction
        if face == 'Down' and dir == 1:
            temp = news.c[LEFT_SIDE][2]
            news.c[LEFT_SIDE][2] = news.c[FRONT_SIDE][2]
            news.c[FRONT_SIDE][2] = news.c[RIGHT_SIDE][2]
            news.c[RIGHT_SIDE][2] = news.c[BACK_SIDE][2]
            news.c[BACK_SIDE][2] = temp
            news.move_counter_clockwise(DOWN_SIDE)

        # move the front side in clockwise direction
        if face == 'Front' and dir == 0:
            for i in range(3):
                temp = news.c[UP_SIDE][2][i]
                news.c[UP_SIDE][2][i] = news.c[LEFT_SIDE][2 - i][2]
                news.c[LEFT_SIDE][2 - i][2] = news.c[DOWN_SIDE][0][2 - i]
                news.c[DOWN_SIDE][0][2 - i] = news.c[RIGHT_SIDE][i][0]
                news.c[RIGHT_SIDE][i][0] = temp
            news.move_clockwise(FRONT_SIDE)

        # move the front side in counter-clockwise direction
        if face == 'Front' and dir == 1:
            for i in range(3):
                temp = news.c[UP_SIDE][2][i]
                news.c[UP_SIDE][2][i] = news.c[RIGHT_SIDE][i][0]
                news.c[RIGHT_SIDE][i][0] = news.c[DOWN_SIDE][0][2 - i]
                news.c[DOWN_SIDE][0][2 - i] = news.c[LEFT_SIDE][2 - i][2]
                news.c[LEFT_SIDE][2 - i][2] = temp
            news.move_counter_clockwise(FRONT_SIDE)

        # move the back side in clockwise direction
        if face == 'Back' and dir == 0:
            for i in range(3):
                temp = news.c[UP_SIDE][0][i]
                news.c[UP_SIDE][0][i] = news.c[RIGHT_SIDE][i][2]
                news.c[RIGHT_SIDE][i][2] = news.c[DOWN_SIDE][2][2 - i]
                news.c[DOWN_SIDE][2][2 - i] = news.c[LEFT_SIDE][0][2 - i]
                news.c[LEFT_SIDE][0][2 - i] = temp
            news.move_clockwise(BACK_SIDE)

        # move the back side in counter-clockwise direction
        if face == 'Back' and dir == 1:
            for i in range(3):
                temp = news.c[UP_SIDE][0][i]
                news.c[UP_SIDE][0][i] = news.c[LEFT_SIDE][0][2 - i]
                news.c[LEFT_SIDE][0][2 - i] = news.c[DOWN_SIDE][2][2 - i]
                news.c[DOWN_SIDE][2][2 - i] = news.c[RIGHT_SIDE][i][2]
                news.c[RIGHT_SIDE][i][2] = temp
            news.move_counter_clockwise(BACK_SIDE)

        # move the left side in clockwise direction
        if face == 'Left' and dir == 0:
            for i in range(3):
                temp = news.c[FRONT_SIDE][0][i]
                news.c[FRONT_SIDE][0][i] = news.c[UP_SIDE][0][i]
                news.c[UP_SIDE][0][i] = news.c[BACK_SIDE][2 - i][2]
                news.c[BACK_SIDE][2 - i][2] = news.c[DOWN_SIDE][0][i]
                news.c[DOWN_SIDE][0][i] = temp
            news.move_clockwise(LEFT_SIDE)

        # move the left side in counter-clockwise direction
        if face == 'Left' and dir == 1:
            for i in range(3):
                temp = news.c[FRONT_SIDE][0][i]
                news.c[FRONT_SIDE][0][i] = news.c[DOWN_SIDE][0][i]
                news.c[DOWN_SIDE][0][i] = news.c[BACK_SIDE][2 - i][2]
                news.c[BACK_SIDE][2 - i][2] = news.c[UP_SIDE][0][i]
                news.c[UP_SIDE][0][i] = temp
            news.move_counter_clockwise(LEFT_SIDE)

        # move the right side in clockwise direction
        if face == 'Right' and dir == 0:
            for i in range(3):
                temp = news.c[FRONT_SIDE][i][2]
                news.c[FRONT_SIDE][i][2] = news.c[DOWN_SIDE][i][2]
                news.c[DOWN_SIDE][i][2] = news.c[BACK_SIDE][2 - i][0]
                news.c[BACK_SIDE][2 - i][0] = news.c[UP_SIDE][i][0]
                news.c[UP_SIDE][i][0] = temp
            news.move_clockwise(RIGHT_SIDE)

        # move the right side in counter-clockwise direction
        if face == 'Right' and dir == 1:
            for i in range(3):
                temp = news.c[FRONT_SIDE][i][2]
                news.c[FRONT_SIDE][i][2] = news.c[UP_SIDE][i][0]
                news.c[UP_SIDE][i][0] = news.c[BACK_SIDE][2 - i][0]
                news.c[BACK_SIDE][2 - i][0] = news.c[DOWN_SIDE][i][2]
                news.c[DOWN_SIDE][i][2] = temp
            news.move_counter_clockwise(RIGHT_SIDE)

        return news  # return new state

    def move_clockwise(self, side):
        temp = self.c[side][0][2]
        self.c[side][0][2] = self.c[side][0][0]
        self.c[side][0][0] = self.c[side][2][0]
        self.c[side][2][0] = self.c[side][2][2]
        self.c[side][2][2] = temp

        temp = self.c[side][0][1]
        self.c[side][0][1] = self.c[side][1][0]
        self.c[side][1][0] = self.c[side][2][1]
        self.c[side][2][1] = self.c[side][1][2]
        self.c[side][1][2] = temp

    def move_counter_clockwise(self, side):
        temp = self.c[side][0][2]
        self.c[side][0][2] = self.c[side][2][2]
        self.c[side][2][2] = self.c[side][2][0]
        self.c[side][2][0] = self.c[side][0][0]
        self.c[side][0][0] = temp

        temp = self.c[side][0][1]
        self.c[side][0][1] = self.c[side][1][2]
        self.c[side][1][2] = self.c[side][2][1]
        self.c[side][2][1] = self.c[side][1][0]
        self.c[side][1][0] = temp


def goal_test(s):
    '''If each side of 6 sides contains same color, then s is a goal state.'''
    '''goal state = State([[[0,0,0],[0,0,0],[0,0,0]], [[1,1,1],[1,1,1],[1,1,1]],
                           [[2,2,2],[2,2,2],[2,2,2]], [[3,3,3],[3,3,3],[3,3,3]],
                           [[4,4,4],[4,4,4],[4,4,4]], [[5,5,5],[5,5,5],[5,5,5]]),
       where State(Up_side, Down_side, Front_side, Right_side, Back_side, Left_side)'''
    for i in range(6):
        color = s.c[i][0][0]
        for j in range(N_layer):
            for k in range(N_layer):
                if s.c[i][j][k] != color: return False
    return True


def goal_message(s):
    return "Goal"


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)


# </COMMON_CODE>


# <INITIAL_STATE>

def random_initialize():
    cube = []
    for i in range(6):
        row = []
        for j in range(3):
            col = []
            for k in range(3):
                col.append(i)
            row.append(col)
        cube.append(row)

    s = State(cube)
    for i in range(100):
        op = random.choice(OPERATORS)
        s = op.apply(s)

    return s


CREATE_INITIAL_STATE = lambda: random_initialize()

# </INITIAL_STATE>

# <OPERATORS>
directions = ({('Up', 0), ('Up', 1),('Down', 0), ('Down', 1),('Front', 0), ('Front', 1),('Back', 0), ('Back', 1),
                ('Left', 0), ('Left', 1),('Right', 0), ('Right', 1)})

OPERATORS = [Operator('Move the ' + str(f) + ' face in clockwise' if d == 0 else 'Move the ' + str(f) + ' face in counter-clockwise',
                      lambda s: s.can_move(),
                      lambda s, face=f, dir1=d: s.move(face, dir1))
             for (f, d) in directions]
# </OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

