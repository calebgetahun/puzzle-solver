from collections import defaultdict
"""
3x3 color representation of final state

              | ooo |
        *     | ooo | 
        *     | ooo |
        +-----+-----+-----+-----+
        | ggg | www | bbb | yyy |
        | ggg | www | bbb | yyy |
        | ggg | www | bbb | yyy | 
        +-----+-----+-----+-----+
         *    | rrr |
         *    | rrr | 
         *    | rrr |

        Representation of each face with numbers
                   | 36 37 38 |
        *          | 39 40 41 | 
        *          | 42 43 44 |
        +-----+-----+-----+-----+
        | 9  10 11 |   0 1 2  | 18 19 20 | 27 28 29 |
        | 12 13 14 |   3 4 5  | 21 22 23 | 30 31 32 |
        | 15 16 17 |   6 7 8  | 24 25 26 | 33 34 35 | 
        +-----+-----+-----+-----+
         *         | 45 46 47 |
         *         | 48 49 50 | 
         *         | 51 52 53 |

    FRONT side is in the middle (white) and BACK is to the right (yellow)
    g = green, w = white, b = blue, y = yellow, r = red, o = orange

    representation in code: (order of FRONT, LEFT, RIGHT, BACK, TOP, DOWN ordered to reflect camera angle)
    [['white', 'white', 'white'], ['white', 'white', 'white'], ['white', 'white', 'white']]
    [['green', 'green', 'green'], ['green', 'green', 'green'], ['green', 'green', 'green']]
    [['blue', 'blue', 'blue'], ['blue', 'blue', 'blue'], ['blue', 'blue', 'blue']]
    [['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow']]
    [['orange', 'orange', 'orange'], ['orange', 'orange', 'orange'], ['orange', 'orange', 'orange']]
    [['red', 'red', 'red'], ['red', 'red', 'red'], ['red', 'red', 'red']]

    Since state is compressed as a string, final solved state is 
    "111111111222222222333333333444444444555555555666666666777777777888888888999999999"

    center pieces (aka pieces that do not move) are in indices 
    for i in range(len(number of cube faces)):
        center index = 4 + (9*i)

"""

class Cube:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    #one of F, L, R, B, T, D, lowercase versions, and move+2 versions

    #TODO figure out way to programmatically apply transformations based on math of different sides and knowledge of where sides would be based on rotation transformations
    # def apply_clockwise(self, face):

    # def apply_counterclockwise(self, face):

    # def apply_double_turn(self, face):

    def apply_move(self, move):
        temp = self.state[:]
        match move:
            case 'F':
                #clockwise front
                self.state[0] = temp[6]
                self.state[1] = temp[3]
                self.state[2] = temp[0]
                self.state[3] = temp[7]
                self.state[5] = temp[1]
                self.state[6] = temp[8]
                self.state[7] = temp[5]
                self.state[8] = temp[2]
                
                #Adjacent faces transformed as a result
                self.state[11] = temp[45]
                self.state[14] = temp[46]
                self.state[17] = temp[47]

                self.state[44] = temp[11]
                self.state[43] = temp[14]
                self.state[42] = temp[17]

                self.state[18] = temp[42]
                self.state[21] = temp[43]
                self.state[24] = temp[44]

                self.state[45] = temp[24]
                self.state[46] = temp[21]
                self.state[47] = temp[18]
            case 'f':
                #counter-clockwise front
                self.state[0] = temp[2]
                self.state[1] = temp[5]
                self.state[2] = temp[8]
                self.state[3] = temp[1]
                self.state[5] = temp[7]
                self.state[6] = temp[0]
                self.state[7] = temp[3]
                self.state[8] = temp[6]

                #Adjacent faces transformed as a result
                self.state[11] = temp[44]
                self.state[14] = temp[43]
                self.state[17] = temp[42]

                self.state[44] = temp[24]
                self.state[43] = temp[21]
                self.state[42] = temp[18]

                self.state[18] = temp[47]
                self.state[21] = temp[46]
                self.state[24] = temp[45]

                self.state[45] = temp[11]
                self.state[46] = temp[14]
                self.state[47] = temp[17]

            # case 'F2':
            
            # case 'L':
            
            # case 'l':

            # case 'L2':

            # case 'R':

            # case 'r':

            # case 'R2':

            # case 'B':

            # case 'b':

            # case 'B2':

            # case 'T':

            # case 't':
                
            # case 'T2':

            # case 'D':

            # case 'd':

            # case 'D2':
