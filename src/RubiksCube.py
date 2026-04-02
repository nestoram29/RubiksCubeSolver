from itertools import product
import numpy as np
from termcolor import colored
import sys

class RubiksCube:
    bgColors = ('green', 'red', 'blue', 'magenta', 'white', 'yellow')

    faces = {
        'L': slice(0, 9),
        'F': slice(9, 18),
        'R': slice(18, 27),
        'B': slice(27, 36),
        'U': slice(36, 45),
        'D': slice(45, 54),
    }

    faceEdges = {
        'L': [36, 39, 42, 9, 12, 15, 45, 48, 51, 35, 32, 29],
        'F': [42, 43, 44, 18, 21, 24, 47, 46, 45, 8, 5, 2],
        'R': [44, 41, 38, 27, 30, 33, 53, 50, 47, 17, 14, 11],
        'B': [38, 37, 36, 0, 3, 6, 51, 52, 53, 26, 23, 20],
        'U': [29, 28, 27, 20, 19, 18, 11, 10, 9, 2, 1, 0],
        'D': [15, 16, 17, 24, 25, 26, 33, 34, 35, 6, 7, 8],
    }

    slices = {
        'M': ['L.', 'R'],
        'E': ['U', 'D.'],
        'S': ['F.', 'B'],
    }

    wideMoves = {
        'u': 'D',
        'd': 'U',
        'r': 'L',
        'l': 'R',
        'f': 'B',
        'b': 'F',
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
    
    def doMove(self, move):        
        if move[0] in RubiksCube.faces:
            self._faceMove(move)
        elif move[0] in RubiksCube.slices:
            self._sliceMove(move)
        else:
            self._wideMove(move)


    def _faceMove(self, move):
        '''
        Face Turns:
        U  D  R  L  F  B  (clockwise)
        U' D' R' L' F' B' (counterclockwise)
        U2 D2 R2 L2 F2 B2
        '''
        direction = -1 # Clockwise

        if len(move) == 2:
            direction = 2 if move[1] == '2' else 1

        face = RubiksCube.faces[move[0]]

        self.cube[face] = np.rot90(
            self.cube[face].reshape(3, 3),
            k = direction,
        ).flatten()

        edgeIndices = RubiksCube.faceEdges[move[0]]

        self.cube[edgeIndices] = np.roll(self.cube[edgeIndices], -3 * direction)

    def _sliceMove(self, move):
        '''
        Slice Moves
        M  E  S
        M' E' S'
        M2 E2 S2
        (M follows L)
        (E follows D)
        (S follows F)
        '''
        modifier = move[1] if len(move) == 2 else None

        faceMoves = RubiksCube.slices[move[0]]

        for faceMove in faceMoves:
            if modifier == '2':
                faceMove = f'{faceMove[0]}2'
            elif modifier is not None:
                faceMove = faceMove[0] + ('.' if len(faceMove) != 2 else '')

            self._faceMove(faceMove)

    def _wideMove(self, move):
        '''
        Wide Moves
        u  d  r  l  f  b
        u' d' r' l' f' b'
        '''
        # TODO: fix reverse issue
        self.doMove(RubiksCube.wideMoves[move])
    
    def doMoves(self, moves):
        if isinstance(moves, str):
            moves = moves.split()

        for move in moves:
            self.doMove(move)

if __name__ == '__main__':
    r = RubiksCube()
    print(r)

    if len(sys.argv) > 1:
        r.doMoves(sys.argv[1:])
    else:
        superflip = "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"
        r.doMoves(superflip)

    print(r)