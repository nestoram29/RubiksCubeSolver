from itertools import product
import numpy as np
from termcolor import colored

class RubiksCube:
    bgColors = ('green', 'red', 'blue', 'magenta', 'white', 'yellow')

    def __init__(self, startState = None):
        self.cube = np.arange(3 * 3 * 6)
    
    def __str__(self):
        def getCliStr(i):
            i = self.cube[i]
            return colored(
                f'{i:2d}',
                'black',
                f'on_{RubiksCube.bgColors[i // 9 % 6]}',
                ['bold']
                )
        
        s = ''

        # Top Face
        for i in range(36, 43, 3):
            s += ' ' * 9
            for j in range(3):
                s += f'{getCliStr(i + j)} '
            
            s += '\n'

        # Left, Front, Right, Back Faces
        for i in range(0, 9, 3):
            for j, k in product(range(i, 28 + i, 9), range(3)):
                s += f'{getCliStr(j + k)} '
            
            s += '\n'
        
        # Bottom Face
        for i in range(45, 52, 3):
            s += ' ' * 9
            for j in range(3):
                s += f'{getCliStr(i + j)} '
            
            s += '\n'

        return s

    def scramble(self):
        pass
    
    def checkInValidState(self):
        pass
    
    def makeMove(self, move):
        '''
        Notation

        Face Turns:
        U  D  R  L  F  B  (clockwise)
        U' D' R' L' F' B' (counterclockwise)
        U2 D2 R2 L2 F2 B2

        Wide Moves
        u  d  r  l  f  b
        u' d' r' l' f' b'

        Slice Moves
        M  E  S
        M' E' S'
        M2 E2 S2
        (M follows L)
        (E follows D)
        (S follows F)
        '''
        move = [c for c in move]

        face = move[0]
        direction = -1 # Clockwise

        if len(move) == 2:
            direction = 2 if move[1] == '2' else 1            
        
        faceSlice = {
            'L': slice(0, 9),
            'F': slice(9, 18),
            'R': slice(18, 27),
            'B': slice(45, 54),
            'U': slice(36, 45),
            'D': slice(45, 54),
        }
        face = faceSlice[move[0]]

        self.cube[face] = np.rot90(
            self.cube[face].reshape(3, 3),
            k = direction,
        ).flatten()

        # TODO: don't forget face edges

if __name__ == '__main__':
    r = RubiksCube()
    print(r)

    r.makeMove('U')
    print(r)

    r.makeMove('L2')
    print(r)