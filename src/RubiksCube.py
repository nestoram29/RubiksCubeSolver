from itertools import product
import numpy as np
from termcolor import colored

class RubiksCube:
    bgColors = ('green', 'red', 'blue', 'magenta', 'white', 'yellow')

    faces = {
        'L': slice(0, 9),
        'F': slice(9, 18),
        'R': slice(18, 27),
        'B': slice(45, 54),
        'U': slice(36, 45),
        'D': slice(45, 54),
    }

    faceEdges = {
        'L': [36, 39, 42, 9, 12, 15, 45, 48, 48, 51, 35, 32, 29],
        'F': [42, 43, 44, 18, 21, 24, 47, 46, 45, 8, 5, 2],
        'R': [44, 41, 38, 27, 30, 33, 53, 50, 47, 17, 14, 11],
        'B': [38, 37, 36, 0, 3, 6, 51, 52, 53, 26, 23, 20],
        'U': [29, 28, 27, 20, 19, 18, 11, 10, 9, 2, 1, 0],
        'D': [15, 16, 17, 24, 25, 26, 33, 34, 35, 6, 7, 8],
    }

    slices = {
        'M': [37, 40, 43, 10, 13, 16, 46, 49, 52, 34, 31, 28],
        'E': [3, 4, 5, 12, 13, 14, 21, 22, 23, 30, 31, 32],
        'S': [39, 40, 41, 19, 22, 25, 50, 49, 48, 7, 4, 1],
    }

    wideMoves = {
        'u': 'E',
        'd': 'E',
        'r': 'M',
        'l': 'M',
        'f': 'S',
        'b': 'S',
    }


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
        move = [c for c in move]

        direction = -1 # Clockwise

        if len(move) == 2:
            direction = 2 if move[1] == '2' else 1            
        
        move = move[0]
        if move in RubiksCube.faces:
            self._faceMove(move, direction)
        elif move in RubiksCube.slices:
            self._sliceMove(move, direction)
        else:
            self._wideMove(move, direction)


    def _faceMove(self, move, direction):
        '''
        Face Turns:
        U  D  R  L  F  B  (clockwise)
        U' D' R' L' F' B' (counterclockwise)
        U2 D2 R2 L2 F2 B2
        '''
        face = RubiksCube.faces[move]

        self.cube[face] = np.rot90(
            self.cube[face].reshape(3, 3),
            k = direction,
        ).flatten()

        edgeIndices = RubiksCube.faceEdges[move]

        self.cube[edgeIndices] = np.roll(self.cube[edgeIndices], -3 * direction)

    def _sliceMove(self, move, direction):
        '''
        Slice Moves
        M  E  S
        M' E' S'
        M2 E2 S2
        (M follows L)
        (E follows D)
        (S follows F)
        '''
        sliceIndices = RubiksCube.slices[move]
        self.cube[sliceIndices] = np.roll(self.cube[sliceIndices], -3 * direction)

    def _wideMove(self, move, direction):
        '''
        Wide Moves
        u  d  r  l  f  b
        u' d' r' l' f' b'
        '''
        self._faceMove(move.upper(), direction)
        self._sliceMove(RubiksCube.wideMoves[move], direction)

if __name__ == '__main__':
    r = RubiksCube()
    print(r)

    r.makeMove('E+')
    print(r)