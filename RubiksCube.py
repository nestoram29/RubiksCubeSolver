import numpy as np
from termcolor import colored

class RubiksCube:
    bgColors = ('green', 'red', 'blue', 'magenta', 'white', 'yellow')
    fgColors = ('white', 'white', 'white', 'white', 'black', 'black')

    def __init__(self, startState = None):
        self.cube = np.arange(3 * 3 * 6)
    
    def __str__(self):
        def getCliStr(i):
            return colored(
                f'{i:2d}',
                f'{RubiksCube.fgColors[int(i / 9) % 6]}',
                f'on_{RubiksCube.bgColors[int(i / 9) % 6]}'
                )
        
        s = ''
        for i in range(0, 9, 3):
            for j in range(i, 28 + i, 9):
                for k in range(3):
                    s += f'{getCliStr(j + k)} '
            
            s += '\n'
        
        return s

#         return f'''
#           {rowToStr(36, 39)}
#           {rowToStr(39, 42)}
#           {rowToStr(42, 45)}
#          ------------
# {rowToStr(0, 3)} | {rowToStr(9, 12)} | {rowToStr(18, 21)} | {rowToStr(27, 30)} 
# {rowToStr(3, 6)} | {rowToStr(12, 1)} | {rowToStr(c[21, 24])} | {rowToStr(30, 33)} 
# {rowToStr(6, 9)} | {rowToStr(15, 1)} | {rowToStr(24, 27)} | {rowToStr(33, 36)}
#          ------------
#           {rowToStr(45, 48)}
#           {rowToStr(48, 51)}
#           {rowToStr(51, )}
# '''

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
        pass